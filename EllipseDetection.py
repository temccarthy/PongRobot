import matplotlib.pyplot as plt

from skimage import data, color, img_as_ubyte
from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter

import cv2

from RectangledWhiteArea import *
from RedMaskTest import *

imgToProc=img10

x,y,w,h = crop_image(imgToProc)
print(x,y,w,h)

image_rgb_big=imgToProc

#image_rgb_uncropped=cv2.resize(image_rgb_big, (0,0), fx=.25, fy=.25)
image_rgb=image_rgb_big[y-int(.3*h):y+h,x-int(.08*w):x+w+int(.08*w)]



print("image found")

# Load picture, convert to grayscale and detect edges
#image_rgb = data.coffee()[0:220, 160:420]
image_gray = color.rgb2gray(image_rgb)
#image_gray = cv2.cvtColor(image_rgb,cv2.COLOR_BGR2GRAY)


edges = canny(image_gray, sigma=2.0,
              low_threshold=0.45, high_threshold=0.55)

edges_img = color.gray2rgb(img_as_ubyte(edges))
#edges_img_r=cv2.resize(edges_img, (0,0), fx=.25, fy=.25)

print("image greyed")

def showimgs():
    cv2.imshow("uncrop",image_rgb_big)
    cv2.imshow("crop",image_rgb)
    cv2.imshow("edge",edges_img)


def findEllipse(edges):
    # Perform a Hough Transform
    # The accuracy corresponds to the bin size of a major axis.
    # The value is chosen in order to get a single high accumulator.
    # The threshold eliminates low accumulators
    result = hough_ellipse(edges, accuracy=20, threshold=250,
                           min_size=10, max_size=200)
    result.sort(order='accumulator')
    print("ellipses found")

    # Estimated parameters for the ellipse
    best = list(result[-1])
    yc, xc, a, b = [int(round(x)) for x in best[1:5]]
    orientation = best[5]

    # Draw the ellipse on the original image
    cy, cx = ellipse_perimeter(yc, xc, a, b, orientation)
    image_rgb[cy, cx] = (0, 0, 255)
    # Draw the edge (white) and the resulting ellipse (red)
    edges = color.gray2rgb(img_as_ubyte(edges))
    edges[cy, cx] = (250, 0, 0)

    fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4),
                                    sharex=True, sharey=True)

    ax1.set_title('Original picture')
    ax1.imshow(image_rgb)

    ax2.set_title('Edge (white) and result (red)')
    ax2.imshow(edges)

    plt.show()

#findEllipse(edges)
showimgs()
