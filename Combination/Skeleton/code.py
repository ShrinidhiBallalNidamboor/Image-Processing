import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel=cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
for i in range(5):
    open=cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    sub=image-open
    close=cv2.erode(image, kernel, iterations=1)
    cv2.bitwise_or(close, temp)