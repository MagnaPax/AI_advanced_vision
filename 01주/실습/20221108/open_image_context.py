# open_image_context.py

from PIL import Image

with Image.open("images/flowers.jpg") as image:
    image.show("flowers")