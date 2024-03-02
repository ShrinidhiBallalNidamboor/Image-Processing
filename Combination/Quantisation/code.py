import cv2
import numpy as np

image=cv2.imread('coin.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
level=2
level=level**2
m=len(image)
n=len(image[0])
hashing={}
for i in range(m):
    for j in range(n):
        image[i][j]=(image[i][j]//(256//level))*(256//level)
        hashing[image[i][j]]=1
print(hashing)
cv2.imwrite('binary.png', image)