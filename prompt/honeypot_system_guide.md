# Honeypot URL Rotation System Guide

## Overview

This system implements a sophisticated honeypot trap for web crawler testing. Two special article pages have URLs that change every 5 minutes, allowing you to detect and monitor crawler activity.

## Honeypot Pages

### 1. **a-6hp.html** (Hub-Referenced Honeypot)
- **Purpose**: Referenced in hub pages (hp-1.html, hp-2.html)
- **Detection**: Crawlers following links from hub pages will access this
- **Content**: Advanced Machine Learning Techniques

### 2. **a-7sm.html** (Sitemap-Only Honeypot)
- **Purpose**: Only referenced in sitemap.xml, not linked from other pages
- **Detection**: Crawlers that follow sitemap links will access this
- **Content**: Emerging AI Technologies

## URL Rotation Process

### How It Works
1. **Every 5 minutes**, the system generates new random filenames
2. **Original files** (`a-6hp.html`, `a-7sm.html`) are renamed to random names
3. **New files** with original names are created with the same content
4. **Access is logged** for monitoring and analysis

### Example Rotation
```
Before: a-6hp.html, a-7sm.html
After:  a-6hp.html, a-7sm.html (new files)
       a-x7k9m2.html, a-y4n8p1.html (old files renamed)
```

## Usage Instructions

### 1. Manual URL Rotation
```bash
python3 code/honeypot_url_rotator.py manual
```

### 2. Check Current URL Mappings
```bash
python3 code/honeypot_url_rotator.py status
```

### 3. Start Continuous Rotation (Every 5 minutes)
```bash
python3 code/honeypot_url_rotator.py
# Press Ctrl+C to stop
```

### 4. Monitor Honeypot Access
```bash
# Analyze access patterns
python3 code/honeypot_monitor.py analyze

# Real-time monitoring
python3 code/honeypot_monitor.py monitor
```

## Detection Capabilities

### What the System Detects
1. **Crawlers following hub page links** → Access to a-6hp.html
2. **Crawlers following sitemap links** → Access to a-7sm.html
3. **High-frequency access** → Same IP accessing multiple times
4. **Known crawler user agents** → Bot, crawler, spider indicators

### Log Files Generated
- `logs/honeypot_url_history.json` - Current URL mappings
- `logs/honeypot_rotations.log` - URL rotation history
- `logs/honeypot_access.log` - Access attempts to honeypot pages
- `logs/honeypot_analysis.json` - Analysis of access patterns

## Security Features

### Protected Directories
- `/logs/` - Contains all honeypot logs and analysis
- `/prompt/` - Contains system documentation
- `/code/` - Contains honeypot scripts

### robots.txt Configuration
```
User-agent: Amazonbot
Disallow: /logs/
Disallow: /prompt/
Disallow: /code/
Allow: /

User-agent: Googlebot
Disallow: /logs/
Disallow: /prompt/
Disallow: /code/
Allow: /

User-agent: *
Disallow: /
```

## Monitoring and Analysis

### Real-Time Monitoring
The system provides real-time monitoring of honeypot access:
- **Access timestamps**
- **IP addresses**
- **User agents**
- **URL patterns**

### Analysis Features
- **Suspicious activity detection**
- **High-frequency IP identification**
- **Crawler user agent detection**
- **Access pattern analysis**

## Manual Control

### Why Manual Control?
You requested that URL changes should not happen without your involvement. The system provides:

1. **Manual rotation** - Only when you run the command
2. **Status checking** - See current URL mappings
3. **Analysis tools** - Monitor access patterns
4. **Logging** - Track all activities

### Recommended Workflow
1. **Start monitoring**: `python3 code/honeypot_monitor.py monitor`
2. **Periodically rotate**: `python3 code/honeypot_url_rotator.py manual`
3. **Analyze results**: `python3 code/honeypot_monitor.py analyze`
4. **Check status**: `python3 code/honeypot_url_rotator.py status`

## Integration with Existing System

### Updated Files
- **Hub pages**: Now include links to a-6hp.html
- **Sitemap**: Includes both honeypot pages
- **robots.txt**: Protects sensitive directories
- **Logging**: Integrated with existing commit-logs.csv system

### New Files Created
- `a-6hp.html` - Hub-referenced honeypot page
- `a-7sm.html` - Sitemap-only honeypot page
- `code/honeypot_url_rotator.py` - URL rotation system
- `code/honeypot_monitor.py` - Monitoring and analysis
- `code/create_additional_placeholders.py` - Image generation
- `img/image-6.jpg`, `img/image-7.jpg` - Honeypot page images

## Testing the System

### 1. Test Manual Rotation
```bash
python3 code/honeypot_url_rotator.py manual
ls *.html | grep a-
```

### 2. Test Monitoring
```bash
python3 code/honeypot_monitor.py analyze
```

### 3. Test Real-Time Monitoring
```bash
python3 code/honeypot_monitor.py monitor
# In another terminal, access the honeypot pages
```

## Safety Features

### Backup and Recovery
- **URL history tracking** - Know where files were moved
- **Logging** - Complete audit trail
- **Error handling** - Graceful failure recovery

### Manual Override
- **Stop rotation** - Ctrl+C to stop continuous rotation
- **Manual control** - Only rotate when you want to
- **Status checking** - Always know current state

## Next Steps

1. **Test the system** with manual rotation
2. **Monitor access** to see if crawlers are detected
3. **Analyze patterns** to understand crawler behavior
4. **Adjust timing** if needed (currently 5 minutes)

The system is now ready for web crawler testing with full manual control over URL rotation! 