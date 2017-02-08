from vehicle_detector import *

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

import glob

import cv2

windFinder = WindowFinder()

image = mpimg.imread('./test_images/test6.jpg')

             
# If you extracted training
# data from .png images (scaled 0 to 1 by mpimg) and the
# image you are searching is a .jpg (scaled 0 to 255) use conversion below.
def pipeline(img):
    pass

## Good for test6.jpg
    hot_windows = windFinder.get_all_hot_windows(img, visualise=False)

    heatMapper = HeatMapper(img)

    heatMapper.add_heat(hot_windows)

    threshold = heatMapper.get_heatmap_max() * 0.4
    # heatMapper.apply_threshold(threshold=0)
    
    f = heatMapper.get_heatmap_and_result()

    return f


output_image_path = './output_images/'
test_images = glob.glob('test_images/*.jpg')

# fig = plt.figure()


for path in test_images:
    # Display images
    img = (mpimg.imread(path))
    fig = pipeline(img)
    savep = output_image_path + path.split('/')[1]
    plt.savefig(savep)

