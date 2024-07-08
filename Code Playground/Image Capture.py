import cv2 as cv
import os
import time

directory = "Batman"

parent_dir = "C:\\Users\\thunk\\Desktop\\My Project\\Python\\Code Playground"

path = os.path.join(parent_dir , directory)


if not os.path.exists(path):
    os.mkdir(path)

file_list = os.listdir(path)

print(len(file_list))

i = 0
if input("Reorder file(y/n)?: ") == "y":
    for file in file_list:
        file = os.path.join(path , file)
        file_path = os.path.join(path , f"batman{i}.png")
        if not os.path.exists(file_path):
            os.rename(file , file_path)
        i += 1

i = len(os.listdir(path))

cap = cv.VideoCapture(0)

cur_time = time.time()

while True:

    ret , frame = cap.read()
    display = frame.copy()
    cv.putText(display , f"img saved: {i}" , (50 , 50) , cv.FONT_HERSHEY_PLAIN , 2 , (255 , 255 , 0) , 3)
    cv.imshow("Image" , display)
    
    if time.time() - cur_time >= 2:
        img_path = os.path.join(path , f"batman{i}.png")
        cv.imwrite(img_path , frame)
        cur_time = time.time()
        i += 1



    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()