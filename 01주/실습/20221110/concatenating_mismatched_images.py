# concatenating_mismatched_images.py

from PIL import Image

image_one = Image.open("images/hummingbird.jpg")
image_two = Image.open("images/silver_falls2.jpg")

# height = image_one.height + image_two.height
# width = min(image_one.width, image_two.width)
# new_image = Image.new("RGB",  (width, height) )
# new_image.paste(image_one, (0, 0))
# new_image.paste(image_two, (0, image_one.height))
# new_image.save("images/v_combined.jpg")

height = min(image_one.height, image_two.height)
width = image_one.width + image_two.width
new_image = Image.new("RGB",  (width, height) )
new_image.paste(image_one, (0, 0))
new_image.paste(image_two, (image_one.width, 0))
new_image.save("images/h_combined.jpg")