#!/bin/bash

# Setup Cron Job for Automated Honeypot Rotation
# This script sets up a cron job to run every 30 minutes

echo "Setting up automated honeypot rotation cron job..."

# Get the current directory (where the script is located)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Create the cron job command
CRON_COMMAND="*/30 * * * * cd $PROJECT_DIR && python3 code/auto_honeypot_rotator.py single >> logs/cron.log 2>&1"

echo "Project directory: $PROJECT_DIR"
echo "Cron command: $CRON_COMMAND"

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "auto_honeypot_rotator.py"; then
    echo "Cron job already exists. Removing old entry..."
    crontab -l 2>/dev/null | grep -v "auto_honeypot_rotator.py" | crontab -
fi

# Add the new cron job
(crontab -l 2>/dev/null; echo "$CRON_COMMAND") | crontab -

echo "Cron job installed successfully!"
echo ""
echo "Current cron jobs:"
crontab -l
echo ""
echo "The honeypot rotation will now run every 30 minutes automatically."
echo "Logs will be saved to:"
echo "  - logs/auto_rotation.log (rotation operations)"
echo "  - logs/cron.log (cron job output)"
echo "  - logs/commit-logs.csv (commit tracking)"
echo ""
echo "To remove the cron job later, run:"
echo "  crontab -e"
echo "  (then delete the line with auto_honeypot_rotator.py)" 