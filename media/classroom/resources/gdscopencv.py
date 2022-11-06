import cv2
import numpy as np
import glob2
import imutils

img_paths=glob2.glob("/**.jpg")
images=[]
for image in img_paths:
    img =cv2.imread(image)
    images.append(img)

imageStitcher=cv2.Stitcher_create()
error,stitched_img=imagesStitcher.stitch(images)
if not error:
    cv2.imwrite("stitched.png",stitched_img)

    stitched_img=cv2.copyMakeBorder(stitched_img,10,10,10,10,cv2.BORDER_CONSTANT,(0,0,0))
    gray_img=cv22cvt.cvtColor(stitched_img,cv2.COLOR_BGR2GRAY)
    thresh_img=cv2.threshold(gray_img,0,255,cv2.THRESH_BINARY)[1]

    cv2.imwrite("thresh.png",thresh_img)
    contours=cv2.findContours(thresh_img.copy(),cv2.RETR)
    
