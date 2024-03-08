import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        image[i][j]=255-image[i][j]
(number, label, values, centroid)=cv2.connectedComponentsWithStats(image, 4, cv2.CV_32S)
for i in range(1, number):
    cv2.imwrite('binary'+str(i)+'.png', (label==i).astype("uint8")*255)