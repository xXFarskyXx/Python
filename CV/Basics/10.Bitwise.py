import cv2
import numpy as np
path = "opencv-course-master\Resources\Photos\park.jpg"
bgr = cv2.imread(path)
rgb = cv2.cvtColor(bgr , cv2.COLOR_BGR2RGB)

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

cv2.imshow('Rectangle', rectangle)
cv2.imshow('Circle', circle)

# bitwise AND --> intersecting regions
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('Bitwise AND', bitwise_and)

# bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('Bitwise OR', bitwise_or)

# bitwise XOR --> non-intersecting regions
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow('Circle NOT', bitwise_not)

cv2.waitKey(0)