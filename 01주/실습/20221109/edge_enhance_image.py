# edge_enhance_image.py

from PIL import Image
from PIL import ImageFilter

image = Image.open("images/cactus.jpg")
# filtered_image = image.filter(ImageFilter.EDGE_ENHANCE)
filtered_image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
filtered_image.save("images/cactus_edge_more.jpg")