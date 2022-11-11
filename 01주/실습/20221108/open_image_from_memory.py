# open_image_from_memory.py

import urllib.request
import io

from PIL import Image

URL = "https://i.picsum.photos/id/721/200/300.jpg?hmac=6g_vLTUju_TGWN7cMKTjZgzqps-JjmHIS0KSuFsgVyc"
f = urllib.request.urlopen(URL)
data = f.read()

with Image.open(io.BytesIO(data)) as image:
    image.show("Downloaded Image")