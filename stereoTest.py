import numpy as np
import cv2
from matplotlib import pyplot as plt

from RectangledWhiteArea import *




imgL = cv2.imread('rackL.JPG',1)
imgR = cv2.imread('rackR.JPG',1)

#crop_image(imgL)
#crop_image(imgR)

cropL=crop_image(imgL)[4]
cropR=crop_image(imgR)[4]


stereo = cv2.StereoBM_create(numDisparities=128, blockSize=15)
disparity = stereo.compute(cropL,cropR)
plt.imshow(disparity,'gray')
plt.show()
