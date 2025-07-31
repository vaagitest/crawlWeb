# Automated Honeypot Rotation System Guide

## Overview

This system automatically rotates honeypot URLs every 30 minutes, updates logs, and pushes changes to mainline git. It's designed to run as a background cron job with full monitoring and control capabilities.

## System Components

### 1. **Auto Honeypot Rotator** (`code/auto_honeypot_rotator.py`)
- **Purpose**: Main automation script that performs rotation cycles
- **Features**: URL rotation, git operations, log updates
- **Schedule**: Every 30 minutes via cron job

### 2. **Cron Job Setup** (`code/setup_cron_job.sh`)
- **Purpose**: Installs the cron job for automated execution
- **Schedule**: `*/30 * * * *` (every 30 minutes)
- **Logging**: All output captured to `logs/cron.log`

### 3. **Management System** (`code/manage_auto_rotation.py`)
- **Purpose**: Control and monitor the automated system
- **Features**: Install/remove cron jobs, view logs, test rotation

## Quick Start

### 1. Install Automated System
```bash
python3 code/manage_auto_rotation.py install
```

### 2. Check Status
```bash
python3 code/manage_auto_rotation.py status
```

### 3. View Logs
```bash
python3 code/manage_auto_rotation.py logs
```

### 4. Test Rotation
```bash
python3 code/manage_auto_rotation.py test
```

## Detailed Usage

### Installation
```bash
# Install the cron job (runs every 30 minutes)
python3 code/manage_auto_rotation.py install

# Verify installation
python3 code/manage_auto_rotation.py status
```

### Monitoring
```bash
# Check system status
python3 code/manage_auto_rotation.py status

# View recent logs (last 20 lines)
python3 code/manage_auto_rotation.py logs

# View more log lines
python3 code/manage_auto_rotation.py logs 50
```

### Testing
```bash
# Run a test rotation cycle
python3 code/manage_auto_rotation.py test

# Run manual rotation
python3 code/auto_honeypot_rotator.py single
```

### Removal
```bash
# Remove the cron job
python3 code/manage_auto_rotation.py remove
```

## What Happens Every 30 Minutes

### 1. **URL Rotation**
- `a-6hp.html` → `a-6hp-x7k9m2.html`
- `a-7sm.html` → `a-7sm-y4n8p1.html`
- New files created with original names

### 2. **Git Operations**
- `git add .` - Stage all changes
- `git commit` - Commit with timestamp
- `git push origin main` - Push to mainline

### 3. **Log Updates**
- Update `logs/commit-logs.csv` with rotation entry
- Commit and push log updates
- Record all operations in `logs/auto_rotation.log`

### 4. **Error Handling**
- Failed operations logged with timestamps
- System continues to next cycle even if one fails
- Complete audit trail maintained

## Log Files

### **`logs/auto_rotation.log`**
- Detailed rotation operations
- Git command results
- Error messages and timestamps

### **`logs/cron.log`**
- Cron job output
- System messages
- Execution status

### **`logs/commit-logs.csv`**
- Updated with each rotation
- Tracks URL changes
- Maintains commit history

### **`logs/honeypot_url_history.json`**
- Current URL mappings
- Rotation history
- File tracking

## Cron Job Details

### **Schedule**: `*/30 * * * *`
- Runs every 30 minutes
- Executes: `python3 code/auto_honeypot_rotator.py single`
- Working directory: Project root
- Output: `logs/cron.log`

### **Cron Job Command**
```bash
*/30 * * * * cd /Users/mardanlo/Documents/crawlWeb && python3 code/auto_honeypot_rotator.py single >> logs/cron.log 2>&1
```

## Safety Features

### **Manual Override**
- Cron job can be stopped anytime
- Manual rotation still available
- Status checking prevents conflicts

### **Error Recovery**
- Failed rotations logged
- System continues to next cycle
- No data loss on failures

### **Logging**
- Complete audit trail
- All operations timestamped
- Error details captured

## Monitoring Commands

### **Check Cron Status**
```bash
crontab -l
```

### **View Real-time Logs**
```bash
tail -f logs/auto_rotation.log
tail -f logs/cron.log
```

### **Check Recent Activity**
```bash
python3 code/manage_auto_rotation.py logs 50
```

## Troubleshooting

### **Cron Job Not Running**
```bash
# Check if cron is installed
python3 code/manage_auto_rotation.py status

# Reinstall if needed
python3 code/manage_auto_rotation.py install
```

### **Git Push Failures**
- Check network connection
- Verify git credentials
- Review `logs/auto_rotation.log` for errors

### **File Permission Issues**
```bash
chmod +x code/setup_cron_job.sh
chmod +x code/auto_honeypot_rotator.py
```

## Integration with Existing System

### **Compatible With**
- Manual rotation system
- Honeypot monitoring
- Existing commit tracking
- All existing honeypot features

### **Enhanced Features**
- Automatic git operations
- Comprehensive logging
- Error handling
- Status monitoring

## Next Steps

1. **Install the system**: `python3 code/manage_auto_rotation.py install`
2. **Test the rotation**: `python3 code/manage_auto_rotation.py test`
3. **Monitor logs**: `python3 code/manage_auto_rotation.py logs`
4. **Check status**: `python3 code/manage_auto_rotation.py status`

The automated system is now ready to run every 30 minutes with full monitoring and control capabilities! 