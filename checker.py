import os
from extract import *
from compare import *

features = []
names = []

def load():
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
    img = extract_features(img_path)

    if (mode == 0):
        result = []
        for i in range(len(features)):
            x = dist(img, features[i])
            result.append((x, i))
        result.sort()
        
        result = result[:n]
        for i in range(len(result)):
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
            result[i] = names[result[i][1]]
        return result

# load()
# ans = compareImage(1, 4)
# print(ans)
# ans = compareImage(0, 4)
<<<<<<< HEAD
# print(ans)
=======
# print(ans)
>>>>>>> 5668df25fb12989640e091a529b78280be1839d8
