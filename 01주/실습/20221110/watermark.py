# watermark.py

from PIL import Image

base_image = Image.open("images/hummingbird.jpg")
watermark_image = Image.open("images/logo.png")

base_image.paste(watermark_image, (0, 0))
base_image.save("images/hummingbird_watermarked.jpg")