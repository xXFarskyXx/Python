import cv2

path = "opencv-course-master\Resources\Photos\park.jpg"
bgr = cv2.imread(path)
rgb = cv2.cvtColor(bgr , cv2.COLOR_BGR2RGB)

#Separate 3 Channels
b , g , r = cv2.split(bgr)

gray = cv2.cvtColor(bgr , cv2.COLOR_BGR2GRAY)
blank = b*0

#Merge[b , g , r] ([r , g , b] in plt)
merge = cv2.merge([b , g , r])
cv2.imshow("Merge" , merge)


blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])


cv2.imshow("Blue" , blue)


cv2.waitKey(0)