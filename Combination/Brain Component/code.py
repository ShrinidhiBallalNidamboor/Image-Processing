import cv2
import numpy as np

image=cv2.imread('Brain.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp=cv2.imread('Brain.png')
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        if image[i][j]>90:
            image[i][j]=255
        else:
            image[i][j]=0
(number, label, values, centroid)=cv2.connectedComponentsWithStats(image, 4, cv2.CV_32S)
maximum=[0, 0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if maximum[0]<area:
        maximum[0]=area
        maximum[1]=i
component=(label==maximum[1]).astype("uint8")*255
cv2.imwrite('binary.png', component)
for i in range(m):
    for j in range(n):
        if component[i][j]==0:
            temp[i][j]=0
cv2.imwrite('component.png', temp)