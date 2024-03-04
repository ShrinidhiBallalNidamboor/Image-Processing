import cv2
import numpy as np

image=cv2.imread('image.png')
image=np.array(image)
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        value=[360*image[i][j][2]/255, 360*image[i][j][1]/255, 360*image[i][j][0]/255]
        result=[0, 0, 0]
        maximum=max(value)
        minimum=min(value)
        result[2]=maximum
        result[1]=(maximum-minimum)/maximum
        if maximum==value[0]:
            result[0]=0+(value[1]-value[2])/(maximum-minimum)
        if maximum==value[1]:
            result[0]=2+(value[0]-value[2])/(maximum-minimum)
        if maximum==value[2]:
            result[0]=4+(value[0]-value[1])/(maximum-minimum)
        result[0]*=60
        if result[0]<0:
            result[0]+=360
        image[i][j][0], image[i][j][1], image[i][j][2]=result[0]*255, result[1]*255, result[2]*255/360
image=cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
cv2.imwrite('hsv.png', image)