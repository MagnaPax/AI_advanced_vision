# apply_posterize.py
# 아래 알고리즘 적용
# https://en.wikipedia.org/wiki/Posterization

from PIL import Image, ImageOps

image = Image.open("images2/jellyfish.jpg")
converted_image = ImageOps.posterize(image, bits=2)  # 1 ~ 8
converted_image.save("images2/jelly_posterize.jpg")
