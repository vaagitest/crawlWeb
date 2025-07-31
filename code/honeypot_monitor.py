#!/usr/bin/env python3
"""
Honeypot Monitor System
Monitors access to honeypot pages and detects crawler activity
"""

import os
import json
import time
from datetime import datetime
from collections import defaultdict

class HoneypotMonitor:
    def __init__(self):
        self.access_log_file = 'logs/honeypot_access.log'
        self.analysis_file = 'logs/honeypot_analysis.json'
        self.honeypot_pages = ['a-6hp.html', 'a-7sm.html']
        
    def log_access(self, url, user_agent, ip_address, timestamp=None):
        """Log access to honeypot pages"""
        if timestamp is None:
            timestamp = datetime.now().isoformat()
            
        log_entry = {
            'timestamp': timestamp,
            'url': url,
            'user_agent': user_agent,
            'ip_address': ip_address,
            'type': 'honeypot_access'
        }
        
        os.makedirs('logs', exist_ok=True)
        with open(self.access_log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
    
    def analyze_access_patterns(self):
        """Analyze access patterns to detect crawler activity"""
        if not os.path.exists(self.access_log_file):
            print("No access log found.")
            return
        
        # Load access logs
        accesses = []
        with open(self.access_log_file, 'r') as f:
            for line in f:
                try:
                    accesses.append(json.loads(line.strip()))
                except:
                    continue
        
        if not accesses:
            print("No access data found.")
            return
        
        # Analyze patterns
        analysis = {
            'total_accesses': len(accesses),
            'unique_ips': len(set(access['ip_address'] for access in accesses)),
            'unique_user_agents': len(set(access['user_agent'] for access in accesses)),
            'access_by_url': defaultdict(int),
            'access_by_ip': defaultdict(int),
            'access_by_user_agent': defaultdict(int),
            'suspicious_activity': []
        }
        
        # Count accesses
        for access in accesses:
            analysis['access_by_url'][access['url']] += 1
            analysis['access_by_ip'][access['ip_address']] += 1
            analysis['access_by_user_agent'][access['user_agent']] += 1
        
        # Detect suspicious patterns
        for ip, count in analysis['access_by_ip'].items():
            if count > 10:  # More than 10 accesses from same IP
                analysis['suspicious_activity'].append({
                    'type': 'high_frequency_ip',
                    'ip': ip,
                    'count': count
                })
        
        # Check for known crawler user agents
        crawler_indicators = ['bot', 'crawler', 'spider', 'scraper', 'googlebot', 'bingbot']
        for access in accesses:
            user_agent_lower = access['user_agent'].lower()
            for indicator in crawler_indicators:
                if indicator in user_agent_lower:
                    analysis['suspicious_activity'].append({
                        'type': 'crawler_user_agent',
                        'user_agent': access['user_agent'],
                        'ip': access['ip_address'],
                        'timestamp': access['timestamp']
                    })
                    break
        
        # Save analysis
        with open(self.analysis_file, 'w') as f:
            json.dump(analysis, f, indent=2)
        
        return analysis
    
    def print_analysis(self):
        """Print current analysis results"""
        analysis = self.analyze_access_patterns()
        if not analysis:
            return
        
        print("\n" + "="*50)
        print("HONEYPOT ACCESS ANALYSIS")
        print("="*50)
        print(f"Total Accesses: {analysis['total_accesses']}")
        print(f"Unique IPs: {analysis['unique_ips']}")
        print(f"Unique User Agents: {analysis['unique_user_agents']}")
        
        print("\nTop Accessed URLs:")
        for url, count in sorted(analysis['access_by_url'].items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {url}: {count} accesses")
        
        print("\nTop IP Addresses:")
        for ip, count in sorted(analysis['access_by_ip'].items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {ip}: {count} accesses")
        
        if analysis['suspicious_activity']:
            print("\n🚨 SUSPICIOUS ACTIVITY DETECTED:")
            for activity in analysis['suspicious_activity']:
                if activity['type'] == 'high_frequency_ip':
                    print(f"  High frequency IP: {activity['ip']} ({activity['count']} accesses)")
                elif activity['type'] == 'crawler_user_agent':
                    print(f"  Crawler detected: {activity['user_agent']} from {activity['ip']}")
        else:
            print("\n✅ No suspicious activity detected")
        
        print("="*50)
    
    def monitor_realtime(self):
        """Monitor access in real-time"""
        print("Starting real-time honeypot monitoring...")
        print("Press Ctrl+C to stop")
        
        last_size = 0
        try:
            while True:
                if os.path.exists(self.access_log_file):
                    current_size = os.path.getsize(self.access_log_file)
                    if current_size > last_size:
                        # New access detected
                        with open(self.access_log_file, 'r') as f:
                            f.seek(last_size)
                            new_lines = f.read()
                            for line in new_lines.strip().split('\n'):
                                if line:
                                    try:
                                        access = json.loads(line)
                                        print(f"[{access['timestamp']}] Access: {access['url']} from {access['ip_address']}")
                                        print(f"  User-Agent: {access['user_agent']}")
                                    except:
                                        continue
                        last_size = current_size
                
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\nStopping real-time monitoring...")

def main():
    monitor = HoneypotMonitor()
    
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'analyze':
            monitor.print_analysis()
        elif sys.argv[1] == 'monitor':
            monitor.monitor_realtime()
        else:
            print("Usage: python honeypot_monitor.py [analyze|monitor]")
            print("  analyze: Show current analysis")
            print("  monitor: Start real-time monitoring")
    else:
        monitor.print_analysis()

if __name__ == "__main__":
    main() 