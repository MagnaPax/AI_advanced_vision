# draw_text.py

from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (200, 200), "green")

draw = ImageDraw.Draw(image)
draw.text( (10, 10), "Hello!!!")
draw.text( (10, 25), "Pillow!!!")

image.save("images/text.jpg")
