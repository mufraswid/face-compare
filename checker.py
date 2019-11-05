import os
from extract import *
from compare import *

def load():
    # Only ran once, when opening the app
    global features
    features = []
    global names
    names = []
    feature_file = 'features.dmp'
    name_file = 'names.dmp'

    f = open(feature_file, 'r')
    for line in f.readlines():
        if (line[-1:] == '\n'):
            line = line[:-1]
        features.append(line.split(' '))

    g = open(name_file, 'r')
    for name in g.readlines():
        name = name[:-1]
        names.append(name)

def compareImage(img_path, mode, n):
    # called every time we want to find similar images
    # img_path: path to the image that we want to compare
    # mode: 0 - euclidean, 1 - cosine
    # n: how many similar images we want to display
    
    img = extract_features(img_path)

    if (mode == 0):
        result = []
        for i in range(len(features)):
            x = dist(img, features[i])
            result.append((x, i))
        result.sort()
        
        result = result[:n]
        for i in range(len(result)):
            # uncomment the line below to debug the function
            # print(result[i][0])
            result[i] = names[result[i][1]]
        return result

    elif (mode == 1):
        result = []
        for i in range(len(features)):
            x = cosine(img, features[i])
            result.append((x, i))
        result.sort()
        result = result[::-1]

        result = result[:n]
        for i in range(len(result)):
            # uncomment the line below to debug the function
            # print(result[i][0])
            result[i] = names[result[i][1]]
        return result
