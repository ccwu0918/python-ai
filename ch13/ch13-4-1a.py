from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/woman2.jpg")
detector = PoseDetector()
pose = detector.findPose(img, draw=False)
if pose:
    lmList = pose["lmList"]
    for point in lmList:
        cv2.circle(img, point, 3, (0, 255, 255), cv2.FILLED)

cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()