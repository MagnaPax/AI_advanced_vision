# apply_padding.py

from PIL import Image, ImageOps

image = Image.open("images2/flowers.jpg")
converted_image = ImageOps.pad(image, size = (1200, 600), color = "green")
converted_image.save("images2/flowers_padded.jpg")