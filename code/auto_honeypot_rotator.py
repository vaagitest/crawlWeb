#!/usr/bin/env python3
"""
Automated Honeypot URL Rotator
Runs every 30 minutes, rotates URLs, updates logs, and pushes to git
Designed to be run as a cron job
"""

import os
import sys
import time
import subprocess
import json
from datetime import datetime
from honeypot_url_rotator import HoneypotURLRotator

class AutoHoneypotRotator:
    def __init__(self):
        self.rotator = HoneypotURLRotator()
        self.log_file = 'logs/auto_rotation.log'
        self.git_log_file = 'logs/git_operations.log'
        
    def log_operation(self, message, log_type='info'):
        """Log operation with timestamp"""
        timestamp = datetime.now().isoformat()
        log_entry = {
            'timestamp': timestamp,
            'type': log_type,
            'message': message
        }
        
        os.makedirs('logs', exist_ok=True)
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        # Also print to console for cron job visibility
        print(f"[{timestamp}] {message}")
    
    def run_git_command(self, command, description):
        """Run git command and log the result"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=os.getcwd())
            
            if result.returncode == 0:
                self.log_operation(f"Git {description} successful: {result.stdout.strip()}")
                return True
            else:
                self.log_operation(f"Git {description} failed: {result.stderr.strip()}", 'error')
                return False
        except Exception as e:
            self.log_operation(f"Git {description} exception: {str(e)}", 'error')
            return False
    
    def update_sitemap_and_hub_pages(self):
        """Update sitemap.xml and hub pages with new URL mappings"""
        try:
            current_urls = self.rotator.get_current_urls()
            
            # Update sitemap.xml
            if os.path.exists('sitemap.xml'):
                with open('sitemap.xml', 'r') as f:
                    sitemap_content = f.read()
                
                # Replace old URLs with new ones and update dates
                current_date = datetime.now().strftime('%Y-%m-%d')
                for original, current in current_urls.items():
                    if original in ['a-6hp.html', 'a-7sm.html']:
                        new_url = f"https://ai-crawler.org/{current}"
                        
                        # Find and replace any existing honeypot URLs in sitemap
                        # This handles both original and rotated URLs dynamically
                        import re
                        if original == 'a-6hp.html':
                            # Replace any a-6hp-* URL with the new one
                            pattern = r'https://ai-crawler\.org/a-6hp-[^"]*\.html'
                            sitemap_content = re.sub(pattern, new_url, sitemap_content)
                        elif original == 'a-7sm.html':
                            # Replace any a-7sm-* URL with the new one
                            pattern = r'https://ai-crawler\.org/a-7sm-[^"]*\.html'
                            sitemap_content = re.sub(pattern, new_url, sitemap_content)
                
                # Update lastmod dates for all pages
                sitemap_content = sitemap_content.replace('<lastmod>2024-12-15</lastmod>', f'<lastmod>{current_date}</lastmod>')
                
                with open('sitemap.xml', 'w') as f:
                    f.write(sitemap_content)
                
                self.log_operation("Updated sitemap.xml with new URL mappings")
            
            # Update hub pages
            hub_pages = ['hp-1.html', 'hp-2.html']
            for hub_page in hub_pages:
                if os.path.exists(hub_page):
                    with open(hub_page, 'r') as f:
                        hub_content = f.read()
                    
                    # Update a-6hp.html references (only this one is in hub pages)
                    if 'a-6hp.html' in current_urls:
                        old_url = 'a-6hp.html'
                        new_url = current_urls['a-6hp.html']
                        hub_content = hub_content.replace(old_url, new_url)
                    
                    with open(hub_page, 'w') as f:
                        f.write(hub_content)
                    
                    self.log_operation(f"Updated {hub_page} with new URL mappings")
                    
        except Exception as e:
            self.log_operation(f"Error updating sitemap and hub pages: {str(e)}", 'error')
    
    def update_commit_logs(self):
        """Update commit-logs.csv with the latest rotation"""
        try:
            # Get the latest commit ID
            result = subprocess.run(['git', 'log', '--oneline', '-1'], capture_output=True, text=True)
            if result.returncode == 0:
                commit_id = result.stdout.strip().split()[0]
                
                # Read current commit-logs.csv
                csv_file = 'logs/commit-logs.csv'
                if os.path.exists(csv_file):
                    with open(csv_file, 'r') as f:
                        lines = f.readlines()
                    
                    # Add new entry
                    timestamp_ms = int(time.time() * 1000)
                    datetime_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
                    # Get current URL mappings
                    current_urls = self.rotator.get_current_urls()
                    pages_changed = {}
                    
                    for original, current in current_urls.items():
                        if original in ['a-6hp.html', 'a-7sm.html']:
                            pages_changed[original] = [f"URL rotated to {current}"]
                    
                    if pages_changed:
                        pages_json = json.dumps(pages_changed).replace('"', '""')
                        new_line = f"{timestamp_ms},{datetime_str},{commit_id},\"{pages_json}\"\n"
                        
                        # Add to CSV
                        with open(csv_file, 'a') as f:
                            f.write(new_line)
                        
                        self.log_operation(f"Updated commit-logs.csv with rotation entry")
                        
        except Exception as e:
            self.log_operation(f"Error updating commit logs: {str(e)}", 'error')
    
    def perform_rotation_cycle(self):
        """Perform one complete rotation cycle"""
        self.log_operation("Starting automated honeypot rotation cycle")
        
        # Step 1: Rotate URLs
        try:
            self.rotator.rotate_urls()
            self.log_operation("URL rotation completed successfully")
        except Exception as e:
            self.log_operation(f"URL rotation failed: {str(e)}", 'error')
            return False
        
        # Step 2: Add all changes to git
        if not self.run_git_command('git add .', 'add'):
            return False
        
        # Step 3: Commit changes
        commit_message = f"Auto-rotate honeypot URLs - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        if not self.run_git_command(f'git commit -m "{commit_message}"', 'commit'):
            return False
        
        # Step 4: Push to mainline
        if not self.run_git_command('git push origin main', 'push'):
            return False
        
        # Step 5: Update sitemap and hub pages
        self.update_sitemap_and_hub_pages()
        
        # Step 6: Update commit logs
        self.update_commit_logs()
        
        # Step 7: Commit the updated logs
        if not self.run_git_command('git add logs/commit-logs.csv', 'add logs'):
            return False
        
        log_commit_message = f"Update commit logs with rotation - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        if not self.run_git_command(f'git commit -m "{log_commit_message}"', 'commit logs'):
            return False
        
        if not self.run_git_command('git push origin main', 'push logs'):
            return False
        
        self.log_operation("Automated rotation cycle completed successfully")
        return True
    
    def run_continuous(self, interval_minutes=30):
        """Run continuous rotation every N minutes"""
        self.log_operation(f"Starting continuous automated rotation every {interval_minutes} minutes")
        
        while True:
            try:
                success = self.perform_rotation_cycle()
                if success:
                    self.log_operation(f"Rotation cycle successful, next rotation in {interval_minutes} minutes")
                else:
                    self.log_operation("Rotation cycle failed, will retry in next cycle", 'error')
                
                # Wait for next cycle
                time.sleep(interval_minutes * 60)
                
            except KeyboardInterrupt:
                self.log_operation("Automated rotation stopped by user")
                break
            except Exception as e:
                self.log_operation(f"Unexpected error in rotation cycle: {str(e)}", 'error')
                time.sleep(60)  # Wait 1 minute before retrying
    
    def run_single_cycle(self):
        """Run a single rotation cycle"""
        return self.perform_rotation_cycle()

def main():
    rotator = AutoHoneypotRotator()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'single':
            print("Running single rotation cycle...")
            success = rotator.run_single_cycle()
            sys.exit(0 if success else 1)
        elif sys.argv[1] == 'continuous':
            interval = 30  # Default 30 minutes
            if len(sys.argv) > 2:
                try:
                    interval = int(sys.argv[2])
                except ValueError:
                    print("Invalid interval, using default 30 minutes")
            rotator.run_continuous(interval)
        else:
            print("Usage: python auto_honeypot_rotator.py [single|continuous [interval_minutes]]")
            print("  single: Run one rotation cycle")
            print("  continuous [interval]: Run continuous rotation (default 30 minutes)")
    else:
        print("Running single rotation cycle...")
        success = rotator.run_single_cycle()
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 