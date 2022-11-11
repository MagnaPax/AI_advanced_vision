# thumbnail_maker.py

from PIL import Image

image = Image.open("images/flowers.jpg")
image.thumbnail( (128, 128) )
image.save("images/flowers.thumbnail", format="JPEG") 