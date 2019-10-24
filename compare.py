import math

def dist(img1, img2):
    ret = 0
    for i in range(len(img1)):
        ret = ret + (float(img1[i])-float(img2[i]))*(float(img1[i])-float(img2[i]))
    ret = math.sqrt(ret)
    return ret