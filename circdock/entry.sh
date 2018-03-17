#!/bin/bash
set -xeo pipefail

pip install -r ../requirements.txt

python ./manage.py test
