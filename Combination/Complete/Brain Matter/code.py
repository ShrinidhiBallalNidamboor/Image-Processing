import cv2
import numpy as np

kernel=np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype("uint8")
image=cv2.imread('Brain.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp=cv2.imread('Brain.png')
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
white=cv2.imread('Brain.png')
white=cv2.cvtColor(white, cv2.COLOR_BGR2GRAY)
gray=cv2.imread('Brain.png')
gray=cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

m=len(temp)
n=len(temp[0])
for i in range(m):
    for j in range(n):
        if image[i][j]>87:
            image[i][j]=255
        else:
            image[i][j]=0

#Closing
image=cv2.erode(image, kernel, iterations=1)

(number, label, values, centroid)=cv2.connectedComponentsWithStats(image, 4, cv2.CV_32S)
maximum=[0, 0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>maximum[0]:
        maximum[0]=area
        maximum[1]=i

component=(label==maximum[1]).astype("uint8")*255
image=cv2.dilate(image, kernel, iterations=1)
cv2.imwrite('binary.png', component)

for i in range(m):
    for j in range(n):
        if component[i][j]==0:
            temp[i][j]=0
cv2.imwrite('component.png', temp)

threshold=150
for i in range(m):
    for j in range(n):
        if temp[i][j]<threshold:
            white[i][j]=0
        else:
            white[i][j]=temp[i][j]

for i in range(m):
    for j in range(n):
        if temp[i][j]<threshold:
            gray[i][j]=temp[i][j]
        else:
            gray[i][j]=0

cv2.imwrite('white.png', white)
cv2.imwrite('gray.png', gray)