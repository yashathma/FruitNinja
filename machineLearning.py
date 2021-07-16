import cv2
import os
import time
import uuid
import tensorflow as tf

IMAGES_PATH = 'D:\GitHub\SLAIComputerVisionProject\Tensorflow\workspace\images'

labels = ['hand']
number_imgs = 0

for label in labels:
    os.mkdir('' + label)
    cap = cv2.VideoCapture(0)
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    cap.release()