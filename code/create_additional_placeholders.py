#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(filename, text, size=(400, 300), bg_color=(100, 150, 200), text_color=(255, 255, 255)):
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    draw.text((x, y), text, fill=text_color, font=font)
    img.save(f'img/{filename}', 'JPEG', quality=85, optimize=True)
    print(f"Created {filename}")

def main():
    placeholders = [
        ("image-6.jpg", "Advanced ML", (102, 153, 255)),  # Blue for a-6hp
        ("image-7.jpg", "Emerging AI", (255, 102, 178))   # Pink for a-7sm
    ]
    for filename, text, color in placeholders:
        create_placeholder_image(filename, text, bg_color=color)

if __name__ == "__main__":
    main() 