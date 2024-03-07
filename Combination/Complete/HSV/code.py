import cv2
import numpy as np

image=cv2.imread('image.png')
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        color=[image[i][j][2]/255, image[i][j][1]/255, image[i][j][0]/255]
        maximum=max(color)
        minimum=min(color)
        image[i][j][2]=maximum*255
        image[i][j][1]=(maximum-minimum)*255/maximum
        if maximum==color[0]:
            value=(0+(color[1]-color[2])/(maximum-minimum))*60
        if maximum==color[1]:
            value=(2+(color[0]-color[2])/(maximum-minimum))*60
        if maximum==color[2]:
            value=(4+(color[0]-color[1])/(maximum-minimum))*60
        if value<0:
            value+=360
        image[i][j][0]=value*255/360
image=cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
cv2.imwrite('hsv.png', image)