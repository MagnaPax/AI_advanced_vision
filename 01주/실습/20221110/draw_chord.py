# draw_chord.py

from PIL import Image, ImageDraw

image = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(image)

draw.chord( (25, 50, 175, 200), start = 30, end =250, fill = "green")
draw.chord( (100, 150, 275, 300), start = 20, end =100, fill = "yellow", width = 5, outline = "blue")

image.save("images/chord.jpg")