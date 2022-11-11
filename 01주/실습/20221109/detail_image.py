# detail_image.py
# DETAIL 필터 적용 후 detailed_butterfly.jpg 로 저장

from PIL import Image
from PIL import ImageFilter

image = Image.open("images/butterfly.jpg")
filtered_image = image.filter(ImageFilter.DETAIL)
filtered_image.save("images/detailed_butterfly.jpg")