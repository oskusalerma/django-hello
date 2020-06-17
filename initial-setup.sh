#!/bin/bash

set -e

virtualenv --python=python3 venv
. venv/bin/activate
pip install -U pip
pip install -r requirements-local.txt
deactivate
