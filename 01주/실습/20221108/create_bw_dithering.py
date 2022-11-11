from PIL import Image

color_image = Image.open("images/monarch_caterpillar.jpg")
gray_scale = color_image.convert(mode = "1", dither=0)
gray_scale.show()
# gray_scale.save("images/dither_caterpillar.jpg")