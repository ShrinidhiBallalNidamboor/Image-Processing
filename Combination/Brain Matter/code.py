import cv2
import numpy as np

kernel=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
image=cv2.imread('Brain.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp=cv2.imread('Brain.png')
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
result1=cv2.imread('Brain.png')
result1=cv2.cvtColor(result1, cv2.COLOR_BGR2GRAY)
result2=cv2.imread('Brain.png')
result2=cv2.cvtColor(result2, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
image=cv2.erode(image, kernel, iterations=2)
(number, label, values, component)=cv2.connectedComponentsWithStats(image, 4, cv2.CV_32S)
maximum=[0, 0]
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
            temp[i][j]=0
        result1[i][j]=temp[i][j]
        result2[i][j]=temp[i][j]
cv2.imwrite('component.png', temp)
for i in range(m):
    for j in range(n):
        if temp[i][j]>150:
            result2[i][j]=0
        else:
            result1[i][j]=0
cv2.imwrite('white.png', result1)
cv2.imwrite('gray.png', result2)