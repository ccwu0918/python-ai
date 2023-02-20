from cvzone.HandTrackingModule import HandDetector
import cv2
import turtle

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)
screen = turtle.Screen()
screen.setup(startx=20, starty=50)
msg = "Stop"
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        bbox = hand["bbox"]        
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)
        if totalFingers == 0: 
            msg = "Stop"
        if totalFingers == 1:
            if fingers[0] == 1:
                if msg != "TurnRight":
                    msg = "TurnRight"
                    turtle.right(90) 
        if totalFingers == 2:
            if fingers[1] == 1 and fingers[2] == 1:
                if msg != "Forward":
                    msg = "Forward"
                    turtle.forward(50)               
        if totalFingers == 5:
            break
        cv2.putText(img, msg, (bbox[0]+100,bbox[1]-30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    else:
        msg = "Stop"
    print(msg)    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
turtle.bye()        
cap.release()
cv2.destroyAllWindows()
