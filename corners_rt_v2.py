from imutils.video import VideoStream
from imutils.video import FPS
from multiprocessing import Process
from multiprocessing import Queue
import argparse
import imutils
import time
import cv2
import numpy as np


print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
fps = FPS().start()

rect = np.zeros((512,512,3), np.uint8)

while True:

    
   



    img = vs.read()

    x_min = 200
    x_max = 500
    y_min = 100
    y_max = 400
    
    point_1 = [x_min,y_min]
    point_2 = [x_min,y_max]
    point_3 = [x_max,y_max]
    point_4 = [x_max,y_min]
    
    #img = vs.resize(img, (500,800))
    #cv2.imshow('image',img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    #(on what, how many up to, image quality, minimum distance)
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corners = np.int0(corners)

    for corner in corners:
        x, y = corner.ravel()
        if (x > x_min and x < x_max) and (y > y_min and y < y_max):
            cv2.circle(img, (x,y), 5, (255,0,0), -1)
        else:
            cv2.circle(img, (x,y), 5, (0,255,255), -1)
        #[row,col](top left,bottom left,bottom right,top right)
        # x = 200 to 500  y = 100 to 400
        pts = np.array([point_1,point_2,point_3,point_4], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,255,255))

    cv2.imshow('corner', img)
    
    #cv2.waitKey(0)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
            break

    # update the FPS counter
    fps.update()
