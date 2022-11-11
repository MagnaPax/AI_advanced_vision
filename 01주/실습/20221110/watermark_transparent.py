# watermark_transparent.py

from PIL import Image

base_image = Image.open("images/hummingbird.jpg")
watermark_image = Image.open("images/logo.png")

width, height = base_image.size

transparent = Image.new("RGB", (width, height), (0, 0, 0, 0))
transparent.paste(base_image, (0, 0))
transparent.paste(watermark_image, (100, 200), mask=watermark_image)
transparent.save("images/hummingbird_watermarked2.jpg")
