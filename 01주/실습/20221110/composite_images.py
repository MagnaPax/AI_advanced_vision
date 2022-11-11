# composite_images.py

from PIL import Image

image1 = Image.open("images/pilot_knob.jpg")
image2 = Image.open("images/grasshopper.jpg")

mask = Image.new("L", image1.size, 100)
composited_images = Image.composite(image1, image2, mask)

composited_images.save("images/composited.jpg")