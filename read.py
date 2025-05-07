import cv2 as cv

# Reading Photos

img = cv.imread("Photos/cat_large.jpg")

cv.imshow("Cat", img)

# Reading Videos

cv.waitKey(0)

