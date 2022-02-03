"""
@author: Osama Shakeel
Sit-Up Couonter using OpenCV and mediapipe

"""

import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    ret, img = cap.read()
    img, bboxs = detector.findFaces(img)
    print(bboxs)
    if bboxs:
        center = bboxs[0]["center"]
        #cv2.circle(img,center, 5,(255,0,255), cv2.FILLED)
        
        
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) ==27:
        break
cap.release()
cv2.destroyAllWindows()