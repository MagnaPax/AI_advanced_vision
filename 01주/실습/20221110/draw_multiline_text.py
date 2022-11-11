# draw_multiline_text.py

from PIL import Image, ImageDraw, ImageFont

image = Image.open("images/pilot_knob.jpg")
draw = ImageDraw.Draw(image)

myText = """멋있는 풍경입니다!
         이 곳에 한번 가보고 싶습니다!
   어디일까요?
"""

font = ImageFont.truetype("fonts/NanumSquareNeo-bRg.ttf", size = 150)
# draw.text( (10, 25), "멋있는 풍경입니다!\n이 곳에 한번 가보고 싶습니다!\n어디일까요?", font= font, fill = "red")
draw.text( (10, 25), myText, font= font, fill = "red")

image.save("images/multiline_text.jpg")
