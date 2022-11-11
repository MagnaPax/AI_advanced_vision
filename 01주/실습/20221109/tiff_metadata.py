#  tiff_metadata.py

from PIL import Image
from PIL.TiffTags import TAGS

image = Image.open("images/reportlab_cover.tiff")

metadata = {}
for tag in image.tag.items():
    metadata[TAGS.get(tag[0])] = tag[1]

# print(metadata.keys())
print(metadata["Compression"])