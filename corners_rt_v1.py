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

while True:
    img = vs.read()
    #img = vs.resize(img, (500,800))
    #cv2.imshow('image',img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    #(on what, how many up to, image quality, minimum distance)
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corners = np.int0(corners)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(img, (x,y), 5, (0,255,255), -1)

    cv2.imshow('corner', img)
    #cv2.waitKey(0)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
            break

    # update the FPS counter
    fps.update()
