import cv2
import numpy as np

#img = cv2.imread("/home/pi/Desktop/opencv_practice/shapes_opencv-06.png")
img = cv2.imread("/Users/jessepelzar/Desktop/opencv_practice/shapes_opencv-05.png")

img = cv2.resize(img, (500,800))
#cv2.imshow('image',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#(on what, how many up to, image quality, minimum distance)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('corner', img)
cv2.imwrite( "/Users/jessepelzar/Desktop/opencv_practice/color_on_white.png", img );
cv2.waitKey(0)
