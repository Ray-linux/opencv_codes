#reading images and videos

import cv2 as cv #importing the open cv library 

#reading an image from images folder
"""

img = cv.imread('images/bimal.jpeg')

cv.imshow("bimal", img)  #1st param is used for name of the window and 2nd is the actual image


cv.waitKey(0) #this is used for hold the image window and '0' means it wait for infinite time and you can all pass time in mili second

"""


#reading a video file from the videos folder

capture = cv.VideoCapture('videos/dog.mp4')

while  True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break;
    
capture.release()
cv.destroyAllWindows()