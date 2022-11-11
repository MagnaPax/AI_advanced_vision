# apply_flip.py => top to bottom
# 좌우반전

from PIL import Image, ImageOps

image = Image.open("images2/ducklings.jpg")
converted_image = ImageOps.mirror(image)
converted_image.save("images2/ducklings_mirrored.jpg")
