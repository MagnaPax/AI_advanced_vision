# draw_rectangle.py

from PIL import Image, ImageDraw

image = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(image)

draw.rectangle( (25, 50, 175, 200), fill = "green")
draw.rectangle( (100, 150, 250, 300), width = 5, outline = "blue")

image.save("images/rectangle.jpg")