import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Bimal and Sourav',(10,200), font, 1,(255,255,255),4,cv.LINE_AA)

"""   
    1st param ===> image input
    2nd param ===> text 
    3rd param ===> start index
    4th param ===> font type
    5th param ===> font size
    6th param ===> font color
    7th param ===> font weight(means how much bold)
    
    8th param(cv.LINE_AA) ===> regular things like color,
                            thickness, lineType etc. For better look, 
                            lineType = cv.LINE_AA is recommended.
"""

cv.imshow("img", img)
cv.waitKey(0)