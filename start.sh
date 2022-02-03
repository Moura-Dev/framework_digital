#!/usr/bin/env bash

pip install -r requirements.txt

export FLASK_APP="manage.py"
export FLASK_DEBUG=1

pytest -v

flask run -h 0.0.0.0 -p 5000
