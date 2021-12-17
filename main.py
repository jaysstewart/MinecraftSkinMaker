# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque
from PIL import Image
import glob

from Skin import Skin
import actions

image_list = []
q = deque()
for filename in glob.glob("skintemplatetests/*.png"):
    im = Image.open(filename)
    image_list.append(im)
    q.append(im)

s = Skin
s.set_body = q[0]
print(s.get_body(s))
#s.head = q[1]
#s.legs = q[2]
#s.arms = q[3]
#q.reverse()

#actions.setDefaultLayers(q)
#print(q[0])
#actions.recompileImage(q)



#q.reverse()
#actions.setDefaultLayers(q)
#actions.recompileImage(q)
#o = Skin.Skin()
#print(o.get_head())
#o.set_head("2")
#print(o.get_head())

