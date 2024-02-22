import cv2
import numpy as np

image=cv2.imread('image.png')
temp=cv2.imread('image.png')

temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

m=len(temp)
n=len(temp[0])

kernel=np.matrix([[0.299, 0.587, 0.114],
                [0.59590059, -0.27455667, -0.32134392],
                [0.21153661, -0.52273617, 0.31119955]])

for i in range(m):
    for j in range(n):
        value=np.matrix([[image[i][j][0]], [image[i][j][1]], [image[i][j][2]]])
        value=kernel*value
        image[i][j][0]=value[0][0]
        image[i][j][1]=value[1][0]
        image[i][j][2]=value[2][0]

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

for i in range(m):
    for j in range(n):
        value=np.matrix([[image[i][j][0]], [image[i][j][1]], [image[i][j][2]]])
        value=((kernel)**-1)*value
        image[i][j][0]=value[0][0]
        image[i][j][1]=value[1][0]
        image[i][j][2]=value[2][0]
        print(value)

cv2.imwrite('enhance.png', image)