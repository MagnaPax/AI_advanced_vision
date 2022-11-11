# apply_solarize.py
# 모든 pixel 값을 threshold를 넘는 값은 invert 한다.

from PIL import Image, ImageOps

image = Image.open("images2/jellyfish.jpg")
converted_image = ImageOps.solarize(image, threshold=250)
converted_image.save("images2/jelly_solarize.jpg")
