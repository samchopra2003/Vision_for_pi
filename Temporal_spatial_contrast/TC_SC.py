"""This module is for a Temporal/Spatial Contrast Camera."""
from scipy import ndimage
import numpy as np
import cv2

source = cv2.VideoCapture(0)
flg = 0

ttd, nmimg = source.read()
while True:

    ret, img = source.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = gray.astype(np.int)

    if flg == 0:
        buffer = gray
        flg = 1

    '''k = np.array([[[1,1,1],[1,1,1],[1,1,1]],
                  [[1,1,1],[0,0,0],[1,1,1]],
                  [[1,1,1],[1,1,1],[1,1,1]]])'''
    k = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    cc = (ndimage.convolve(gray, k, mode='constant', cval=0)) / 8
    # diff = np.asarray(gray, np.float64)
    # diff2 = np.asarray(gray, np.float64)
    diff = gray - cc
    diff2 = cc - gray

    diff3 = cv2.subtract(gray, buffer)
    diff4 = cv2.subtract(buffer, gray)
    # nmimg[:]=127
    nmimg[:] = [127, 127, 127]

    # print(diff)
    nmimg[diff > 5] = [255, 0, 0]
    nmimg[diff2 > 5] = [0, 0, 255]
    nmimg[diff3 > 50] = [255, 255, 255]
    nmimg[diff4 > 50] = [0, 0, 0]
    cv2.imshow("Live", nmimg)
    buffer = gray
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cv2.destroyAllWindows()
source.release()
