import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m, n=image.shape
kernel=90
start=[30, 30]
for i in range(start[0], m+kernel, 2*kernel):
    for j in range(start[1], n+kernel, 2*kernel):
        temp=image[max([i-kernel, 0]):min([i+kernel, m-1]),max([j-kernel, 0]):min([j+kernel, n-1])]
        temp=cv2.equalizeHist(temp)
        image[max([i-kernel, 0]):min([i+kernel, m-1]),max([j-kernel, 0]):min([j+kernel, n-1])]=temp

cv2.imwrite('binary.png', image)