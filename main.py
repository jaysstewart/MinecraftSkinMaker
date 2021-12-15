# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque
from PIL import Image
import glob

import Skin
import actions

image_list = []
q = deque()
for filename in glob.glob("skintemplatetests/*.png"):
    im = Image.open(filename)
    image_list.append(im)
    q.append(im)
    #q.

#im1 = image_list[0]
#im2 = image_list[1]
#im3 = image_list[2]
#im4 = image_list[3]
#im1.paste(im2, (0,0), im2)
#im1.paste(im3, (0,0), im3)
#im1.paste(im4, (0,0), im4)
#im1.save("skin.png")
#im1.show()
actions.recompileImage(q)
#o = Skin.Skin()
#print(o.get_head())
#o.set_head("2")
#print(o.get_head())

