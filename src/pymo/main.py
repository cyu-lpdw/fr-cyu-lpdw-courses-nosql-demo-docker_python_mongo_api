#!/usr/bin/env python3

import os


import socket

from fastapi import FastAPI, Depends
from uvicorn import Config, Server

from pymo.api import main_router
from pymo.db import DatabaseConnection
from pymo.services import get_services
from pymo.utils.log import setup_logging, LOG_LEVEL

def get_app():
    app = FastAPI()

    db_conn_helper = DatabaseConnection()
    app.state.services = Depends(get_services()).dependency

    # Start or stop database connection on application related events.
    app.add_event_handler("startup", db_conn_helper.open)
    app.add_event_handler("shutdown", db_conn_helper.close)
    app.include_router(main_router)
    return app

app = get_app()

if __name__ == "__main__":
    setup_logging(JSON_LOGS=True)
    hostname = socket.gethostname()
    bind_address = socket.gethostbyname(hostname)
    port = os.environ.get("APP_PORT") or 8081

    server = Server(
        Config(
            "pymo.main:app",
            host=bind_address,
            port=int(port),
            log_level=LOG_LEVEL,
        ),
    )

    # setup logging last, to make sure no library overwrites it
    # (they shouldn't, but it happens)

    server.run()
