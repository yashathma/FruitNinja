import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    res, img = cap.read()
    gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (height, width, depth) = img.shape


    # a rectangular mask that keeps the middle of a picture
    rMask = np.zeros((height, width, 1), np.uint8)
    rMask[(height // 4):3 * (height // 4), (width // 4):3 * (width // 4)] = 255

    # applying a mask to an image (this is a bit weird)
    maskedImg1 = cv2.bitwise_and(img, img, mask=rMask)



    # Using thresholding to create a mask
    res, tMask = cv2.threshold(gImg, 25, 255, cv2.THRESH_BINARY)
    maskedImg2 = cv2.bitwise_and(img, img, mask=tMask)


    cv2.imshow("Video", maskedImg2)

    cv2.waitKeyEx(30)

