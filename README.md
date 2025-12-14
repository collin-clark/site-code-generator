# site-code-generator
Generate unique site codes for branch offices and data centers around the world.

## Location Naming Convention (UN/LOCODE–Aligned)
A standardized location naming convention aligned with **UN/LOCODE (United Nations Code for Trade and Transport Locations)** to ensure consistency, global interoperability, and unambiguous identification of locations across systems and documentation.

| Component | UN/LOCODE Term | Description |
|---------|---------------|-------------|
| `CC` | Country Code | ISO 3166-1 alpha-2 country code as defined by UN/LOCODE |
| `-` | Separator | Hyphen delimiter |
| `LLL` | Location Code | Three-letter UN/LOCODE location identifier |

- **Country Code (`CC`)**  
  The two-letter code assigned by ISO 3166-1 and used by UN/LOCODE to identify a country or territory.

- **Location Code (`LLL`)**  
  The three-letter code defined by UN/LOCODE that identifies a **city, port, terminal, or trade-relevant location** within a country. The typical use is to use the location of the circuit install.  

## Installation
If you walready have a Flask server prepared, copy ```apps.py``` to the root folder of your Flask project and copy ```home.html``` to the templates folder of your project.
or
Use the Docker image at the following location to get a ready-to-go version.
  
