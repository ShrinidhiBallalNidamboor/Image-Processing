import cv2
import numpy as np

image=cv2.imread('Brain.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, threshold=cv2.threshold(image, 50, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('binary.png', threshold)
kernel=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
threshold=cv2.erode(threshold, kernel, iterations=2)
(number, label, values, centroid)=cv2.connectedComponentsWithStats(threshold, 4, cv2.CV_32S)
maximum=[0,0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if maximum[0]<area:
        maximum[0]=area
        maximum[1]=i
component=(label==maximum[1]).astype("uint8")*255
component=cv2.dilate(component, kernel, iterations=2)
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        if component[i][j]==0:
            image[i][j]=0
cv2.imwrite('component.png', image)