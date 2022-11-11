# draw_truetype.py

from PIL import Image, ImageDraw, ImageFont

image = Image.open("images/pilot_knob.jpg")
draw = ImageDraw.Draw(image)

y = 10
for font_size in range(12, 75, 10):
    font = ImageFont.truetype("fonts/NanumSquareNeo-bRg.ttf", size = font_size)
    draw.text( (10, y), f"멋진 폰트의 크기는 {font_size}입니다!", font= font)
    y += 35

image.save("images/truetype.jpg")
