from cvzone.HandTrackingModule import HandDetector
import cv2

detector = HandDetector(detectionCon=0.5, maxHands=1)
img = cv2.imread("images/OK.jpg")
hands, img = detector.findHands(img)
if hands:
    hand = hands[0]
    lmList1 = hand["lmList"]
    fingers = detector.fingersUp(hand)
    totalFingers = fingers.count(1)
    print(totalFingers)
    msg = "None"
    if fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
        length, info, img = detector.findDistance(lmList1[8],lmList1[4],img)
        print("Length:", length)
        if length <= 30:
            angle, img = detector.findAngle(lmList1[5], lmList1[6], lmList1[7],img)
            print("Angle:", angle)
            if detector.angleCheck(angle, 100, addOn=20):                    
                msg = "OK"
    cv2.putText(img, msg, (10, 30),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

cv2.imshow("Hand", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
