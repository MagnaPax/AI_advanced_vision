# create_image.py

from PIL import Image
from PIL import ImageColor

image = Image.new("RGBA", (150, 150))

red = ImageColor.getcolor("red", "RGBA")
green = ImageColor.getcolor("green", "RGBA")
color = red

count = 0
for y in range(150):
    for x in range(150):
        if count == 5:
            color = red if red != color else green
            count = 0
        image.putpixel( (x, y), color )
        count += 1

image.save("images/lines.png")
