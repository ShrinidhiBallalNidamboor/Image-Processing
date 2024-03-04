import cv2
import numpy as np

image=cv2.imread('image.png')
temp1=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp2=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp3=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        temp1[i][j]=image[i][j][0]
        temp2[i][j]=image[i][j][1]
        temp3[i][j]=image[i][j][2]
clahe=cv2.createCLAHE(clipLimit=10)
temp1=clahe.apply(temp1)
temp2=clahe.apply(temp2)
temp3=clahe.apply(temp3)
for i in range(m):
    for j in range(n):
        image[i][j][0]=temp1[i][j]
        image[i][j][1]=temp2[i][j]
        image[i][j][2]=temp3[i][j]
cv2.imwrite('enhance.png', image)