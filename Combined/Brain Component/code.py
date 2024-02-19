import cv2
import numpy as np

image=cv2.imread('Brain.png')
temp=cv2.imread('Brain.png')
hsv=cv2.imread('Brain.png')

image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv=cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

m=len(image)
n=len(image[0])

for i in range(m):
    for j in range(n):
        if image[i][j]>=140:
            image[i][j]=255
        else:
            image[i][j]=0
        hsv[i][j]=image[i][j]

def pushValue(i, j, value, result):
    if i<0 or j<0 or i>=m or j>=n:
        return
    if image[i][j]==value:
        result.append([i, j])

def N4(i, j, value):
    result=[]
    pushValue(i-1, j, value, result)
    pushValue(i+1, j, value, result)
    pushValue(i, j-1, value, result)
    pushValue(i, j+1, value, result)
    return result

components=[]
for i in range(m):
    for j in range(n):
        if image[i][j]==255:
            array=[[i, j]]
            size=0
            while array!=[]:
                value=array.pop()
                size+=1
                image[value[0]][value[1]]=0
                result=N4(value[0], value[1], 255)
                array+=result
            components.append([size, [i, j]])

for i in range(m):
    for j in range(n):
        image[i][j]=hsv[i][j]

for i in range(m):
    for j in range(n):
        hsv[i][j]=0

value=max(components)
i=value[1][0]
j=value[1][1]
array=[[i, j]]
while array!=[]:
    value=array.pop()
    image[value[0]][value[1]]=0
    hsv[value[0]][value[1]]=255
    result=N4(value[0], value[1], 255)
    array+=result

hsv=cv2.cvtColor(hsv, cv2.COLOR_GRAY2BGR)
cv2.imwrite('binary.png', hsv)