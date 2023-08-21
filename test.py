import cv2 as  cv

img = cv.imread("images/bimal.jpeg", cv.IMREAD_GRAYSCALE)

print(img.shape)