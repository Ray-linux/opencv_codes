import cv2 as cv

img = cv.imread("images/bimal.jpeg")


cv.imshow("Display image", img)
k = cv.waitKey(0)


if k == ord('s'):
    cv.imwrite('bimal_save.jpg', img)