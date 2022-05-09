#!/usr/bin/env python3
import uvicorn

from pymo.api import app
from pymo.utils import setup_logging

setup_logging()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
