# apply_autocontrast.py
# autocontrast의 목적 : 이미지의 contrast을 최대화(maximize)하거나 정규화 (normalize)

from PIL import Image, ImageOps

image = Image.open("images2/ducklings.jpg")
converted_image = ImageOps.autocontrast(image, cutoff=2, ignore=None)
converted_image.save("images2/autocontrast.jpg")