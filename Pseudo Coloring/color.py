import cv2
import numpy as np

image = cv2.imread('grey.png')
m=len(image)
n=len(image[0])
o=len(image[0][0])
for i in range(m):
    for j in range(n):
        temp=image[i][j][0]*3
        image[i][j][0]=temp*0.0722
        image[i][j][1]=temp*0.587
        image[i][j][2]=temp*0.2126
cv2.imwrite("color.png", image)
