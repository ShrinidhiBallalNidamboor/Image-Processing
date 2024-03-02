import cv2
import numpy as np

image=cv2.imread('image.png')
temp=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
clahe=cv2.createCLAHE(clipLimit=10)
temp=clahe.apply(temp)
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        image[i][j][2]=temp[i][j]
image=cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
cv2.imwrite('enhance.png', image)