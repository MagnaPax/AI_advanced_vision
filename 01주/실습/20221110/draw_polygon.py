# draw_polygon.py

from PIL import Image, ImageDraw

points = [ (100, 100), (200, 50), (125, 25) ]

image = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(image)

draw.polygon( points, fill = "green")
draw.polygon( (100, 150, 250, 300), outline = "blue")

image.save("images/polygons.jpg")