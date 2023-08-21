import numpy as np
import cv2 as cv

img = cv.imread("images/baroon.jpeg")

print(img.shape)
print(img.size)
print(img.dtype)

"""
    gives the output (500, 490, 3)
    
    resolution is 500 * 490 and it is an bgr image
    
    you can also get the size and data-type of the image using
    
    "img.size" and "img.dtype"
    
"""


cv.waitKey(0)