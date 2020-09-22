#!/usr/bin/env python3
from PIL import Image
import os

for file in os.listdir("./supplier-data/images"):
    if file.endswith("tiff"):
        im = Image.open("./supplier-data/images/" + file)
        im = im.resize((600,400), Image.ANTIALIAS)
        name = file[:3]
        rgb_im = im.convert('RGB')
        rgb_im.save("./supplier-data/images/" + name + ".jpeg")