
# convert argument
# L
# 1
# P
# RGB
# CYMK

from PIL import Image

color_image = Image.open("./images/monarch_caterpillar.jpg")
gray_scale = color_image.convert(mode="L", dither=30)
gray_scale.show()
# gray_scale.save("./images/gray_caterpillar.jpg")
