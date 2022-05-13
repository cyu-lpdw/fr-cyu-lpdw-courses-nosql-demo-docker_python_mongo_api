#!/usr/bin/env python3

import logging

from starlette.requests import Request
from starlette.responses import JSONResponse

from pymo.api import app
from pymo.utils import get_full_stacktrace

gunicorn_logger = logging.getLogger('gunicorn.error')
# logger.handlers = gunicorn_logger.handlers
# logger.setLevel(logging.DEBUG)


@app.middleware("http")
async def error_handler(request: Request, call_next):
    try:
        response = await call_next(request)
    except Exception as e:
        msg = None
        if hasattr(e, "msg"):
            msg = e.msg
        else:
            msg = str(e)
        logging.error(f"Error at: {msg} {get_full_stacktrace()}")
        return JSONResponse({"error": msg})
    return response