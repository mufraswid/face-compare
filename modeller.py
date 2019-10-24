from extract import *
    
def run():
    images_path = '../FaceCompare/PINS'
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    
    batch_extractor(images_path)

run()