# apply_equalize.py
# 색깔 히스토그램을 평균화(동등하게)

from PIL import Image, ImageOps

image = Image.open("images2/skyline.png")
converted_image = ImageOps.equalize(image)
converted_image.save("images2/skyline_equalized.png")
