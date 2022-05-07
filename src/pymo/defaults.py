#!/usr/bin/env python3

import sys

from pythonjsonlogger.jsonlogger import JsonFormatter

LOGGER_NAME = "cyu.lpdw.pymo"
LOGGING_SETTINGS = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "json_formatter": {
            "()": JsonFormatter,
        }
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "json_formatter",
            "level": "DEBUG",
            "stream": sys.stdout,
        }
    },
    "loggers": {
        "": {  # root loggers
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": True,
        },
        "__main__": {  # if __name__ == '__main__'
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": False,
        },
        "pymo": {
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": False,
        }
    },
    "root": {"handlers": ["default"], "level": "INFO", "propagate": False},
}
