# draw_multiple_truetype.py

from PIL import Image, ImageDraw, ImageFont

image = Image.open("images/pilot_knob.jpg")
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("fonts/NanumSquareNeo-bRg.ttf", size = 50)
draw.text( (10, 25), "멋있는 풍경입니다!", font= font)

font = ImageFont.truetype("fonts/DNFBitBitTTF.ttf", size = 50)
draw.text( (10, 100), "멋있는 풍경입니다!", font= font)

image.save("images/truetype_fonts.jpg")
