"""
@author: Osama Shakeel
HeadShot Predictor using OpenCV and mediapipe

"""
import cv2
import cvzone
import numpy as np
import time
from cvzone.FaceDetectionModule import FaceDetector

det = FaceDetector()

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ctime = 0
ptime = 0

while True:
    _, img = cap.read()
    img,bbox = det.findFaces(img, False)
    
    if bbox:
        #print(bbox)
        cx,cy = bbox[0]['center']
        print(cx,cy)
        cv2.line(img,(0,cy-110), (640,cy-100), (),2)
        cv2.line(img,(cx,0), (cx,480), (),2)
        cv2.circle(img, (cx,cy-110), 6, (213,123,45), cv2.FILLED )
        cv2.circle(img, (cx,cy-110), 25, (60,175,20), 2 )
        cvzone.putTextRect(img,f'({cx},{cy-90})',(cx+60,cy-130),1.6,2,colorT=(255,255,255), colorR= (255,0,0), border = 3)
        
    ctime = time.time()
    fps = 1/(ctime-ptime) 
    ptime = ctime
    cvzone.putTextRect(img,f'FPS:{int(fps)}',(15,450),1.3,2,colorT=(255,255,255), colorR= (255,0,0), border = 3)
    cv2.imshow("HeadShot Predictor", img)
    
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()