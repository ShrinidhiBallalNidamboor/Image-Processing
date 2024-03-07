import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp=cv2.imread('image.png')
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2HSV)
image=cv2.equalizeHist(image)
m=len(temp)
n=len(temp[0])
for i in range(m):
    for j in range(n):
        temp[i][j][2]=image[i][j]
temp=cv2.cvtColor(temp, cv2.COLOR_HSV2BGR)
cv2.imwrite('enhance.png', temp)