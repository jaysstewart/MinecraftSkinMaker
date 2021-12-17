from collections import deque
from PIL import Image
from Skin import Skin


def setDefaultLayers(q):
    s = Skin
    q.clear()
    q.append(s.get_body)
    q.append(s.get_head)
    q.append(s.get_arms)
    q.append(s.get_legs)
    return q


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

def recompileImage(q):
    img1 = q[0]
    for i in range(len(q) - 1):
        if not i == len(q):
            img2 = q[i + 1]
            img1.paste(img2, (0, 0), img2)
        else:
            break
    img1.save("skin.png")
