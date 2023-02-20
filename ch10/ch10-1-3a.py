import cv2 

img = cv2.imread("koala.jpg")
cv2.imwrite("result.png", img)