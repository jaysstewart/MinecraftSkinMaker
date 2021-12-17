# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque
from PIL import Image
import glob

from Skin import Skin
import actions

q = deque()
for filename in glob.glob("skintemplatetests/*.png"):
    im = Image.open(filename)
    q.append(im)

skin = Skin()
actions.moveLayerUp(q, 2)

actions.recompileImage(q)
#s.head = q[1]
#s.legs = q[2]
#s.arms = q[3]
#q.reverse()


