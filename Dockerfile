FROM alpine:latest
EXPOSE 80
RUN apk add python3 python3-dev py3-pip git
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip3 install Flask requests
WORKDIR /app
RUN git clone https://github.com/collin-clark/site-code-generator.git .
ENTRYPOINT ["python3", "app.py"]
