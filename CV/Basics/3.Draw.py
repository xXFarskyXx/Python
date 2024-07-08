import cv2
import numpy as np

img = cv2.imread("opencv-course-master\Resources\Photos\cat.jpg")
cv2.imshow("Cat" , img)

#Set Resolution of Cascade
blank = np.zeros((500 , 500 , 3) , dtype = "uint8")
cv2.imshow("Blank Cascade" , blank)

#Assign Value for element in numpy array
blank[:] = 0,255,0
cv2.imshow("Green" , blank)

#Draw rectangle / circle / line
cv2.rectangle(blank , (0 , 0) , (100 , 100) , (0 , 0 , 255) , thickness = 2) #thickness = cv2.FILLED
cv2.imshow("Blank with rectangle" , blank)

cv2.circle(blank , (blank.shape[1]//2 , blank.shape[0]//2) , 40 , (0 , 0 , 0) , thickness = 2)

#Put Text
cv2.putText(blank , "Hello" , (250 , 250) , cv2.FONT_HERSHEY_COMPLEX , 1 , (255 , 0 , 0) , 2)
cv2.imshow("blank with Text" , blank)

cv2.waitKey(0)