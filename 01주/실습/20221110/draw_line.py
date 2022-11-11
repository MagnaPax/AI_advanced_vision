# draw_line.py

from PIL import Image, ImageDraw

image = Image.open("images/madison_county_bridge_2.jpg")
draw = ImageDraw.Draw(image)
draw.line( (100, 100) + (300, 300), width = 5, fill = "red")
image.save("images/lines.jpg")