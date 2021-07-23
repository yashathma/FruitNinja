import os
import random
import time
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('Hand.png')


while True:
    res, frame = cap.read()
    if not res:
        break
    # frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    face_rects = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in face_rects:
       cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("thresh", frame)