import numpy as np
from PIL import Image  # ImageFilter, you can add if you need
image = Image.open('kunfu.jpg')
image = image.convert('RGB')
arrayView = np.array(image)
data = image.getdata()
newArrayEl = []


def white_color():
    colors = []
    for i in range(200, 256):
        item_c = (i, i, i)
        colors.append(item_c)
    return colors


def black_color():
    colors = []
    for i in range(0, 121):
        item_c = (i, i, i)
        colors.append(item_c)
    return colors


for item in data:
    if item in white_color():
        newArrayEl.append((0, 0, 0))
    elif item in black_color():
        newArrayEl.append((255, 255, 255))
    else:
        newArrayEl.append(item)

# converting a new array to a pic
image.putdata(newArrayEl)

# original = image.filter(ImageFilter.BLUR)
# original.save('kunfu1.jpg')
# original.show()

image.save("kunfu1.jpg")
image.show()
