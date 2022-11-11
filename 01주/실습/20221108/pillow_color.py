
# RGB : 빨,초,파
# RGBA: 빨,초,파,Alpha(투명도)
# HSL : Hue-Saturation-Lightness
# HSV : Hue-Saturation-Value


from PIL import ImageColor

print(ImageColor.getcolor("#ff0000", "RGBA"))
print(ImageColor.getcolor("red", "RGBA"))
print(ImageColor.getrgb("hsv(0, 100%, 100%)"))
print(ImageColor.colormap)
print(len(ImageColor.colormap))
