# draw_ellipse.py

from PIL import Image, ImageDraw

image = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(image)

draw.ellipse( (25, 50, 50, 100), fill = "green")
draw.ellipse( (100, 150, 250, 300), fill = "yellow", width = 5, outline = "blue")

image.save("images/ellipse.jpg")