import cv2
import numpy as np

kernel=np.array([[1, 1, 1], [1, 1, 1]])
image=cv2.imread('Brain.png')
temp=cv2.imread('Brain.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 50, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
image=cv2.erode(image, kernel, iterations=2)
cv2.imwrite('binary.png', image)
(number, label, values, centroid)=cv2.connectedComponentsWithStats(image, 4, cv2.CV_32S)
maximum=[0, 0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>maximum[0]:
        maximum[0]=area
        maximum[1]=i
component=(label==maximum[1]).astype("uint8")*255
component=cv2.dilate(component, kernel, iterations=2)
m=len(temp)
n=len(temp[0])
for i in range(m):
    for j in range(n):
        if component[i][j]==0:
            temp[i][j]=0
cv2.imwrite('component.png', temp)