#!/usr/bin/env bash

set -e

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "Virtual environment not found"
    exit 1
fi

# Run tests
pytest

exit 0
