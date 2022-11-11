# sharpen_image.py

from PIL import Image
from PIL import ImageFilter

image = Image.open("images/grasshopper.jpg")
filtered_image = image.filter(ImageFilter.SHARPEN)
filtered_image.save("images/grasshopper_sharpened.jpg")