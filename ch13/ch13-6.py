from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/push_up.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    angle1, img = detector.findAngle(lmList[11], lmList[23], lmList[25], img)
    print(angle1)
    angle2, img = detector.findAngle(lmList[11], lmList[13], lmList[15], img)
    print(angle2)
    
cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
