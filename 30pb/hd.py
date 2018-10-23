#!/usr/bin/env python

from PIL import Image

# Opens an image
tile = Image.open("hd.jpg")

# The width and height of the background tile
tile_w, tile_h = tile.size

# desired width of final size
w = 10000

# 30 PB = 30000 TB = 15000 2 TB Drives 
# assuming a square layout how many in each row/column?
n = int(15000**(0.5))

# figure out the width of the resized tile
new_w = int(w/n)
new_h = int(new_w * (tile_h / tile_w))

# resize our image so it can tile
tile.thumbnail((new_w, new_h))

# create new image
new_im = Image.new('RGB', (w, new_h * n))

# The width and height of the new image
w, h = new_im.size

for i in range(0, w, new_w):
    for j in range(0, h, new_h):
        new_im.paste(tile, (i, j))

new_im.save('hds.jpg')
