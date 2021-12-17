from collections import deque
from PIL import Image
from Skin import Skin


# move layer up an element in queue
def moveLayerUp(q, layerIdx):
    i = layerIdx + 1
    img = q[layerIdx]
    del q[layerIdx]
    q.insert(i, layerIdx)


# move layer down an element in queue
def moveLayerDown(q, layerIdx):
    i = layerIdx - 1
    img = q[layerIdx]
    del q[layerIdx]
    q.insert(i, img)


# compile image skin, 1st queue element = bottom layer

def recompileImage(q):
    img1 = q[0]
    for i in range(len(q) - 1):
        if not i == len(q):
            img2 = q[i + 1]
            img1.paste(img2, (0, 0), img2)
        else:
            break
    img1.save("skin.png")
