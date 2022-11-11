# apply_colorize.py

from PIL import Image, ImageOps

image = Image.open("images2/gray_caterpillar.jpg")
converted_image = ImageOps.colorize(image, black="blue", white="white")
converted_image.save("images2/color_caterpillar.jpg")
