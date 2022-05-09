#!/usr/bin/env python3
import os

DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb://localhost:27017/")
""" The database URI. """

DATABASE_NAME = os.environ.get("DATABASE_PYMO", "pymo")
""" The database name. """
