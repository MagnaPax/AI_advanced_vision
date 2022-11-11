# resize_image.py
# pilot_knob.jpg => pilot_knob_small.jpg

from PIL import Image

image = Image.open("images/pilot_knob.jpg")
width, height = image.size
print(f"원본 이미지의 크기 : {width} {height}")

resized_image = image.resize( (800, 400) )
width, height = resized_image.size
print(f"조정 이미지의 크기 : {width} {height}")

resized_image.save("images/pilot_knob_small.jpg")