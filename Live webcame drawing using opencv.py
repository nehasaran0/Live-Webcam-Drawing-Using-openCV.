# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:33:54 2021

@author: nehas
"""

import cv2
import numpy as np

# Setup camera
cap = cv2.VideoCapture(0)
# Set a smaller resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


def nothing(x):
    pass


canny = "Canny"
cv2.namedWindow(canny)
cv2.createTrackbar('Threshold 1', canny, 0, 255, nothing)
cv2.createTrackbar('Threshold 2', canny, 0, 255, nothing)

while True:
    # Capture frame-by-frame
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    t1 = cv2.getTrackbarPos('Threshold 1', canny)
    t2 = cv2.getTrackbarPos('Threshold 2', canny)
    gb = cv2.GaussianBlur(frame, (5, 5), 0)
    can = cv2.Canny(gb, t1, t2)

    cv2.imshow(canny, can)

    frame[np.where(can)] = 255
    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()