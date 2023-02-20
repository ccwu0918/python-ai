import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
  ret, frame = cap.read()
  cv2.imshow("Frame", frame)      
  if cv2.waitKey(1) & 0xFF == ord("q"):
      break
  
cap.release()
cv2.destroyAllWindows()

