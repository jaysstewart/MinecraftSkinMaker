from collections import deque
from PIL import Image


# move layer up an element in queue
def moveLayerUp(q, layer):
    i = q.index(layer) + 1
    q.remove(layer)
    q.insert(i, layer)


# move layer down an element in queue
def moveLayerDown(q, layer):
    i = q.index(layer) - 1
    q.remove(layer)
    q.insert(i, layer)


# compile image skin, 1st queue element = bottom layer
def recompileImage(self, q):
    for i in q:
        img1 = q[i]
        img2 = q[i+1]
        img1.paste(img2, (0, 0), img2)
    img1.save("skin.py")
