import numpy as np
from scipy.ndimage import imread
from scipy.misc import imsave

jpg = imread("panda.jpg")
idx = np.random.uniform(size=jpg.shape) < 0.001
jpg[idx] += np.random.uniform(-2,2, size=idx.sum()).astype(np.uint8)
jpg[jpg<0] = 0
jpg[jpg>255] = 255

imsave("panda_new.jpg", jpg)
