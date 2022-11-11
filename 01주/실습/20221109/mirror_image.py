# mirror_image.py
# mantis.jpg => mantis_mirrored.jpg

from PIL import Image

image = Image.open("images/mantis.jpg")
# mirror_image = image.transpose(Image.FLIP_LEFT_RIGHT)
# mirror_image.save("images/mantis_mirrored.jpg")

flip_image = image.transpose(Image.FLIP_TOP_BOTTOM)
flip_image.save("images/mantis_flipped.jpg")
