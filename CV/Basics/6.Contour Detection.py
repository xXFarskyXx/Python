import cv2
import numpy as np

img = cv2.imread("opencv-course-master\Resources\Photos\cats.jpg")

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray , (3 , 3) , cv2.BORDER_DEFAULT)

#Method: Canny
canny = cv2.Canny(blur , 125 , 200)
cv2.imshow("Canny" , canny)

#Method: Thresholding
#ret, thresh = cv2.threshold(gray , 125 , 255 , cv2.THRESH_BINARY)

#Finding Contours
contour , hierarchy = cv2.findContours(canny , cv2.RETR_LIST , cv2.CHAIN_APPROX_NONE)
#contour , hierarchy = cv2.findContours(thresh , cv2.RETR_LIST , cv2.CHAIN_APPROX_NONE)

blank = np.zeros(img.shape , dtype = "uint8")

cv2.drawContours(blank , contour , -1 , (0 , 255 , 0) , thickness = 1)
cv2.imshow("Contours" , blank)

print(len(contour))
#cv2.imshow("Threshold" , thresh)
cv2.imshow("Canny" , canny)

cv2.waitKey()