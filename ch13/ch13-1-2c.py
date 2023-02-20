from cvzone.HandTrackingModule import HandDetector
import cv2

img = cv2.imread("images/hand2.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=2)
hands, img = detector.findHands(img)
if hands:
    hand1 = hands[0]
    lmList1 = hand1["lmList"]
    angle, img = detector.findAngle(lmList1[9], lmList1[10],
                                    lmList1[11], img)
    print(angle)
    print(detector.angleCheck(angle, 150, addOn=20))
    print(detector.angleCheck(angle, 100, addOn=20))

cv2.imshow("Hand", img)
cv2.waitKey(0)
cv2.destroyAllWindows()