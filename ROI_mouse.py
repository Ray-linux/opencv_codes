import numpy as np
import cv2 as cv

image = cv.imread("images/baroon.jpeg")
  
# Select ROI
r = cv.selectROI("select the area", image)
  
# Crop image
cropped_image = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
  
# Display cropped image
cv.imshow("Cropped image", cropped_image)

cv.waitKey(0)