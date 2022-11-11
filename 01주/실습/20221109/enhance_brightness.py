# enhance_brightness.py

from PIL import Image
from PIL import ImageEnhance

image = Image.open("images/silver_falls.jpg")
enhancer = ImageEnhance.Brightness(image)
new_image = enhancer.enhance(1.3)
new_image.save("images/silver_falls_enhanced.jpg")