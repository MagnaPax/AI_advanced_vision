# apply_crop.py
# 외곽을 기준으로 얼마나 잘라내나

from PIL import Image, ImageOps

image = Image.open("images2/flower_border.jpg")
converted_image = ImageOps.crop(image, border=250)
converted_image.save("images2/flower_no_border.jpg")
