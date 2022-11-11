from PIL import Image

# image = Image.open("./images/cape_thick_knee.jpg")
# colors = image.getcolors()  # default로 256개 색상만 확인이 가능 / 그것을 넘는 색을 가진 이미지의 경우 None
# print(colors)
# print(len(colors))

image2 = Image.open("./images/butterfly.jpg")
colors2 = image2.getcolors(maxcolors=2797568)
print(colors2)
print(len(colors2))
