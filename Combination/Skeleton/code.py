import cv2
import numpy as np

image=cv2.imread('image.png', 0)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
skel=np.zeros(image.shape, np.uint8)
kernel=cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
while True:
    open=cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    temp=cv2.subtract(image, open)
    erode=cv2.erode(image, kernel)
    skel=cv2.bitwise_or(skel, temp)
    image=erode.copy()
    if cv2.countNonZero(image)==0:
        break

cv2.imwrite('thin.png', skel)