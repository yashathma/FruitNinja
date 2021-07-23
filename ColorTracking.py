import cv2
import numpy as np

def averageList(inputArr):
    total = 0
    for idx in inputArr:
        total += idx

    return int(total/len(inputArr))


cap = cv2.VideoCapture(0)

xAxis = 500
yAxis = 250
xRate = 20
yRate = 20

while True:
    res, img = cap.read()
    hsvim = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 0], dtype="uint8")
    upper = np.array([100, 100, 100], dtype="uint8")
    skinRegionHSV = cv2.inRange(hsvim, lower, upper)
    blurred = cv2.blur(skinRegionHSV, (2, 2))
    ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)
    thresh = cv2.flip(thresh, 1)




    xList = []
    yList = []
    height = thresh.shape
    for i in range(0, height[0]):
        for g in range(0, height[1]):
            if thresh[i][g] == 255:
                xList.append(g)
                yList.append(i)


    HandXPos = height[1]-averageList(xList)
    HandYPos = averageList(yList)
    cv2.ellipse(img, (HandXPos, HandYPos ), (20, 20), 30, 0, 360, (0, 255, 0), -1)
    cv2.putText(img, "Hand", (HandXPos-20, HandYPos+5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 0),1, cv2.LINE_AA, False)











    if xAxis>thresh.shape[0]-100 or xAxis<50:
        xRate = xRate*(-1)

    if yAxis>thresh.shape[1]-50 or yAxis<50:
        yRate = yRate*(-1)





    xAxis+=xRate
    yAxis+=yRate

    #cv2.ellipse(img, (yAxis, xAxis), (50, 50), 30, 0, 360, (255, 255, 0), -1)

    cv2.imshow("thresh", thresh)





    cv2.waitKey(1)