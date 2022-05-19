#!/usr/bin/env python3

import logging
import os
import sys

from loguru import logger

LOG_LEVEL = logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG"))
JSON_LOGS = True if os.environ.get("JSON_LOGS", "0") == "1" else False


class InterceptHandler(logging.Handler):
    """
    Logs interceptor.
    """

    def emit(self, record):
        """ Get corresponding Loguru level if it exists.
        :param record: The log record.
        :return:
        """
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logging(JSON_LOGS=True):
    """
    Intercept everything at the root logger.
    """
    intercept_handler = InterceptHandler()
    logging.root.handlers = [intercept_handler]
    logging.root.setLevel(LOG_LEVEL)

    # remove every other logger's handlers
    # and propagate to root logger
    for name in logging.root.manager.loggerDict.keys():
        print(name)
        logging.getLogger(name).handlers = [intercept_handler]
        logging.getLogger(name).propagate = True


    # configure loguru
    logger.configure(handlers=[{"sink": sys.stdout, "serialize": JSON_LOGS}])
