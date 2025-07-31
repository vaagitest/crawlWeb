#!/usr/bin/env python3
"""
Script to add Google Analytics tracking code to all HTML pages
"""

import os
import glob

# Google Analytics tracking code
GA_CODE = '''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-WVBPDESL96"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-WVBPDESL96');
    </script>'''

def add_google_analytics_to_file(filepath):
    """Add Google Analytics code to a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if Google Analytics is already present
        if 'G-WVBPDESL96' in content:
            print(f"Google Analytics already present in {filepath}")
            return False
        
        # Find the position after the first <head> tag and after the viewport meta tag
        head_start = content.find('<head>')
        if head_start == -1:
            print(f"No <head> tag found in {filepath}")
            return False
        
        # Find the position after the viewport meta tag
        viewport_pos = content.find('<meta name="viewport"')
        if viewport_pos == -1:
            print(f"No viewport meta tag found in {filepath}")
            return False
        
        # Find the end of the viewport meta tag
        viewport_end = content.find('>', viewport_pos) + 1
        
        # Insert Google Analytics code after the viewport meta tag
        new_content = content[:viewport_end] + '\n' + GA_CODE + content[viewport_end:]
        
        # Write the updated content back to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Added Google Analytics to {filepath}")
        return True
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Add Google Analytics to all HTML files"""
    # Get all HTML files in the current directory
    html_files = glob.glob('*.html')
    
    print(f"Found {len(html_files)} HTML files")
    
    updated_count = 0
    for html_file in html_files:
        if add_google_analytics_to_file(html_file):
            updated_count += 1
    
    print(f"\nUpdated {updated_count} files with Google Analytics tracking code")

if __name__ == "__main__":
    main() 