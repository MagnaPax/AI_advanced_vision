# crop_image.py

from PIL import Image

image = Image.open("images/green_mantis.jpeg")
cropped_image = image.crop( (302,101,910, 574) )
cropped_image.save("images/cropped_mantis.jpg")