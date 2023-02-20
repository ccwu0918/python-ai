from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/site_up.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    angle, img = detector.findAngle(lmList[11], lmList[23], lmList[25], img)
    print(angle)
    
cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
