#!/bin/bash

exprot FLASK_APP=app.py
export FLASK_ENV=development

flask run --port 5000