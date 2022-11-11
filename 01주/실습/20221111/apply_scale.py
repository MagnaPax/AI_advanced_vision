# ImageOps.scale(image, 0.7) 07. = 70%로 줄이겠다


from PIL import Image, ImageOps

image = Image.open("images2/flowers.jpg")
converted_image = ImageOps.scale(image, 0.7)
converted_image.save("images2/flower_scaled.jpg")
