import cv2
import numpy

def rescaleFrame(frame , scale = 0.75):
    #Images, Videos, and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width , height) #Tuple

    return cv2.resize(frame , dimensions , interpolation = cv2.INTER_AREA)

def changeRes(width , height):
    #Live Videos
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT , height)

# img = cv2.imread("dataset\colorobject.png")
# cv2.imshow("Hi" , img)

vid = cv2.VideoCapture("opencv-course-master\Resources\Videos\dog.mp4")

while True:
    isTrue , frame = vid.read()
    #cv2.imshow("Frame" , frame)

    frame_resized = rescaleFrame(frame)
    cv2.imshow("Resized" , frame_resized)

    res = cv2.waitKey(20)
    print("Res:" , res)
    if res & 0xFF == ord(" "):
        break

vid.release()
cv2.destroyAllWindows()
