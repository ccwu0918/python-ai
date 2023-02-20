from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/fitness.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    length, distInfo, img = detector.findDistance(lmList[11], lmList[25], img)
    print(length, distInfo)

cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()