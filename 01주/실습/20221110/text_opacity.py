# text_opacity.py

from PIL import Image, ImageDraw, ImageFont

base_image = Image.open("images/pilot_knob.jpg").convert("RGBA")

txt_img = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
font = ImageFont.truetype("fonts/NanumSquareNeo-bRg.ttf", size = 150)
draw = ImageDraw.Draw(txt_img)

myText = """멋있는 풍경입니다!"""
width, height = base_image.size
font_width, font_height = font.getsize(myText)

new_width = (width - font_width) / 2
new_height = (height - font_height) / 2
draw.text( (new_width, new_height), myText, font= font, fill = (255, 0, 0, 80))

composite = Image.alpha_composite(base_image, txt_img)
composite.save("images/pilot_knob_opacity.png")
