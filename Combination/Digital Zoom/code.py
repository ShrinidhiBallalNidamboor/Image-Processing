import cv2
import numpy as np

image=cv2.imread('image.png')
temp=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
zoom=3
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        temp[i][j]=0
def value(i, j, result):
    if i<0 or j<0 or i>=m or j>=n:
        return
    if temp[i][j]==0:
        temp[i][j]=1
        result.append([i, j])
def store(i, j, value):
    if i<0 or j<0 or i>=m or j>=n:
        return
    image[i][j]=value
start=[50, 50]
array=[start]
while array!=[]:
    i, j=array.pop()
    arr=[]
    value(i-2*zoom-1, j-2*zoom-1, arr)
    value(i+2*zoom+1, j+2*zoom+1, arr)
    value(i-2*zoom-1, j+2*zoom+1, arr)
    value(i+2*zoom+1, j-2*zoom-1, arr)
    value(i-2*zoom-1, j, arr)
    value(i, j-2*zoom-1, arr)
    value(i, j+2*zoom+1, arr)
    value(i+2*zoom+1, j, arr)
    for k in range(i-zoom, i+zoom+1, 1):
        for l in range(j-zoom, j+zoom+1, 1):
            store(k, l, image[i][j])
    array=array+arr
cv2.imwrite('zoom.png', image)
