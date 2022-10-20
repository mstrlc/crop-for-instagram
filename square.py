from PIL import Image
from os import path
import sys

# Cropped image dimensions
IMAGE_SIZE = 1080

def create_square_image():
    # Get image path from user
    # If Ctrl+C is pressed, exit
    try:
        image_path = input("Enter image path (drag and drop in the terminal): ")
    except KeyboardInterrupt:
        sys.exit(0)

    # If image path is drag and dropped onto the terminal,
    # the spaces will be escaped, replace them to spaces
    image_path = image_path.replace("\ ", " ")
    # Also, filename might end with space, remove it
    image_path = image_path.strip()

    # Create background and open image
    bg = Image.new("RGB", (IMAGE_SIZE, IMAGE_SIZE), "white")
    im = Image.open(image_path)

    # Resize original image to fit in the background completely
    im.thumbnail((IMAGE_SIZE, IMAGE_SIZE), Image.Resampling.LANCZOS)

    # aste onto the background
    bg.paste(im, ((IMAGE_SIZE - im.width) // 2, (IMAGE_SIZE - im.height) // 2))

    # Append _sq to the filename and save to the same directory
    new_image = path.splitext(image_path)[0] + "_sq" + path.splitext(image_path)[1]
    bg.save(new_image)

    print("Success! Ctrl-C to exit.")

while True:
    create_square_image()