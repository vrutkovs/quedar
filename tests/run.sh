#!/bin/bash
set -eux

pipenv install --system -d
python3 -m pytest
