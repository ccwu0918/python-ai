from cvzone.FaceMeshModule import FaceMeshDetector
import cv2
import numpy as np

img = cv2.imread("images/face.jpg")
detector = FaceMeshDetector(maxFaces=8)
img, faces = detector.findFaceMesh(img, draw=False)
if faces:
    face_leye = detector.getFacePart(img, 0, "LEFT_EYE")
    height_leye, width_leye = detector.getFacePartSize(face_leye)
    print("LEFT_EYE:", width_leye, height_leye)
    face_oval = detector.getFacePart(img, 0, "FACE_OVAL")
    height_oval, width_oval = detector.getFacePartSize(face_oval)
    print("FACE OVAL:", width_oval, height_oval)
    points = np.array(face_oval, np.int32)
    cv2.polylines(img, [points], True, (0, 0, 255), 1)  
    points = np.array(face_leye, np.int32)
    cv2.polylines(img, [points], True, (0, 255, 255), 1)     

cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()