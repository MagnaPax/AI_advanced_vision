
# convert argument
# L
# 1
# P
# RGB
# CYMK

from PIL import Image


# 내가 만든 팔레트
whitish = (255, 240, 192)
palette = []
r, g, b = whitish
for i in range(255):
    new_red = r * i // 255
    new_green = g * i // 255
    new_blue = b * i // 255
    palette.extend((new_red, new_green, new_blue))

color_image = Image.open("./images/monarch_caterpillar.jpg")

image = color_image.convert(mode="L")
image.putpalette(palette)  # 내가 만든 팔레트 적용
image.show()

sepia_image = image.convert("RGB")  # 이렇게 안 바꾸면 저장할 때 에러남
sepia_image.save("./images/sepia_caterpillar.jpg")
