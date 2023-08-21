import cv2 as cv
import numpy as np

image = np.ones((300, 300, 3), np.uint8) * 255

pt1 = (150, 100)
pt2 = (100, 200)
pt3 = (200, 200)

cv.circle(image, pt1, 2, (0,0,255), -1)
cv.circle(image, pt2, 2, (0,0,255), -1)
cv.circle(image, pt3, 2, (0,0,255), -1)

triangle_cnt = np.array( [pt1, pt2, pt3] )

cv.drawContours(image, [triangle_cnt], 0, (255,255,0), -1)
cv.rectangle(image, (100, 200), (200, 400),(255,255,0), -1)

cv.imshow("image", image)
cv.waitKey()
cv.destroyAllWindows()