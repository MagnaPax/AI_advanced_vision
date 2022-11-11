# apply_invert.py
# ImageChops.invert()
# 사진 필름 색깔 나오듯 색깔 반전

from PIL import Image, ImageOps, ImageChops

image = Image.open("images2/ducklings.jpg")
# converted_image = ImageOps.invert(image)
# converted_image.save("images2/ducklings_inverted.jpg")

converted_image = ImageChops.invert(image)
converted_image.save("images2/ducklings_inverted2.jpg")
