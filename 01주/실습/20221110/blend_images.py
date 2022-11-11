# blend_images.py

from PIL import Image

image1 = Image.open("images/silver_falls.jpg")
image2 = Image.open("images/silver_falls2.jpg")

if image1.size != image2.size:
    print("ERROR: 이미지 크기가 다릅니다!")

blended_image = Image.blend(image1, image2, 0.8)
blended_image.save("images/blended.jpg")
