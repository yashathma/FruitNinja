import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img2 = cv2.imread("/Users/yash/PycharmProjects/FruitNinja/Hand.png")

while True:
    res, img1 = cap.read()
    # gImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    # res, tMask = cv2.threshold(gImg, 50, 255, cv2.THRESH_BINARY)
    # maskedImg2 = cv2.bitwise_and(img1, img1, mask=tMask)
    # print("Threshold mask")

    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    lowThresh = 100
    highThresh = 150
    img1 = cv2.Canny(gray, lowThresh, highThresh)

    # img1 = cv2.blur(img1, (5, 5))
    # img1 = cv2.inRange(img1, np.array([120, 120, 100]), np.array([255, 255, 255]))

    orb = cv2.ORB_create()
    bfMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # Find all stable matches: matches is a list of Match objects that identify the indices of the matching
    matches = bfMatcher.match(des1, des2)

    # Sort matches by distance (best matches come first in the list)
    matches.sort(key=lambda mat: mat.distance)

    # Find index where matches start to be over threshold
    i = 0
    for i in range(len(matches)):
        if matches[i].distance > 50.0:
            break

    # Draw good-quality matches up to the threshold index
    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:i], None)

    cv2.imshow("Video", img3)

    cv2.waitKeyEx(30)
