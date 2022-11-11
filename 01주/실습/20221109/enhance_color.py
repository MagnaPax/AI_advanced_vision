# enhance_color.py

from PIL import Image
from PIL import ImageEnhance

image = Image.open("images/goldenrod_soldier_beetle.jpg")
enhancer = ImageEnhance.Color(image)
new_image = enhancer.enhance(2.5)
new_image.save("images/beetle_color_enhanced.jpg")