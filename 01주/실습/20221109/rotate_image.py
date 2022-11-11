# rotate_image.py

from PIL import Image

image = Image.open("images/dragonfly.jpg")
rotated_image = image.rotate( 90 )
rotated_image.save("images/dragonfly_rotated.jpg")