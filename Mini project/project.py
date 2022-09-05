import numpy as np
from cv2 import cv2

classifyImage=cv2.CascadeClassifier('C:/Users/Amit gupta/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
originalImage=cv2.imread('C:/Users/Amit gupta/Desktop/zuckerberg-testify-ap-img.jpg')
grayImg=cv2.cvtColor(originalImage,cv2.COLOR_BGR2GRAY)

# region of interest tro detect the face
faceROI=classifyImage.detectMultiScale(grayImg,1,3.5)

# check if face ROI tuple is empty or not

if faceROI is ():
    print('No face detected')

#iterate through face data and draw2a rectangle around

for(x,y,w,h) in faceROI:
    cv2.rectangle(originalImage,(x,y),(x+w,y+h),(127,0,250),2)
    cv2.imshow('face detect resut',originalImage)
    cv2.waitKey(0)

cv2.destroyAllWindows()    
