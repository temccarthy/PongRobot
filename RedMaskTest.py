import numpy as np
import cv2

img1 = cv2.imread("Pong1.JPG",1)
img2 = cv2.imread("Pong2.JPG",1)
img3 = cv2.imread("Pong3.JPG",1)
img4 = cv2.imread("Pong4.JPG",1)
img5 = cv2.resize(cv2.imread("Pong5flash.JPG",1), (0,0), fx=.25,fy=.25) 
img6 = cv2.imread("Pong6.JPG",1)
img7 = cv2.imread("Pong7flash.JPG",1)
img8 = cv2.imread("Pong8.JPG",1)
img9 = cv2.imread("Pong9flash.JPG",1)
img10 = cv2.imread("Triangle1.JPG",1)
img11 = cv2.imread("Triangle2.JPG",1)



def mask_images(img):

    #img_edit = cv2.resize(img, (0,0), fx=.25, fy=.25)
    #cv2.imshow("original image",img_edit)

    #img3edit = cv2.resize(img3, (0,0), fx=.25, fy=.25)
    #cv2.imshow("image3",img3edit)

    hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # converts colors from rgb to hsv (hue saturation value)

##    lowerRed1=np.array([0,180,50]) #lower red limit 
##    upperRed1=np.array([20,255,255]) #upper red limit
##    mask1 = cv2.inRange(hsv_img,lowerRed1,upperRed1) #create mask, which displays white pixels when color of pixel is within limits
##
##    lowerRed2=np.array([160,180,50]) #lower red limit
##    upperRed2=np.array([180,255,255]) #upper red limit
##    mask2 = cv2.inRange(hsv_img,lowerRed2,upperRed2) #create mask


    
    lowerRed1=np.array([int(0),int(50*2.55),int(25*2.55)]) #lower red limit 
    upperRed1=np.array([int(10),int(100*2.55),int(100*2.55)]) #upper red limit
    mask1 = cv2.inRange(hsv_img,lowerRed1,upperRed1) #create mask, which displays white pixels when color of pixel is within limits

    lowerRed2=np.array([int(160),int(50*2.55),int(25*2.55)]) #lower red limit
    upperRed2=np.array([int(180),int(100*2.55),int(100*2.55)]) #upper red limit
    mask2 = cv2.inRange(hsv_img,lowerRed2,upperRed2) #create mask

    

    mask = mask1 + mask2 #combine masks

    output_img = img.copy() #dont know
    output_img[np.where(mask==0)] = 0 #dont know

    #cv2.imshow("combo",output_img)


    return output_img, mask

#cv2.imshow("combo",mask_images(img6)[0])
#cv2.imshow("combo",mask_images(img7)[1])
