#!/bin/bash

# Cron wrapper script for honeypot rotation
# This script sets up the proper environment for the Python script

# Set the project directory
PROJECT_DIR="/Users/mardanlo/Documents/crawlWeb"
cd "$PROJECT_DIR" || exit 1

# Set up environment variables for cron
export HOME="/Users/mardanlo"
export PATH="/Users/mardanlo/.pyenv/shims:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export PYTHONPATH="$PROJECT_DIR:$PYTHONPATH"
export SHELL="/bin/bash"

# Log the start of execution
echo "Cron wrapper started at $(date)" >> logs/cron.log

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 not found in PATH" >> logs/cron.log
    exit 1
fi

# Check if the rotation script exists
if [ ! -f "code/auto_honeypot_rotator.py" ]; then
    echo "Error: auto_honeypot_rotator.py not found" >> logs/cron.log
    exit 1
fi

# Run the rotation script
echo "Starting honeypot rotation at $(date)" >> logs/cron.log
/Users/mardanlo/.pyenv/shims/python3 code/auto_honeypot_rotator.py single >> logs/cron.log 2>&1

# Log the completion
echo "Cron wrapper completed at $(date)" >> logs/cron.log 