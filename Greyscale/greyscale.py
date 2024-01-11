import cv2
import numpy as np

image = cv2.imread('image.png')
m=len(image)
n=len(image[0])
o=len(image[0][0])
for i in range(m):
    for j in range(n):
        temp=0.114*image[i][j][0]+0.587*image[i][j][1]+0.299*image[i][j][2]
        image[i][j][0]=temp
        image[i][j][1]=temp
        image[i][j][2]=temp
cv2.imwrite("greyscale.png", image)
