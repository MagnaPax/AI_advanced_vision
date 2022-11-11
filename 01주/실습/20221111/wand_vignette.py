from wand.image import Image

image = Image(filename="images2/ducklings.jpg")
image.vignette(x=120, y=120)
image.save(filename="images2/vignette.jpg")
