import cv2
import os
import time
import uuid
import tensorflow as tf

IMAGES_PATH = 'D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/images/allimages'

labels = ['hand']
number_imgs = 100

for label in labels:
    cap = cv2.VideoCapture(0)
    print('collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(0.5)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    cap.release()
