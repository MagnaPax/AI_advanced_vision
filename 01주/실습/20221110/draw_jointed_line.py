# draw_jointed_line.py

from PIL import Image, ImageDraw

points = [ (100, 100), (150, 200), (200, 50), (400, 400) ]

image = Image.new("RGB", (400, 400), "red")
draw = ImageDraw.Draw(image)
draw.line(points, width = 15, fill="green", joint="curve")

image.save("images/jointed_lines.jpg")