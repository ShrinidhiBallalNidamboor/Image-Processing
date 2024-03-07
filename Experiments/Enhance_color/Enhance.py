import cv2
import numpy as np

image = cv2.imread('nature.jpg')
image_hsv = cv2.imread('nature.jpg')

image_hsv = cv2.cvtColor(image_hsv, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image_hsv, cv2.COLOR_RGB2HSV)

image = np.array(image)
m=len(image)
n=len(image[0])
o=len(image[0][0])
array1 = [0]*256
array2 = [0]*256
array3 = [0]*256

count=m*n
for i in range(m):
    for j in range(n):
        array1[image[i][j][0]]+=1
        array2[image[i][j][1]]+=1
        array3[image[i][j][2]]+=1

for i in range(256):
    array1[i]/=count
    array2[i]/=count
    array3[i]/=count
for i in range(1, 256):
    array1[i]+=array1[i-1]
    array2[i]+=array2[i-1]
    array3[i]+=array3[i-1]
for i in range(256):
    array1[i]*=255
    array2[i]*=255
    array3[i]*=255

for i in range(m):
    for j in range(n):
        image[i][j][0]=np.floor(array1[image[i][j][0]])
        image[i][j][1]=np.floor(array2[image[i][j][1]])
        image[i][j][2]=np.floor(array3[image[i][j][2]])

array=[0]*256

count=m*n
for i in range(m):
    for j in range(n):
        array[image_hsv[i][j][2]]+=1

for i in range(256):
    array[i]/=count
for i in range(1, 256):
    array[i]+=array[i-1]
for i in range(256):
    array[i]*=255

for i in range(m):
    for j in range(n):
        image_hsv[i][j][2]=np.floor(array[image_hsv[i][j][2]])

image_hsv = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("enhanced.jpg", image)
cv2.imwrite("enhanced_hsv.jpg", image)