# emboss_image.py
# hummingbird.jpg => hummingbird_emboss.jpg

from PIL import Image
from PIL import ImageFilter

image = Image.open("images/hummingbird.jpg")
filtered_image = image.filter(ImageFilter.EMBOSS)
filtered_image.save("images/hummingbird_emboss.jpg")