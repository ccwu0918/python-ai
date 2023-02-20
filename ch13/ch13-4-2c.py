from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/fitness.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    length, distInfo = detector.findDistance(lmList[11], lmList[25])
    msg = str(int(length))
    point1, point2, center = distInfo
    cv2.line(img, point1, point2, (255, 0, 255), 3)
    cv2.circle(img, point1, 15, (255, 0, 255), cv2.FILLED)
    cv2.circle(img, point2, 15, (255, 0, 255), cv2.FILLED)
    cv2.circle(img, center, 15, (0, 0, 255), cv2.FILLED)
    cv2.putText(img, msg, (10, 35),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()