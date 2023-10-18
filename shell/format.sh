#!/bin/bash
isort --sl .
black --line-length 120 .
flake8 .
