import cv2
import numpy as np

image=cv2.imread('coin.png')
m=len(image)
n=len(image[0])
o=len(image[0][0])

levels=2
levels=levels**2

for i in range(m):
    for j in range(n):
        for k in range(o):
            value=256//levels
            value=np.floor(image[i][j][k]/value)*value
            image[i][j][k]=value

cv2.imwrite('binary.png', image)