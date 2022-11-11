# enhance_contrast.py

from PIL import Image
from PIL import ImageEnhance

image = Image.open("images/madison_county_bridge.jpg")
enhancer = ImageEnhance.Contrast(image)
new_image = enhancer.enhance(2.5)
new_image.save("images/madison_county_bridge_enhanced.jpg")