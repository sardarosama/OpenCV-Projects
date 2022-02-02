"""
@author: Global Computers
Face Mesh Detection using OpenCV and mediapipe

"""
import cvzone
import cv2
import numpy as np
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)

detector = FaceMeshDetector(maxFaces=2)

while True:
    ret, img = cap.read()
    #cv2.imwrite("D://test.jpg", img)
    img, bboxs = detector.findFaceMesh(img)
    
    if bboxs:
        print(bboxs[0])
        
    
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows