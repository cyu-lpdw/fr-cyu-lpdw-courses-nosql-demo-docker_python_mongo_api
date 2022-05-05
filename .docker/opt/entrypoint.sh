#!/bin/bash

set -e 

export PYTHONPATH="${PYTHONPATH}:/app"

if [ "$1" == "test" ]; then
  pytest test/
else
  exec "$@"
fi

exec "$@"

