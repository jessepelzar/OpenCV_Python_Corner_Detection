import imutils
import cv2

cap = cv2.VideoCapture(0)
while True:
          ret,frame=cap.read()
          gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
          ret,thresh = cv2.threshold(gray,140,255,0)
          image,contours,hie = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
          frame = cv2.drawContours(frame, contours, 3, (0,255,0), 3)
          cv2.imshow("vid",frame)
          if cv2.waitKey(1) & 0xFF == ord('q'):
                           break
