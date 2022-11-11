from PIL import Image

# image = Image.open("images/blue_flowers.jpg")
# image.save("images/blue_flowers_compressed.jpg", quality = 95, optimize = True)

# image = Image.open("images/flowers.png")
# image.save("images/flowers_compressed.png", compress_level = 5) # 0 ~ 9 : 0 no comp

image = Image.open("images/blue_flowers.jpg")
image.save("images/blue_flowers_dpi.jpg", dpi=(72, 72))
