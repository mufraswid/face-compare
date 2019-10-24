from extract import *

def show_img(path):
    img = imread(path, mode="RGB")
    plt.imshow(img)
    plt.show()
    
def run():
    images_path = '../algeontol/PINS'
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    
    batch_extractor(images_path)

run()