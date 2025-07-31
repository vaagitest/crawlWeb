#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(filename, text, size=(400, 300), bg_color=(100, 150, 200), text_color=(255, 255, 255)):
    # Create image
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position (center)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save with compression
    img.save(f'img/{filename}', 'JPEG', quality=85, optimize=True)
    print(f"Created {filename}")

def main():
    # Create placeholder images
    placeholders = [
        ("image-1.jpg", "AI Breakthrough", (100, 150, 200)),
        ("image-2.jpg", "Quantum Computing", (150, 100, 200)),
        ("image-3.jpg", "Web Development", (200, 100, 150)),
        ("image-4.jpg", "Cybersecurity", (200, 150, 100)),
        ("image-5.jpg", "Data Science", (150, 200, 100))
    ]
    
    for filename, text, color in placeholders:
        create_placeholder_image(filename, text, bg_color=color)

if __name__ == "__main__":
    main() 