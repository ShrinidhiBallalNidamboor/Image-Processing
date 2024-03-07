import cv2
import numpy as np

image = cv2.imread('grey.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

array=[0]*256

count=m*n
for i in range(m):
    for j in range(n):
        array[image[i][j][0]]+=1

for i in range(256):
    array[i]/=count
for i in range(1, 256):
    array[i]+=array[i-1]
for i in range(256):
    array[i]*=255

for i in range(m):
    for j in range(n):
        image[i][j][0]=np.floor(array[image[i][j][0]])
        image[i][j][1]=np.floor(array[image[i][j][1]])
        image[i][j][2]=np.floor(array[image[i][j][2]])

cv2.imwrite("enhanced.png", image)