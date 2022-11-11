# draw_arc.py

from PIL import Image, ImageDraw

image = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(image)

draw.arc( (25, 50, 175, 200), start = 30, end =250, fill = "green")
draw.arc( (100, 150, 275, 300), start = 20, end =100, fill = "yellow", width = 5)

image.save("images/arc.jpg")