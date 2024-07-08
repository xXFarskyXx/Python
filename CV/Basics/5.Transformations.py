import cv2
import numpy as np

def translate(img , x , y , ang_x = 0 , ang_y = 0):
    trans_m = np.float32([[1 , ang_x , x] , [ang_y , 1 , y]])
    dimension = (img.shape[1] , img.shape[0])
    return cv2.warpAffine(img , trans_m , dimension)

def rotate(img , angle ,  rotPoint = None):
    h , w = img.shape[:2]
    dimension = (w , h)

    if rotPoint == None:
        rotPoint = (w//2 , h//2) 

    rot_m = cv2.getRotationMatrix2D(rotPoint , angle , 1)
    print(rot_m)

    return cv2.warpAffine(img , rot_m , dimension)

img = cv2.imread("opencv-course-master\Resources\Photos\cat.jpg")

translated = translate(img , -100 , 0 , ang_x = 0.3)
cv2.imshow("Translate" , translated)

rotated = rotate(img , 50)
cv2.imshow("Rotated" , rotated)

cv2.waitKey()