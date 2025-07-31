#!/usr/bin/env python3
from PIL import Image
import os

def compress_images():
    img_dir = 'img'
    for filename in os.listdir(img_dir):
        if filename.endswith('.png'):
            filepath = os.path.join(img_dir, filename)
            print(f"Compressing {filename}...")
            
            # Open and resize image
            with Image.open(filepath) as img:
                # Resize to 800x600 while maintaining aspect ratio
                img.thumbnail((800, 600), Image.LANCZOS)
                
                # Save with compression
                img.save(filepath, 'PNG', optimize=True, compress_level=9)
            
            # Get file size
            size = os.path.getsize(filepath)
            print(f"  {filename}: {size/1024:.1f} KB")

if __name__ == "__main__":
    compress_images() 