
# 모든 형식 목록을 보고싶을 때 - $ python -m PIL

from PIL import Image

image = Image.open("./images/flowers.jpg")
# image.show("꽃")
# print(dir(image))
# print(image.size)
print(image.size[0], image.size[1])

width, height = image.size
print(width, height)

print(image.filename)
print(image.format)
print(image.format_description)

image.save("./images/flowers.png")
