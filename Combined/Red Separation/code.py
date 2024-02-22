import cv2
import numpy as np

image=cv2.imread('image.png')
temp=cv2.imread('image.png')
val=cv2.imread('image.png')
result=cv2.imread('image.png')
m=len(image)
n=len(image[0])

for i in range(m):
    for j in range(n):
        if not(image[i][j][2]>110 and image[i][j][1]<110 and image[i][j][0]<110):
            value=image[i][j][1]
            image[i][j][0]=value
            image[i][j][1]=value
            image[i][j][2]=value
            temp[i][j][0]=value
            temp[i][j][1]=value
            temp[i][j][2]=value
            val[i][j][0]=value
            val[i][j][1]=value
            val[i][j][2]=value
            result[i][j][0]=value
            result[i][j][1]=value
            result[i][j][2]=value
        else:
            temp[i][j][0]=0
            result[i][j][0], result[i][j][2]=result[i][j][2], result[i][j][0]
            image[i][j][1], image[i][j][2]=image[i][j][2], image[i][j][1]

cv2.imwrite('enhance1.png', image)
cv2.imwrite('enhance2.png', temp)
cv2.imwrite('enhance3.png', val)
cv2.imwrite('enhance4.png', result)