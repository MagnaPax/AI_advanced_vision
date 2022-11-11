# RGB : 빨,초,파
# RGBA: 빨,초,파,Alpha(투명도)


from PIL import ImageColor

for color in ImageColor.colormap:
    print(f"{color} = {ImageColor.getcolor(color, 'RGBA')}")
