import cv2
import numpy as np

img = cv2.imread("opencv-course-master\Resources\Photos\cat.jpg")

#Gray Scale
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray" , gray)

#Blur
blur = cv2.GaussianBlur(img , (9 , 9) , cv2.BORDER_DEFAULT)
cv2.imshow("Blur" , blur)

#Canny
canny = cv2.Canny(blur , 100 , 200)
cv2.imshow("Canny" , canny)

#Dilate
dilate = cv2.dilate(canny , (3 , 3) , iterations = 10)
cv2.imshow("Dilate" , dilate)

#Erode
erode = cv2.erode(dilate , (3 , 3) , iterations= 5)
cv2.imshow("Erode" , erode)

#Resize
resize = cv2.resize(erode , (500 , 500) , interpolation= cv2.INTER_CUBIC)
cv2.imshow("Resize" , resize)

#Cropping
crop = img[50:200 , 20:200]
cv2.imshow("Crop" , crop)

cv2.waitKey()