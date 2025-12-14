from flask import Flask, render_template, request, jsonify
import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
app = Flask(__name__)

# ---------------------------------------------------------
# Config
# ---------------------------------------------------------
LOCODE_URL = (
    "https://pkgstore.datahub.io/core/un-locode/"
    "code-list_json/data/05f6ccfe0cd03ab51bed07273b982df9/"
    "code-list_json.json"
)
CACHE_TTL = 60 * 60 * 24  # 24 hours

# ---------------------------------------------------------
# Cache storage
# ---------------------------------------------------------
LOCODE_CACHE = {
    "data": None,
    "timestamp": 0
}


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------
def get_locode_data():
    """Fetch and cache the UN/LOCODE dataset."""
    now = time.time()

    # Return cached version if still valid
    if LOCODE_CACHE["data"] is not None and (now - LOCODE_CACHE["timestamp"] < CACHE_TTL):
        return LOCODE_CACHE["data"]

    # Otherwise fetch fresh copy
    resp = requests.get(LOCODE_URL, verify=False, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    # Store in memory
    LOCODE_CACHE["data"] = data
    LOCODE_CACHE["timestamp"] = now

    return data


def filter_by_city(city, data):
    """Return matching site records for a given city."""
    city_normalized = city.strip().title()

    matches = []
    for rec in data:
        if rec.get("Name") == city_normalized:
            matches.append({
                "site_code": f"{rec['Country']}-{rec['Location']}",
                "state": rec.get("Subdivision", ""),
                "country_code": rec.get("Country", "")
            })

    return city_normalized, matches


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------
@app.route("/")
def home():
    return render_template("home.html", title="UN/LOCODE Lookup", site_codes=[], city="")


@app.get("/lookup")
def lookup_code():
    """AJAX endpoint used by the frontend fetch() call."""
    city = request.args.get("city", "").strip()

    if not city:
        return jsonify({"error": "City is required."}), 400

    try:
        data = get_locode_data()
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve UN/LOCODE dataset: {str(e)}"}), 500

    city_normalized, matches = filter_by_city(city, data)

    return jsonify({
        "city": city_normalized,
        "site_codes": matches
    })


# ---------------------------------------------------------
# Run
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
