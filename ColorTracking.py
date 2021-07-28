import random

import cv2
import numpy as np

def distance(x1, y1, x2, y2):
    return ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)


def averageList(inputArr):
    total = 0
    for idx in inputArr:
        total += idx

    return int(total/len(inputArr))


cap = cv2.VideoCapture(0)
distanceBetween = 0

FrameCount = 0

Lives = 3

FruitxAxis = 500
FruityAxis = 250

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)

score = 0

HandX = 100
HandY = 100
xRate = 20
yRate = 20

hand = cv2.imread("Hand.png")

while True:
    FrameCount += 1

    distanceBetween = distance(FruityAxis, FruitxAxis, HandX, HandY)



    #Threshing
    res, img = cap.read()
    hsvim = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 0], dtype="uint8")
    upper = np.array([100, 100, 100], dtype="uint8")
    skinRegionHSV = cv2.inRange(hsvim, lower, upper)
    blurred = cv2.blur(skinRegionHSV, (2, 2))
    ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)
    thresh = cv2.flip(thresh, 1)
    img = cv2.flip(img, 1)



    #Hand Center

    M = cv2.moments(thresh)
    HandX = int(M["m10"] / M["m00"])
    HandY = int(M["m01"] / M["m00"])
    #cv2.ellipse(img, (HandX, HandY), (20, 20), 30, 0, 360, (255, 255, 255), 1)
    cv2.putText(img, "("+str(HandX)+","+str(HandY)+")", (HandX-40, HandY+10 ), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 255, 255),2, cv2.LINE_AA, False)


    #Fruit
    if FruitxAxis>thresh.shape[0]-100 or FruitxAxis<50:
        xRate = xRate*(-1)
    if FruityAxis>thresh.shape[1]-50 or FruityAxis<50:
        yRate = yRate*(-1)
    FruitxAxis+=xRate
    FruityAxis+=yRate








    cv2.ellipse(img, (FruityAxis, FruitxAxis), (50, 50), 30, 0, 360, (red, green, blue), -1)

    #Score

    if FrameCount > 50:
        FrameCount = 0
        Lives -= 1

    if distanceBetween<300 or FrameCount>50:
        score+=100
        FrameCount = 0

        while (distance(FruityAxis,FruitxAxis,HandX,HandY)<600):
            FruitxAxis = random.randint(100, 700)
            FruityAxis = random.randint(100, 1500)

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)



    cv2.putText(img, str(score), (100,200), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 4, cv2.LINE_AA, False)


    if Lives == 3:
        cv2.ellipse(img, (1800, 70), (30, 30), 30, 0, 360, (0, 0, 255), -1)
        cv2.ellipse(img, (1700, 70), (30, 30), 30, 0, 360, (0, 0, 255), -1)
        cv2.ellipse(img, (1600, 70), (30, 30), 30, 0, 360, (0, 0, 255), -1)
    elif Lives == 2:
        cv2.ellipse(img, (1800, 70), (30, 30), 30, 0, 360, (0, 0, 255), -1)
        cv2.ellipse(img, (1700, 70), (30, 30), 30, 0, 360, (0, 0, 255), -1)
    elif Lives == 1:
        cv2.ellipse(img, (1800, 70), (30, 30), 30, 0, 360, (0, 0, 255), -1)




    cv2.imshow("Fruit Ninja", img)





    cv2.waitKey(1)