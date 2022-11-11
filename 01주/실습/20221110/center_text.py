# center_text.py

from PIL import Image, ImageDraw, ImageFont

image = Image.open("images/pilot_knob.jpg")
draw = ImageDraw.Draw(image)

myText = """멋있는 풍경입니다!"""

width, height = image.size
font = ImageFont.truetype("fonts/NanumSquareNeo-bRg.ttf", size = 150)

font_width, font_height = font.getsize(myText)

new_width = (width - font_width) / 2
new_height = (height - font_height) / 2

draw.text( (new_width, new_height), myText, font= font, fill = "red")

image.save("images/centered_text.jpg")
