import cv2

path = "opencv-course-master\Resources\Photos\park.jpg"
bgr = cv2.imread(path)

# BGR to Grayscale
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# BGR to HSV
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

# BGR to RGB
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('LAB --> BGR', lab_bgr)

cv2.waitKey(0)