import cv2
import numpy as np

image=cv2.imread('image.png')
image1=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image2=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image1=cv2.equalizeHist(image1)
m=len(image1)
n=len(image1[0])
for i in range(m):
    for j in range(n):
        image2[i][j][2]=image1[i][j]
image2=cv2.cvtColor(image2, cv2.COLOR_HSV2BGR)
cv2.imwrite('enhance.png', image2)