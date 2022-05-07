#!/bin/sh
set -e

PYTHON_BIN="$(which python3)"

export PYTHONPATH="${PYTHONPATH}:/app/lib/python3.10"
export PATH="${PATH}:/app/.local/bin"


echo "Container's IP address: `awk 'END{print $1}' /etc/hosts`"
echo "$1"
if [ "$1" = 'test' ]; then
  echo '{"command": "test"}'
  cd /app/test \
  && ${PYTHON_BIN} -m unittest test_services.py
else
  exec "$@"
fi


