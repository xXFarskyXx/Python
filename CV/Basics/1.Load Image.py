import cv2
import numpy


img = cv2.imread("dataset\colorobject.png")
cv2.imshow("Hi" , img)

vid = cv2.VideoCapture("opencv-course-master\Resources\Videos\dog.mp4")

while True:
    isTrue , frame = vid.read()

    cv2.imshow("Frame" , frame)

    res = cv2.waitKey(20)
    print("Res:" , res)
    if res & 0xFF == ord(" "):
        break

vid.release()
cv2.destroyAllWindows()
