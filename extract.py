import cv2
import numpy as np
import math
import os
import random as rnd
import matplotlib.pyplot as plt
import cPickle as pickle
from scipy import *
from scipy.misc import imread

# Feature extractor
def extract_features(image_path, vector_size=32):
    image = imread(image_path, mode="L")
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print 'Error: ', e
        return None

    return dsc


def batch_extractor(images_path, dump_path="features.pck"):
    folders = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    f = open("features.pck", "w")
    num = []
    for i in range(5): # number of people
        files = [os.path.join(folders[i], p) for p in sorted(os.listdir(folders[i]))]
        result = []
        avgresult = []
        print i
        num.append(len(files) * 4 // 5)
        for j in range(len(files) * 4 // 5):
            name = files[j].split('/')[-1].lower()
            result.append(extract_features(files[j]))
        
        p = [0 for k in range(2048)]
        assert(len(result) == num[i])
        for j in range(len(result)):
            for k in range(2048):
                p[k] = p[k] + result[j][k]*result[j][k]
        for k in range(2048):
            p[k] = p[k] / num[i]
            p[k] = math.sqrt(p[k])
        for elmt in p:
            f.write(str(elmt))
            f.write(" ")
        f.write("\n")

    f.close()
        

    