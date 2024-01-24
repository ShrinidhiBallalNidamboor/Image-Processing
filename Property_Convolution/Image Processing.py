import cv2
import numpy as np

image = cv2.imread('image.png')
duplicate1 = cv2.imread('image.png')
duplicate2 = cv2.imread('image.png')
subtraction = cv2.imread('subtraction.png')

image = np.array(image)
duplicate1 = np.array(duplicate1)
duplicate2 = np.array(duplicate2)
subtraction = np.array(subtraction)

m=len(image)
n=len(image[0])
o=len(image[0][0])

kernel=[
    [2/7, 1/7, 0],
    [1/7, 0, 1/7],
    [0, 1/7, 1/7]
]
size=1

def get(i, j, k, image):
    if i<0 or j<0 or i>=m or j>=n:
        return 0
    return image[i][j][k]

def convolution(i, j, image, kernel):
    value=[0, 0, 0]
    for a in range(i-size, i+size+1):
        for b in range(j-size, j+size+1):
            value[0]+=get(a, b, 0, image)*kernel[i-a+size][j-b+size]
            value[1]+=get(a, b, 1, image)*kernel[i-a+size][j-b+size]
            value[2]+=get(a, b, 2, image)*kernel[i-a+size][j-b+size]
    return value     

for i in range(m):
    for j in range(n):
        duplicate1[i][j][0]=(image[i][j][0]+subtraction[i][j][0])/2
        duplicate1[i][j][1]=(image[i][j][1]+subtraction[i][j][1])/2
        duplicate1[i][j][2]=(image[i][j][2]+subtraction[i][j][2])/2

for i in range(m):
    for j in range(n):
        value=convolution(i, j, duplicate1, kernel)
        duplicate2[i][j][0]=value[0]
        duplicate2[i][j][0]=value[0]
        duplicate2[i][j][0]=value[0]

cv2.imwrite("duplicate1.png", duplicate2)

for i in range(m):
    for j in range(n):
        value=convolution(i, j, image, kernel)
        duplicate1[i][j][0]=value[0]
        duplicate1[i][j][0]=value[0]
        duplicate1[i][j][0]=value[0]

for i in range(m):
    for j in range(n):
        value=convolution(i, j, subtraction, kernel)
        duplicate2[i][j][0]=value[0]
        duplicate2[i][j][0]=value[0]
        duplicate2[i][j][0]=value[0]

for i in range(m):
    for j in range(n):
        duplicate2[i][j][0]=(duplicate1[i][j][0]+duplicate2[i][j][0])/2
        duplicate2[i][j][1]=(duplicate1[i][j][1]+duplicate2[i][j][1])/2
        duplicate2[i][j][2]=(duplicate1[i][j][2]+duplicate2[i][j][2])/2

cv2.imwrite("duplicate2.png", duplicate2)