# Automated Honeypot Rotation System - Installation & Usage Instructions

## 🚀 Quick Installation

### Install the Automated System
```bash
python3 code/manage_auto_rotation.py install
```

### Verify Installation
```bash
python3 code/manage_auto_rotation.py status
```

## 📋 System Overview

### What the System Does
- **Rotates honeypot URLs** every 30 minutes automatically
- **Preserves original prefixes** for tracking (e.g., `a-6hp-x7k9m2.html`)
- **Updates git repository** with changes
- **Maintains comprehensive logs** of all operations
- **Pushes to mainline** automatically

### Honeypot Pages
- **`a-6hp.html`** - Referenced in hub pages (hp-1.html, hp-2.html)
- **`a-7sm.html`** - Only referenced in sitemap.xml

## 🔧 Management Commands

### Check System Status
```bash
python3 code/manage_auto_rotation.py status
```
**Output:**
- ✅ Cron job active/inactive
- ✅ Log files exist
- ✅ Honeypot files exist
- 🎯 Overall system status

### View Recent Logs
```bash
# View last 20 lines (default)
python3 code/manage_auto_rotation.py logs

# View more lines
python3 code/manage_auto_rotation.py logs 50
```

### Test Manual Rotation
```bash
python3 code/manage_auto_rotation.py test
```

### Remove Cron Job
```bash
python3 code/manage_auto_rotation.py remove
```

## ⏰ Cron Job Details

### Schedule
- **Frequency**: Every 30 minutes
- **Cron Expression**: `*/30 * * * *`
- **Command**: `python3 code/auto_honeypot_rotator.py single`

### What Happens Every 30 Minutes
1. **URL Rotation**:
   - `a-6hp.html` → `a-6hp-x7k9m2.html`
   - `a-7sm.html` → `a-7sm-y4n8p1.html`
   - New files created with original names

2. **Git Operations**:
   - `git add .` - Stage all changes
   - `git commit` - Commit with timestamp
   - `git push origin main` - Push to mainline

3. **Log Updates**:
   - Update `logs/commit-logs.csv` with rotation entry
   - Commit and push log updates
   - Record operations in `logs/auto_rotation.log`

## 📁 Log Files

### **`logs/auto_rotation.log`**
- Detailed rotation operations
- Git command results
- Error messages and timestamps
- Complete audit trail

### **`logs/cron.log`**
- Cron job output
- System messages
- Execution status
- Background process logs

### **`logs/commit-logs.csv`**
- Updated with each rotation
- Tracks URL changes
- Maintains commit history
- Machine-readable format

### **`logs/honeypot_url_history.json`**
- Current URL mappings
- Rotation history
- File tracking
- JSON format for analysis

## 🔍 Monitoring Commands

### Real-time Log Monitoring
```bash
# Watch auto rotation logs
tail -f logs/auto_rotation.log

# Watch cron job logs
tail -f logs/cron.log

# Watch both simultaneously
tail -f logs/auto_rotation.log logs/cron.log
```

### Check Cron Status
```bash
# View all cron jobs
crontab -l

# Edit cron jobs manually
crontab -e
```

### Check Recent Activity
```bash
# View last 50 log entries
python3 code/manage_auto_rotation.py logs 50

# Check system status
python3 code/manage_auto_rotation.py status
```

## 🛠️ Troubleshooting

### Cron Job Not Running
```bash
# Check if cron is installed
python3 code/manage_auto_rotation.py status

# Reinstall if needed
python3 code/manage_auto_rotation.py install

# Check cron service
sudo launchctl list | grep cron
```

### Git Push Failures
- Check network connection
- Verify git credentials
- Review `logs/auto_rotation.log` for errors
- Ensure repository is up to date

### File Permission Issues
```bash
# Make scripts executable
chmod +x code/setup_cron_job.sh
chmod +x code/auto_honeypot_rotator.py
chmod +x code/manage_auto_rotation.py
```

### Manual Override
```bash
# Stop automated rotation
python3 code/manage_auto_rotation.py remove

# Run manual rotation
python3 code/honeypot_url_rotator.py manual

# Check current status
python3 code/honeypot_url_rotator.py status
```

## 🔒 Safety Features

### Manual Control
- **Stop anytime**: `python3 code/manage_auto_rotation.py remove`
- **Manual rotation**: `python3 code/honeypot_url_rotator.py manual`
- **Status checking**: `python3 code/manage_auto_rotation.py status`

### Error Recovery
- Failed rotations logged with timestamps
- System continues to next cycle even if one fails
- No data loss on failures
- Complete audit trail maintained

### Logging
- All operations timestamped
- Error details captured
- Complete audit trail
- Multiple log files for redundancy

## 📊 System Integration

### Compatible With
- Manual rotation system
- Honeypot monitoring
- Existing commit tracking
- All existing honeypot features

### Enhanced Features
- Automatic git operations
- Comprehensive logging
- Error handling
- Status monitoring
- Background operation

## 🎯 Quick Reference

### Installation
```bash
python3 code/manage_auto_rotation.py install
```

### Status Check
```bash
python3 code/manage_auto_rotation.py status
```

### View Logs
```bash
python3 code/manage_auto_rotation.py logs
```

### Test Rotation
```bash
python3 code/manage_auto_rotation.py test
```

### Remove System
```bash
python3 code/manage_auto_rotation.py remove
```

### Real-time Monitoring
```bash
tail -f logs/auto_rotation.log
```

## 🚀 Next Steps

1. **Install the system**: `python3 code/manage_auto_rotation.py install`
2. **Verify installation**: `python3 code/manage_auto_rotation.py status`
3. **Test the system**: `python3 code/manage_auto_rotation.py test`
4. **Monitor logs**: `python3 code/manage_auto_rotation.py logs`
5. **Set up real-time monitoring**: `tail -f logs/auto_rotation.log`

The automated honeypot rotation system is now ready to run every 30 minutes with full monitoring and control capabilities! 