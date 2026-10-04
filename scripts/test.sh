#!/usr/bin/env bash

set -e

if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
else
    PYTHON=python
fi

$PYTHON -m pytest -q

echo "TESTS: 4/4"