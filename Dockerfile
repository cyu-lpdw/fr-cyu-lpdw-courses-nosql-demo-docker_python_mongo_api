FROM python:3.10-alpine as python-builder


COPY ["requirements.txt", "/app/"]

RUN apk add bash \
    && adduser --disabled-password --home /app python \
    && chown -R python.python /app 

WORKDIR "/app"
USER python
RUN pip3 install -r requirements.txt \
    && pip3 install -r requirements-test.txt 


FROM python:3.10-alpine as just-python-dependencies 

COPY --from=python-builder ["/app/.local", "/app"]
COPY ["./.docker/", "/"]

RUN apk add bash \
    && adduser --disabled-password --home /app python \
    && chown -R python.python /app \
                              /opt \
    && chmod +x /opt/entrypoint.sh


FROM scratch


COPY --from=just-python-dependencies ["/", "/"]
COPY ["./src", "/app/src"]

USER python

ENTRYPOINT "/opt/entrypoint.sh"

