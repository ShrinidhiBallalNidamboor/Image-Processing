import cv2
import numpy as np

image = cv2.imread('nature.jpg')
m=len(image)
n=len(image[0])
o=len(image[0][0])
for i in range(m):
    for j in range(n):
        image[i][j][0]+=5
        image[i][j][1]+=5
        image[i][j][2]+=5
        if image[i][j][0]>=255:
            image[i][j][0]=255
        if image[i][j][1]>=255:
            image[i][j][1]=255
        if image[i][j][2]>=255:
            image[i][j][2]=255
cv2.imwrite("brightness.jpg", image)
