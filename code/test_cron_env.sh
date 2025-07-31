#!/bin/bash

# Test script to check cron environment
echo "=== Cron Environment Test ==="
echo "Date: $(date)"
echo "User: $(whoami)"
echo "PWD: $PWD"
echo "PATH: $PATH"
echo "PYTHONPATH: $PYTHONPATH"
echo "HOME: $HOME"
echo "SHELL: $SHELL"

# Test Python availability
echo "=== Python Test ==="
which python3
python3 --version

# Test if we can access the project directory
echo "=== Directory Test ==="
ls -la /Users/mardanlo/Documents/crawlWeb/code/cron_wrapper.sh

# Test if we can run the wrapper
echo "=== Wrapper Test ==="
/Users/mardanlo/Documents/crawlWeb/code/cron_wrapper.sh

echo "=== Test Complete ===" 