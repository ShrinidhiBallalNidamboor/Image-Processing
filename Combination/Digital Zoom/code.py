import cv2
import numpy as np

image=cv2.imread('image.png')
image1=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image2=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
size=3
m=len(image)
n=len(image[0])

for i in range(m):
    for j in range(n):
        temp[i][j]=0

def check(i, j, result):
    if i<0 or j<0 or i>=m or j>=n:
        return
    if temp[i][j]==0:
        temp[i][j]=1
        result.append([i, j])

def get(i, j, value):
    if i<0 or j<0 or i>=m or j>=n:
        return
    image2[i][j]=value

start=[50, 50]
array=[start]
while array!=[]:
    value=array.pop()
    stack=[]
    check(value[0]-2*size-1, value[1]-2*size-1, stack)
    check(value[0]-2*size-1, value[1]+2*size+1, stack)
    check(value[0]+2*size+1, value[1]-2*size-1, stack)
    check(value[0]+2*size+1, value[1]+2*size+1, stack)
    array+=stack
    for i in range(value[0]-2*size, value[0]+2*size+1):
        for j in range(value[1]-2*size, value[1]+2*size+1):
            get(i, j, image1[value[0]][value[1]])
cv2.imwrite('zoom.png', image2)