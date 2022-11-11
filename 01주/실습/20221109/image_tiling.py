# image_tiling.py

from PIL import Image

image = Image.open("images/hummingbird.jpg")
width, height = image.size

new_image = Image.new("RGB", (width, height))

cropped_image = image.crop( (125, 712, 642, 963) )
cropped_width, cropped_height = cropped_image.size

for left_pos in range(0, width, cropped_width):
    for top_pos in range(0, height, cropped_height):
        new_image.paste(cropped_image, (left_pos, top_pos))

new_image.save("images/hummingbird_tiled.jpg")