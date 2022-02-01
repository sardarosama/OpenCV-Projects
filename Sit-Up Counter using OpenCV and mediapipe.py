"""
@author: Osama Shakeel
Sit-Up Couonter using OpenCV and mediapipe

"""
import cv2
import numpy as np
from cvzone.PoseModule import PoseDetector


detector = PoseDetector(detectionCon=0.5)

cap = cv2.VideoCapture(0)
per = 0
angle = 0
color = (0,0,255)
situps = 0
dir = 0

while True:
    _, img = cap.read()
    
    img = detector.findPose(img)
    lmlist,bbox = detector.findPosition(img,False)
    cv2.imshow("Situp counter", img)
    
    if lmlist:
        #print(lmlist)
        angle = detector.findAngle(img, 24,26,28)
        #print(angle)
        per = np.interp(angle,(30,180), (15, 15+300))
        bar_value = np.interp(angle,(25,170), (100,0))
        #print(per)
        cv2.rectangle(img,(580, int(bar_value)),(580+30, 15+350), color ,cv2.FILLED)
        cv2.rectangle(img,(580,15),(580+30, 15+350), (),3)
        if per ==100:
            if dir ==0:
                situps += 0.5
                dir = 1
                color = (0,255,0)
            
        elif per == 0:
            if dir == 1:
                situps += 0.5
                dir = 0
                color = (0,255,0)
                
        else:
            color = (0,0,255)
       
        print(situps)
        #cvzone.putTextRect(img, str(int(situps)),(40,40),2,2)
        cv2.putText(img, f'Number of Situps : {str(int(situps))}', (30,40),2,2,colorT= (255,255,255), colorR= (0,0,255),border = 2)
    
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()