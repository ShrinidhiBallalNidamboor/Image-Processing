import cv2
import numpy as np

image=cv2.imread('enhance.png')
color=cv2.imread('image.png')
enhance=cv2.imread('image.png')
enhance=cv2.cvtColor(enhance, cv2.COLOR_BGR2HSV)
histogram=[]
for i in range(256):
    histogram.append([[0, 0, 0], 0])
m=len(enhance)
n=len(enhance[0])
for i in range(m):
    for j in range(n):
        histogram[enhance[i][j][1]][0][0]+=color[i][j][0]
        histogram[enhance[i][j][1]][0][1]+=color[i][j][1]
        histogram[enhance[i][j][1]][0][2]+=color[i][j][2]
        histogram[enhance[i][j][1]][1]+=1
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        try:
            image[i][j][0]=histogram[image[i][j][0]][0][0]/histogram[image[i][j][0]][1]
            image[i][j][1]=histogram[image[i][j][1]][0][1]/histogram[image[i][j][1]][1]
            image[i][j][2]=histogram[image[i][j][2]][0][2]/histogram[image[i][j][2]][1]
        except:
            print('',end='')
cv2.imwrite('color.png', image)