# WARNING DO NOT RUN
# This program will only be ran once, to create the features.dmp and names.dmp

from extract import *
    
def run():
    images_path = '../SplitFaceCompare/train'
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    
    batch_extractor(images_path)

run()