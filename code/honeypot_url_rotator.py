#!/usr/bin/env python3
"""
Honeypot URL Rotator System
Changes URLs for honeypot pages every 5 minutes to detect crawlers
"""

import os
import time
import random
import string
import shutil
from datetime import datetime
import json

class HoneypotURLRotator:
    def __init__(self):
        self.honeypot_pages = ['a-6hp.html', 'a-7sm.html']
        self.url_history_file = 'logs/honeypot_url_history.json'
        self.current_urls = {}
        self.load_current_urls()
    
    def generate_random_filename(self, original_name):
        """Generate a random filename for the honeypot pages with original prefix"""
        # Extract prefix from original name (e.g., 'a-6hp' from 'a-6hp.html')
        prefix = original_name.replace('.html', '')
        
        # Generate random string
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"{prefix}-{random_suffix}.html"
    
    def load_current_urls(self):
        """Load current URL mappings from history file"""
        if os.path.exists(self.url_history_file):
            try:
                with open(self.url_history_file, 'r') as f:
                    data = json.load(f)
                    self.current_urls = data.get('current_urls', {})
            except:
                self.current_urls = {}
        else:
            self.current_urls = {}
    
    def save_url_history(self):
        """Save current URL mappings to history file"""
        os.makedirs('logs', exist_ok=True)
        data = {
            'current_urls': self.current_urls,
            'last_updated': datetime.now().isoformat()
        }
        with open(self.url_history_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def rotate_urls(self):
        """Rotate URLs for honeypot pages"""
        print(f"[{datetime.now()}] Starting URL rotation for honeypot pages...")
        
        # Get current filenames from mappings or use original names
        current_files = {}
        for original_page in self.honeypot_pages:
            current_file = self.current_urls.get(original_page, original_page)
            if os.path.exists(current_file):
                current_files[original_page] = current_file
            else:
                print(f"Warning: {current_file} does not exist, skipping...")
                continue
        
        for original_page, current_file in current_files.items():
            # Generate new random filename with original prefix
            new_filename = self.generate_random_filename(original_page)
            
            # Ensure new filename doesn't conflict with existing files
            while os.path.exists(new_filename):
                new_filename = self.generate_random_filename(original_page)
            
            # Move the file to new name
            try:
                shutil.move(current_file, new_filename)
                self.current_urls[original_page] = new_filename
                print(f"Rotated {current_file} -> {new_filename}")
                
                # Log the rotation
                self.log_rotation(current_file, new_filename)
                
            except Exception as e:
                print(f"Error rotating {current_file}: {e}")
        
        # Save updated mappings
        self.save_url_history()
        print(f"[{datetime.now()}] URL rotation completed.")
    
    def log_rotation(self, old_name, new_name):
        """Log URL rotation for monitoring"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'old_url': old_name,
            'new_url': new_name,
            'action': 'url_rotation'
        }
        
        log_file = 'logs/honeypot_rotations.log'
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
    
    def get_current_urls(self):
        """Get current URL mappings"""
        return self.current_urls
    
    def run_continuous_rotation(self, interval_minutes=5):
        """Run continuous URL rotation every N minutes"""
        print(f"Starting continuous URL rotation every {interval_minutes} minutes...")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                self.rotate_urls()
                print(f"Next rotation in {interval_minutes} minutes...")
                time.sleep(interval_minutes * 60)
                
        except KeyboardInterrupt:
            print("\nStopping URL rotation...")
    
    def manual_rotation(self):
        """Perform a single manual rotation"""
        self.rotate_urls()

def main():
    rotator = HoneypotURLRotator()
    
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'manual':
            print("Performing manual URL rotation...")
            rotator.manual_rotation()
        elif sys.argv[1] == 'status':
            print("Current URL mappings:")
            for original, current in rotator.get_current_urls().items():
                print(f"  {original} -> {current}")
        else:
            print("Usage: python honeypot_url_rotator.py [manual|status]")
            print("  manual: Perform single rotation")
            print("  status: Show current URL mappings")
            print("  (no args): Run continuous rotation every 5 minutes")
    else:
        # Run continuous rotation
        rotator.run_continuous_rotation()

if __name__ == "__main__":
    main() 