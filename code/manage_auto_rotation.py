#!/usr/bin/env python3
"""
Manage Automated Honeypot Rotation
Control and monitor the automated rotation system
"""

import os
import sys
import subprocess
import json
from datetime import datetime

class AutoRotationManager:
    def __init__(self):
        self.log_file = 'logs/auto_rotation.log'
        self.cron_log_file = 'logs/cron.log'
        
    def check_cron_status(self):
        """Check if cron job is installed"""
        try:
            result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
            if result.returncode == 0:
                cron_jobs = result.stdout
                if 'auto_honeypot_rotator.py' in cron_jobs:
                    print("✅ Cron job is installed and active")
                    for line in cron_jobs.split('\n'):
                        if 'auto_honeypot_rotator.py' in line:
                            print(f"   Schedule: {line.strip()}")
                    return True
                else:
                    print("❌ Cron job is not installed")
                    return False
            else:
                print("❌ No cron jobs found")
                return False
        except Exception as e:
            print(f"❌ Error checking cron status: {e}")
            return False
    
    def install_cron_job(self):
        """Install the cron job"""
        try:
            script_path = os.path.join(os.getcwd(), 'code', 'setup_cron_job.sh')
            result = subprocess.run(['bash', script_path], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Cron job installed successfully")
                print(result.stdout)
                return True
            else:
                print("❌ Failed to install cron job")
                print(result.stderr)
                return False
        except Exception as e:
            print(f"❌ Error installing cron job: {e}")
            return False
    
    def remove_cron_job(self):
        """Remove the cron job"""
        try:
            result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
            if result.returncode == 0:
                cron_jobs = result.stdout
                # Remove the auto_honeypot_rotator.py line
                new_cron_jobs = '\n'.join([line for line in cron_jobs.split('\n') 
                                          if 'auto_honeypot_rotator.py' not in line])
                
                # Write back the cron jobs without our entry
                subprocess.run(['echo', new_cron_jobs], stdout=subprocess.PIPE)
                subprocess.run(['crontab', '-'], input=new_cron_jobs.encode())
                
                print("✅ Cron job removed successfully")
                return True
            else:
                print("❌ No cron jobs found to remove")
                return False
        except Exception as e:
            print(f"❌ Error removing cron job: {e}")
            return False
    
    def show_recent_logs(self, lines=20):
        """Show recent logs from auto rotation"""
        log_files = [
            ('Auto Rotation Log', self.log_file),
            ('Cron Job Log', self.cron_log_file)
        ]
        
        for log_name, log_file in log_files:
            if os.path.exists(log_file):
                print(f"\n📋 {log_name} (last {lines} lines):")
                print("=" * 50)
                try:
                    with open(log_file, 'r') as f:
                        all_lines = f.readlines()
                        recent_lines = all_lines[-lines:] if len(all_lines) > lines else all_lines
                        for line in recent_lines:
                            print(line.strip())
                except Exception as e:
                    print(f"Error reading {log_file}: {e}")
            else:
                print(f"\n📋 {log_name}: File not found")
    
    def run_test_rotation(self):
        """Run a test rotation cycle"""
        print("🔄 Running test rotation cycle...")
        try:
            result = subprocess.run(['python3', 'code/auto_honeypot_rotator.py', 'single'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Test rotation completed successfully")
                print(result.stdout)
            else:
                print("❌ Test rotation failed")
                print(result.stderr)
        except Exception as e:
            print(f"❌ Error running test rotation: {e}")
    
    def show_status(self):
        """Show overall status of the automated system"""
        print("🤖 Automated Honeypot Rotation Status")
        print("=" * 50)
        
        # Check cron status
        cron_active = self.check_cron_status()
        
        # Check log files
        log_files_exist = os.path.exists(self.log_file) and os.path.exists(self.cron_log_file)
        
        # Check if honeypot files exist
        honeypot_files_exist = os.path.exists('a-6hp.html') and os.path.exists('a-7sm.html')
        
        print(f"Cron Job Active: {'✅ Yes' if cron_active else '❌ No'}")
        print(f"Log Files Exist: {'✅ Yes' if log_files_exist else '❌ No'}")
        print(f"Honeypot Files Exist: {'✅ Yes' if honeypot_files_exist else '❌ No'}")
        
        if cron_active and log_files_exist:
            print("\n🎯 System Status: ACTIVE")
            print("   The automated rotation is running every 30 minutes")
        else:
            print("\n🎯 System Status: INACTIVE")
            print("   Run 'install' to activate the automated system")

def main():
    manager = AutoRotationManager()
    
    if len(sys.argv) < 2:
        print("Usage: python manage_auto_rotation.py [command]")
        print("Commands:")
        print("  status     - Show system status")
        print("  install    - Install cron job")
        print("  remove     - Remove cron job")
        print("  logs       - Show recent logs")
        print("  test       - Run test rotation")
        return
    
    command = sys.argv[1]
    
    if command == 'status':
        manager.show_status()
    elif command == 'install':
        manager.install_cron_job()
    elif command == 'remove':
        manager.remove_cron_job()
    elif command == 'logs':
        lines = int(sys.argv[2]) if len(sys.argv) > 2 else 20
        manager.show_recent_logs(lines)
    elif command == 'test':
        manager.run_test_rotation()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main() 