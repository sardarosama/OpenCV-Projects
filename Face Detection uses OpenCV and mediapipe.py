"""

@author: Global Computers
Face Detection using OpenCV and mediapipe

"""
import cvzone
import cv2
import numpy as np
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)

detector = FaceDetector()

while True:
    ret, img = cap.read()
    #cv2.imwrite("D://test.jpg", img)
    img, bboxs = detector.findFaces(img)
    
    if bboxs:
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255,0,255), cv2.FILLED)
        
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows