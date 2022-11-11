# apply_flip.py => top to bottom
# transpose() LEFT_RIGHT / TOP_BOTTOM

from PIL import Image, ImageOps

image = Image.open("images2/ducklings.jpg")
converted_image = ImageOps.flip(image)
converted_image.save("images2/ducklings_flipped.jpg")