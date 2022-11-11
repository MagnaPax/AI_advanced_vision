# draw_text_default_font.py

from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (200, 200), "green")

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text( (10, 10), "Hello!!!", font= font)
draw.text( (10, 25), "Pillow!!!", font = font)

image.save("images/text.jpg")
