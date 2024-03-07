import cv2
import numpy as np

image=cv2.imread('image.png')
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        if not(image[i][j][2]>=170):
            value=image[i][j][0]/3+image[i][j][1]/3+image[i][j][2]/3
            image[i][j][0], image[i][j][1], image[i][j][2]=value, value, value
cv2.imwrite('red.png', image)
