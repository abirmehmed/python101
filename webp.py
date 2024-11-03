from PIL import Image
import os

# Prompt the user to enter the WebP file name
webp_file = input("Enter the name of the WebP file (including the extension): ")

# Open the WebP image
webp_image = Image.open(webp_file)

# Convert the image to RGB mode
rgb_image = webp_image.convert('RGB')

# Create the JPEG file name by replacing the .webp extension with .jpg
jpeg_file = os.path.splitext(webp_file)[0] + '.jpg'

# Save the image as a JPEG file
rgb_image.save(jpeg_file, 'jpeg')

print(f"Conversion successful! The JPEG file is saved as {jpeg_file}")
