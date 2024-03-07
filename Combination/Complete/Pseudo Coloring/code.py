import cv2
import numpy as np

image=cv2.imread('image.png')
reference1=cv2.imread('reference.png')
reference2=cv2.cvtColor(reference1, cv2.COLOR_BGR2HSV)

m=len(reference1)
n=len(reference1[0])
array=[]
for i in range(256):
    array.append([[0, 0, 0], 0])
for i in range(m):
    for j in range(n):
        array[reference2[i][j][1]][0][0]+=reference1[i][j][0]
        array[reference2[i][j][1]][0][1]+=reference1[i][j][1]
        array[reference2[i][j][1]][0][2]+=reference1[i][j][2]
        array[reference2[i][j][1]][1]+=1
for i in range(256):
    if array[i][1]!=0:
        array[i][0][0]/=array[i][1]
        array[i][0][1]/=array[i][1]
        array[i][0][2]/=array[i][1]
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        value=image[i][j][1]
        image[i][j][0]=array[value][0][0]
        image[i][j][1]=array[value][0][1]
        image[i][j][2]=array[value][0][2]
cv2.imwrite('color.png', image)