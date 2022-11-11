# text_alignment.py

from PIL import Image, ImageDraw, ImageFont

image = Image.open("images/pilot_knob.jpg")
draw = ImageDraw.Draw(image)

myText = """멋있는 풍경입니다!
이 곳에 한번 가보고 싶습니다!
어디일까요?
"""

font = ImageFont.truetype("fonts/NanumSquareNeo-bRg.ttf", size=50)
draw.text((10, 25), myText, font=font, fill="red", align="left")
draw.text((10, 225), myText, font=font, fill="red", align="center")
draw.text((10, 425), myText, font=font, fill="red", align="right")


image.save("images/aligned_text.jpg")
