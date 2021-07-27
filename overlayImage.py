import cv2
import numpy as np

watermelon = cv2.imread("watermelon.jpg")

cap = cv2.VideoCapture(0)

x_offset = 50
y_offset = 50

while True:
    ret, frame = cap.read()
    scale_percent = 220  # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    x_offset += 5
    y_offset += 5

    resized[y_offset:y_offset+watermelon.shape[0], x_offset:x_offset+watermelon.shape[1]] = watermelon

    cv2.imshow('watermelon', resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break

