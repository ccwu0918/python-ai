from cvzone.HandTrackingModule import HandDetector
import cv2

img = cv2.imread("images/hand3.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=2)
hands, img = detector.findHands(img)
if hands:
    hand1 = hands[0]
    lmList1 = hand1["lmList"]
    bbox1 = hand1["bbox"]
    length, info, img = detector.findDistance(lmList1[4],lmList1[8],img)
    print(info)
    msg = "Dist:" + str(int(length))
    cv2.putText(img, msg, (bbox1[0]+100,bbox1[1]-30),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)        

cv2.imshow("Hand", img)
cv2.waitKey(0)
cv2.destroyAllWindows()