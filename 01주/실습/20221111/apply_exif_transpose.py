# apply_exif_transpose.py

from PIL import Image, ImageOps

image = Image.open("images2/snowman.jpg")
exif = image.getexif()
orientation = exif.get(0x0112)
print(f"Orientation = {orientation}")

converted_image = ImageOps.exif_transpose(image)
converted_image.save("images2/snowman_exif_transposed.jpg")
