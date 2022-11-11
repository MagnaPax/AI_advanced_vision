# exif_getter.py
# JPG에는 메타정보를 가지고 있다! Exchangeable Image File Format (Exif)
# pillow는 Tag Image File Format (TIFF)

from PIL import Image
from PIL.ExifTags import TAGS

exif_table = {}
image = Image.open("images/bridge.JPG")
info = image.getexif()

for tag, value in info.items():
    decoded = TAGS.get(tag, tag)
    exif_table[decoded] = value

print(exif_table)