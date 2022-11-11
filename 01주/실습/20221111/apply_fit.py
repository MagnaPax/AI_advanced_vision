# apply_fit.py
# fit = size + crop

from PIL import Image, ImageOps

image = Image.open("images2/flowers.jpg")
converted_image = ImageOps.fit(image, size=(
    200, 200), centering=(1.0, 0.0))  # centering - 기준점을 어디로 잡느냐
converted_image.save("images2/flowers_fitted.jpg")
