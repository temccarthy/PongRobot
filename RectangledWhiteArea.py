import numpy as np
import cv2

from RedMask2 import *

#cv2.imshow("combo",mask_images(img6)[1])



def crop_image(img):

    aMask = mask_images(img)[1]

    contours, hier = cv2.findContours(aMask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)


    for i,cnt in enumerate(contours):
        if i==0:
            bigcnt=cnt
        if cv2.contourArea(cnt)>cv2.contourArea(bigcnt):
            bigcnt=cnt

    (x,y,w,h) = cv2.boundingRect(bigcnt)

    cv2.rectangle(aMask,(x,y),(x+w,y+h),(100,150,80),1)

    cv2.drawContours(aMask, contours, -1, (80,255,0), 2)

    

    #blank = np.ones((4000,5000,3), np.uint8) * 255
    #blank = cv2.CreateImage((1000,1000),IPL_DEPTH_8U,3)
    #cv2.rectangle(blank,(x,y),(x+w,y+h),(100,150,80),1)
    #cv2.imshow("rectangled blank",cv2.resize(blank,(0,0),fx=.25,fy=.25))
    #print(type(aMask))
    aMaskCrop = aMask[y:y+h,x:x+w]
    #print(aMaskCrop.size)
    #print(type(aMaskCrop))
    cv2.imshow("cropped",cv2.resize(aMaskCrop,(0,0),fx=.25,fy=.25))

    cv2.imshow("rectangled",cv2.resize(aMask,(0,0),fx=.25,fy=.25))
        
    print(x,y,w,h)

    #imwrite("croppedL.jpg",aMaskCrop)
    
    return x,y,w,h,aMaskCrop

crop_image(img3)
