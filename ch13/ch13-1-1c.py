from cvzone.HandTrackingModule import HandDetector
import cv2

img = cv2.imread("images/hands.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=2)
hands = detector.findHands(img, draw=False)
if hands:
    hand1 = hands[0]   # 第1隻手
    x, y, w, h = hand1["bbox"]
    cv2.rectangle(img, (x, y), (x+w, y+h),
                               (0, 0, 255), 2)
    for point in hand1["lmList"]:
        cv2.circle(img, point, 3, (0, 255, 255), cv2.FILLED)     
    if len(hands) == 2:
        hand2 = hands[1]   # 第2隻手
        x, y, w, h = hand2["bbox"]
        cv2.rectangle(img, (x, y), (x+w, y+h),
                                   (0, 0, 255), 2)
        for point in hand2["lmList"]:
            cv2.circle(img, point, 3, (0, 255, 255), cv2.FILLED)
        
cv2.imshow("Hands", img)
cv2.waitKey(0)
cv2.destroyAllWindows()