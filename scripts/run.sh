#!/usr/bin/env bash

set -e

PORT=${PORT:-8080}
export PORT

if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
else
    PYTHON=python
fi

$PYTHON -m app.main
EOF