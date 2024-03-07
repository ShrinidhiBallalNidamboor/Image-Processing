import cv2
import numpy as np

image = cv2.imread('grey.png')
image = np.array(image)
m=len(image)
n=len(image[0])
o=len(image[0][0])
kernel=1000

for i in range(kernel, m-kernel, kernel):
    for j in range(kernel, n-kernel, kernel):
        array = [0]*256
        count=0
        for a in range(i-kernel, i+kernel+1):
            for b in range(j-kernel, j+kernel+1):
                array[image[a][b][0]]+=1
                count+=1
        for a in range(256):
            array[a]/=count
        for a in range(1, 256):
            array[a]+=array[a-1]
        for a in range(256):
            array[a]=a*array[a]
        for a in range(i-kernel, i+kernel+1):
            for b in range(j-kernel, j+kernel+1):
                image[a][b][0]=array[image[a][b][0]]
                image[a][b][1]=array[image[a][b][1]]
                image[a][b][2]=array[image[a][b][2]]

cv2.imwrite("enhanced.png", image)