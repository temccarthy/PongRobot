import matplotlib.pyplot as plt

from skimage import data, color, img_as_ubyte
from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter

import cv2

image_rgb_big=cv2.imread("Pong1.JPG",1)
image_rgb=cv2.resize(image_rgb_big, (0,0), fx=.25, fy=.25)

gray = color.rgb2gray(image_rgb)

cv2.imshow("gray",gray)
#--- First obtain the threshold using the greyscale image ---
ret,th = cv2.threshold(gray,127,255,0)

#--- Find all the contours in the binary image ---
_, contours,hierarchy = cv2.findContours(th,2,1)
cnt = contours
big_contour = []
max = 0
for i in cnt:
    area = cv2.contourArea(i) #--- find the contour having biggest area ---
    if(area > max):
        max = area
        big_contour = i 

final = cv2.drawContours(image_rgb, big_contour, -1, (0,255,0), 3)
cv2.imshow('final', final)
