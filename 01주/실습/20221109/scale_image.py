# scale_image.py

from PIL import Image
import sys

width = None
height = 500

image = Image.open("images/pilot_knob.jpg")
w, h = image.size
print(f"원본 이미지의 크기 : {width} {height}")

if width and height:
    max_size = (width, height)
elif width:
    max_size = (width, h)
elif height:
    max_size = (w, height)
else:
    sys.exit("높이든, 너비든 필요합니다.")

image.thumbnail(max_size, Image.ANTIALIAS)
image.save("images/pilot_knob_scaled.jpg")

scaled_image = Image.open("images/pilot_knob_scaled.jpg")
width, height = scaled_image.size
print(f"조정 이미지의 크기 : {width} {height}")
