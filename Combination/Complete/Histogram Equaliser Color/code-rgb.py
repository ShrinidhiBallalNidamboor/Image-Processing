import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
temp=cv2.imread('image.png')
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

m=len(temp)
n=len(temp[0])

for i in range(m):
    for j in range(n):
        temp[i][j]=image[i][j][2]
temp=cv2.blur(temp, (2, 2))
for i in range(m):
    for j in range(n):
        image[i][j][2]=temp[i][j]
image=cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

for i in range(m):
    for j in range(n):
        temp[i][j]=image[i][j][0]
temp=cv2.equalizeHist(temp)
for i in range(m):
    for j in range(n):
        image[i][j][0]=temp[i][j]

for i in range(m):
    for j in range(n):
        temp[i][j]=image[i][j][1]
temp=cv2.equalizeHist(temp)
for i in range(m):
    for j in range(n):
        image[i][j][1]=temp[i][j]

for i in range(m):
    for j in range(n):
        temp[i][j]=image[i][j][2]
temp=cv2.equalizeHist(temp)
for i in range(m):
    for j in range(n):
        image[i][j][2]=temp[i][j]

cv2.imwrite('enhance.png', image)