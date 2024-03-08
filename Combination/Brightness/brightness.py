import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m=len(gray)
n=len(gray[0])
for i in range(m):
    for j in range(n):
        gray[i][j]=np.log2(gray[i][j]+1)
for i in range(m):
    for j in range(n):
        gray[i][j]+=100
for i in range(m):
    for j in range(n):
        image[i][j][2]=gray[i][j]
image=cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
cv2.imwrite('brightness.jpg', image)