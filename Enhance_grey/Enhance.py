import cv2
import numpy as np

image = cv2.imread('grey.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

array = [0]*256
count=0

for i in range(m):
    for j in range(n):
        array[image[i][j][0]]+=1
        count+=1

for i in range(256):
    array[i]/=count
for i in range(1, 256):
    array[i]+=array[i-1]
for i in range(256):
    array[i]=i*array[i]

for i in range(m):
    for j in range(n):
        image[i][j][0]=array[image[i][j][0]]
        image[i][j][1]=array[image[i][j][1]]
        image[i][j][2]=array[image[i][j][2]]

cv2.imwrite("enhanced.png", image)