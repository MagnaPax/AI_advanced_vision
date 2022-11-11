# gps_exif_getter.py

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

exif_table = {}
image = Image.open("images/jester.jpg")
info = image._getexif()

for tag, value in info.items():
    decoded = TAGS.get(tag, tag)
    exif_table[decoded] = value

gps_info = {}
for key in exif_table["GPSInfo"]:
    decode = GPSTAGS.get(key, key)
    gps_info[decode] = exif_table["GPSInfo"][key]

if gps_info:
    print(gps_info)
else:
    print("GPS 정보가 없습니다.")