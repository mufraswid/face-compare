import os
from extract import *
from compare import *

feature_file = 'features.dmp'
name_file = 'names.dmp'

features = []
f = open(feature_file, 'r')
for line in f.readlines():
    if (line[-1:] == '\n'):
        line = line[:-1]
    features.append(line.split(' '))

names = []
g = open(name_file, 'r')
for name in g.readlines():
    name = name[:-1]
    names.append(name)

img_file = '2.jpg'
img = extract_features(img_file)

p = int(input())

if (p == 0):
    result = []
    for i in range(len(features)):
        x = dist(img, features[i])
        result.append((x, i))
    result.sort()

    for i in range(5):
        print(result[i][1])
        print(names[result[i][1]])
elif (p == 1):
    result = []
    for i in range(len(features)):
        x = cosine(img, features[i])
        result.append((x, i))
    result.sort()

    for i in range(5):
        print(result[i][1])
        print(names[result[i][1]])