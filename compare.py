import math

def dist(img1, img2):
    ret = 0
    for i in range(len(img1)):
        ret = ret + (float(img1[i])-float(img2[i]))*(float(img1[i])-float(img2[i]))
    ret = math.sqrt(ret)
    return ret

def cosine(img1, img2) :
    dot = 0
    for i in range(len(img1)):
        dot = dot + (float(img1[i]) * float(img2[i]))
    panjangv = 0
    panjangw = 0
    for i in range(len(img1)):
        panjangv = float(img1[i]) * float(img1[i])
        panjangw = float(img2[i]) * float(img2[i])
    panjangv = math.sqrt(panjangv)
    panjangw = math.sqrt(panjangw)
    ret = dot / (panjangv * panjangw)
    return ret
