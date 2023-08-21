import numpy as np
import cv2 as cv


img = np.zeros((512, 512, 3), np.uint8)

#circle
cv.circle(img,(347,63), 63, (0,255,0), -1)
font = cv.FONT_HERSHEY_SIMPLEX

cv.putText(img,'Bimal and Sourav',(10,500), font, 1,(255,255,255),4,cv.LINE_AA)

"""
    
"""

cv.imshow("img", img)

cv.waitKey(0)