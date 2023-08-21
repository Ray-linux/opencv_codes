import numpy as np
import cv2 as cv

baroon = cv.imread("images/baroon.jpeg")

face = baroon[157:258, 147:207]

baroon[257:358, 247:307] = face
cv.imshow("barron", baroon)

cv.waitKey(0)
