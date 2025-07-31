#!/bin/bash

# Cron wrapper script for honeypot rotation
# This script sets up the proper environment for the Python script

# Set the project directory
PROJECT_DIR="/Users/mardanlo/Documents/crawlWeb"
cd "$PROJECT_DIR"

# Set up Python environment
export PATH="/Users/mardanlo/.pyenv/shims:$PATH"
export PYTHONPATH="$PROJECT_DIR:$PYTHONPATH"

# Run the rotation script
/Users/mardanlo/.pyenv/shims/python3 code/auto_honeypot_rotator.py single >> logs/cron.log 2>&1 