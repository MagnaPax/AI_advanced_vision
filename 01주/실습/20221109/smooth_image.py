# smooth_image.py

from PIL import Image
from PIL import ImageFilter

image = Image.open("images/spider.jpg")
# filtered_image = image.filter(ImageFilter.SMOOTH)
filtered_image = image.filter(ImageFilter.SMOOTH_MORE)
filtered_image.save("images/spider_smooth_more.jpg")