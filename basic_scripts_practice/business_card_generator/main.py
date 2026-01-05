# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pillow",
# ]
# ///

# Uses the Pillow (PIL) library to create and manipulate images
from PIL import Image, ImageDraw, ImageFont
print("Business Card Generator")
print("-----------------------")
# Takes user input for name, title, email, and phone number
name = input("Enter your name: ")
title = input("Enter your title: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")

print("Generating business card...")
# Creates a business card image with a colored background
card = Image.new("RGB", (400, 240), color=(73, 109, 137))
draw = ImageDraw.Draw(card)

# Adds text with different fonts and sizes for visual hierarchy
font_name = ImageFont.truetype("/usr/share/fonts/truetype/dejavu//DejaVuSans.ttf", 24)
draw.text((20, 30), name, font=font_name, fill="white")

font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu//DejaVuSans.ttf", 16)
draw.text((20, 60), title, font=font_title, fill="white")

font_contact = ImageFont.truetype("/usr/share/fonts/truetype/dejavu//DejaVuSans.ttf", 12)
draw.text((20, 90), email, font=font_contact, fill="white")
draw.text((20, 110), phone, font=font_contact, fill="white")

# Saves the generated business card as a PNG image
card.save("business_card.png")
print("Business card saved as 'business_card.png'.")