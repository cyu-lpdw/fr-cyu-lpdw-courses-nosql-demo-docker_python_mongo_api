FROM python:3.10-alpine as python-builder


COPY ["requirements.txt", "/app/"]
COPY ["requirements-test.txt", "/app/"]

RUN apk add bash \
    && adduser --disabled-password --home /app python \
    && chown -R python.python /app 

WORKDIR "/app"
ENV PATH "/app/.local/bin:${PATH}"
USER python
RUN pip3 install -r requirements.txt \
    && pip3 install -r requirements-test.txt 


FROM python:3.10-alpine as just-python-dependencies 

COPY --from=python-builder ["/app/.local", "/app/.local"]
COPY ["./.dockerfile/adds/", "/"]

RUN apk add bash \
    && adduser --disabled-password --home /app python \
    && chown -R python.python /app \
                              /opt \
    && chmod +x /opt/entrypoint.sh


FROM scratch


COPY --from=just-python-dependencies ["/", "/"]
COPY ["./src", "/app/src"]
COPY ["./test", "/app/test"]

USER python
WORKDIR "/app/src"

ENTRYPOINT ["/opt/entrypoint.sh"]

CMD ["python3", "pymo/main.py"]

