import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)

"""
    here, numpy is used for creating array. Now the np.zeros function is  
    used for creating a array that containes only zero. This gives a black image
    
    it  give a 512*512 px of black image 
    
    and 3 is used for RGB value
    
    
"""

#Draw a diagonal blue line with thickness of 5 px
#             (x, y)
# cv.line(img,(1,256),(511, 256),(0,0,255),5)
# cv.line(img,(256,1),(256, 511),(255,0,0),5)


#rectangle
# cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

#circle
# cv.circle(img,(447,63), 63, (0,0,255), -1)


#ellipse
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


"""
    1st param ===> is used for giving the image
    2nd param ===> it is the starting index, from where the line will start
    3rd param ===> it is the end index
    4th param ===> it is the color of the line
    5th param ===> it takes the , how thick the line is

"""


cv.imshow("img", img)

cv.waitKey(0)
