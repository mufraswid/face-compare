import cv2
import numpy as np
import math
import os
import random as rnd
import matplotlib.pyplot as plt
import cPickle as pickle
# import _pickle as pickle
from scipy import *
import imageio

def show_img(path):
    # Show image
    img = imageio.imread(path, pilmode="RGB")
    plt.imshow(img)
    plt.show()

def extract_features(image_path, vector_size=32):
    # Feature extractor
    image = imageio.imread(image_path, pilmode="RGB")
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create(threshold=0.0001)
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
        print ('Error: ', e)
        return None

    return dsc


def batch_extractor(images_path, dump_features="features.dmp", dump_names="names.dmp"):
    # Extract the train folder into features.dmp (the feature vector) and names.dmp (the image paths)
    folders = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    f = open(dump_features, "w").close()
    f = open(dump_features, "w")
    g = open(dump_names, "w").close()
    g = open(dump_names, "w")
    result = []
    names = []
    for i in range(100): # number of people		
        files = [os.path.join(folders[i], p) for p in sorted(os.listdir(folders[i]))]
        print (i)
        for j in range(len(files)):
            result.append(extract_features(files[j]))
            g.write(str(files[j]))
            g.write("\n")

    for i in result:
        for j in i:
            f.write(str(j))
            f.write(" ")
        f.write("\n")

    f.close()
    g.close()
    