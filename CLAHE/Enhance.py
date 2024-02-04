import cv2
import numpy as np

image = cv2.imread('grey.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

array = [0]*256
temp = [0]*256
residual = [0]*256
count=0
limit = 500

for i in range(m):
    for j in range(n):
        array[image[i][j][0]]+=1

for i in range(256):
    if array[i]>=limit:
        temp[i]=array[i]-limit
        residual[i]=array[i]-limit
        array[i]-=limit
        count+=array[i]
for i in range(256):
    temp[i]/=count
for i in range(1, 256):
    temp[i]+=temp[i-1]
for i in range(256):
    temp[i]=int(np.floor(i*temp[i]))
for i in range(256):
    array[temp[i]]+=residual[i]
count=m*n
for i in range(256):
    array[i]/=count
for i in range(1, 256):
    array[i]+=array[i-1]
for i in range(256):
    array[i]=int(np.floor(i*array[i]))

for i in range(m):
    for j in range(n):
        image[i][j][0]=array[image[i][j][0]]
        image[i][j][1]=array[image[i][j][1]]
        image[i][j][2]=array[image[i][j][2]]

cv2.imwrite("enhanced.png", image)