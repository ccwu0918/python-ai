from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/fitness.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    angle, img = detector.findAngle(lmList[24], lmList[26], lmList[28], img)
    print(angle)
    print(detector.angleCheck(angle, 140, addOn=20))
    print(detector.angleCheck(angle, 90, addOn=20))
    
cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()