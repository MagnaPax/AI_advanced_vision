# blur_image.py
# filter = effect 
# filter = image transformation이나 image transform의 한 종류
# image transform : 입력으로 이미지를 받고, 조정된 이미지를 출력으로 내보내는 함수, 기능
# filter는 이미지의 색을 변경, 선명도를 조정 등등
# pillow에서 지원하는 대표적인 필터
# BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE

from PIL import Image
from PIL import ImageFilter

image = Image.open("images/butterfly.jpg")
filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save("images/butterfly_blurred.jpg")
