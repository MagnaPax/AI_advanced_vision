# find_edges_image.py

from PIL import Image
from PIL import ImageFilter

image = Image.open("images/buffalo.jpg")
filtered_image = image.filter(ImageFilter.FIND_EDGES)
filtered_image.save("images/buffalo_edges.jpg")