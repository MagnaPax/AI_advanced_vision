# contour_image.py
# contour 필터 적용 후 flowers_contour.jpg 로 저장

from PIL import Image
from PIL import ImageFilter

image = Image.open("images/flowers_dallas.jpg")
filtered_image = image.filter(ImageFilter.CONTOUR)
filtered_image.save("images/flowers_contour.jpg")