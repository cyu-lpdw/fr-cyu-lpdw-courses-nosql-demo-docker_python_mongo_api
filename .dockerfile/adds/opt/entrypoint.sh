#!/bin/sh
set -e

PYTHON_BIN="$(which python3)"

export PYTHONPATH="/app/src:/app/lib/python3.10"
export PATH="${PATH}:/app/.local/bin"

ENTRYPOINT_PYMODULE="/app/src/pymo/main.py"


# echo "Container's IP address: `awk 'END{print $1}' /etc/hosts`"
# echo "$1"
if [ "$1" = 'test' ]; then
  echo '{"command": "test"}'
  cd /app/test \
  && ${PYTHON_BIN} -m unittest test_services.py
elif [ "$1" = 'console' ]; then
  echo '{"command": "console"}'
  cd /app/test \
  && bash
elif [ "$1" = 'wait' ]; then
  echo '{"command": "wait"}' \
  && sleep inifinite
else
  echo '{"command": "' ${PYTHON_BIN} "${ENTRYPOINT_PYMODULE}" "$@" '}' \
  && exec ${PYTHON_BIN} ${ENTRYPOINT_PYMODULE} "$@"
fi
