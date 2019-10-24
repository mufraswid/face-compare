import os
from extract import *
from compare import *

model_file = 'features.pck'

model = []

f = open(model_file, 'r')
for line in f.readlines():
    if (line[-1:] == '\n'):
        line = line[:-1]
    model.append(line.split(' '))

img_file = '2.jpg'
img = extract_features(img_file)

res = []
for i in range(len(model)):
    res.append((dist(img, model[i]), i + 1))

print(res)