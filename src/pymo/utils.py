#!/usr/bin/env python3

from logging.config import dictConfig
import os

import yaml
from pythonjsonlogger import jsonlogger

from pymo import defaults


def get_full_stacktrace():
    import traceback, sys
    exc = sys.exc_info()[0]
    stack = traceback.extract_stack()[:-1]  # last one would be full_stack()
    if exc is not None:  # i.e. an exception is present
        del stack[-1]  # remove call of full_stack, the printed exception
        # will contain the caught exception caller instead
    trc = 'Traceback (most recent call last):\n'
    stackstr = trc + ''.join(traceback.format_list(stack))
    if exc is not None:
        stackstr += '  ' + traceback.format_exc().lstrip(trc)
    return stackstr


def get_environment():
    """ Return current environnement of application.

    :return: Current environment name. "local" if environment is not specified.
    """
    return os.environ.get("APP_ENV", "local")


def setup_logging_from_config(config: dict = defaults.LOGGING_SETTINGS):
    """ Setup logging to use a JSON formatter.

    :param config: The logging configuration to apply.
    """
    dictConfig(config=config)


def setup_logging(yaml_filename: str = None):
    """ Setyp logging strategy.

    :param yaml_filename: The configyration filename to use for logging.
    """
    if yaml_filename is None:
        return setup_logging_from_config()
    with open(yaml_filename, 'r') as file:
        return setup_logging_from_config(yaml.safe_load(file))


def factory(name: str = defaults.LOGGER_NAME, suffix: str = None):
    """A simple loggers factory.

    :param name: The loggers name.
    :param suffix: Optional suffix loggers
    :return: An instance of official Python {logging.Logger}
    """
    if isinstance(suffix, str) and len(suffix) > 0:
        try:
            return logging.getLogger(name).getChild(suffix=suffix)
        except Exception:
            return logging.getLogger(name)
    return logging.getLogger(name)
