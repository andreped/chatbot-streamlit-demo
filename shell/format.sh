#!/bin/bash
isort --sl app.py
black --line-length 120 app.py
flake8 app.py
