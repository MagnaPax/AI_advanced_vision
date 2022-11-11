# apply_expand.py

from PIL import Image, ImageOps

image = Image.open("images2/flowers.jpg")
converted_image = ImageOps.expand(image, border = 25, fill = "yellow")
converted_image.save("images2/flower_border.jpg")