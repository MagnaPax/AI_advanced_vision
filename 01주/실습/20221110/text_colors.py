# text_colors.py

from PIL import Image, ImageDraw, ImageFont

image = Image.open("images/pilot_knob.jpg")
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("fonts/NanumSquareNeo-bRg.ttf", size = 150)
draw.text( (10, 25), "멋있는 풍경입니다!", font= font, fill = "red")

font = ImageFont.truetype("fonts/DNFBitBitTTF.ttf", size = 150)
draw.text( (10, 300), "멋있는 풍경입니다!", font= font, fill = "blue")

image.save("images/colored_text.jpg")
