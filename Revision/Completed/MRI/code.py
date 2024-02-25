import cv2
import numpy as np

image=cv2.imread('Brain.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp=cv2.imread('Brain.png')
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
result, threshold=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel=np.array([[1, 1], [1, 1]])
threshold=cv2.erode(threshold, kernel, iterations=1)
threshold=cv2.dilate(threshold, kernel, iterations=1)
cv2.imwrite('binary.png', threshold)
(number, label, values, centroid)=cv2.connectedComponentsWithStats(threshold, 4, cv2.CV_32S)
maximum=[0, 0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>maximum[0]:
        maximum[0]=area
        maximum[1]=i
component=(label==maximum[1]).astype("uint8")*255
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        if component[i][j]==0:
            temp[i][j]=0
cv2.imwrite('component.png', temp)