import cv2
import numpy as np

image=cv2.imread('rice.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
value, threshold=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

m=len(image)
n=len(image[0])

for i in range(m):
    for j in range(n):
        if image[i][j]>=threshold[i][j]:
            image[i][j]=0
        else:
            image[i][j]=255

gray=cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.imwrite('binary.png', gray)

def pushValue(i, j, result):
    if i<0 or j<0 or i>=m or j>=n:
        return
    if image[i][j]==255:
        result.append([i, j])

def N4(i, j, result):
    pushValue(i-1, j, result)
    pushValue(i+1, j, result)
    pushValue(i, j-1, result)
    pushValue(i, j+1, result)

count=0
for i in range(m):
    for j in range(n):
        if image[i][j]==255:
            array=[[i, j]]
            size=0
            while array!=[]:
                value=array.pop()
                size+=1
                image[value[0]][value[1]]=0
                result=[]
                N4(value[0], value[1], result)
                array+=result
            if size>=100:
                count+=1

print('Number of rice components: ', count)


