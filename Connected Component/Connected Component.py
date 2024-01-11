import cv2
import numpy as np

image = cv2.imread('MRI.png')
m=len(image)
n=len(image[0])
o=len(image[0][0])

for i in range(m):
    for j in range(n):
        if image[i][j][0]>=50:
            image[i][j][0]=1
            image[i][j][1]=1
            image[i][j][2]=1
        else:
            image[i][j][0]=0
            image[i][j][1]=0
            image[i][j][2]=0
            
def order(i, j, m, n, index):
    array=[[i, j]]
    count=0
    while array!=[]:
        value=array.pop()
        if value[0]<0 or value[1]<0 or value[0]>=m or value[1]>=n:
            continue
        if image[value[0]][value[1]][0]==1:
            count+=1
            image[value[0]][value[1]]=index
            array.append([value[0]-1, value[1]])
            array.append([value[0]+1, value[1]])
            array.append([value[0], value[1]-1])
            array.append([value[0], value[1]+1])
    return count

index=2
maximum=[0, 0]
for i in range(m):
    for j in range(n):
        if image[i][j][0]==1:
            value=order(i, j, m, n, index)
            if value>maximum[1]:
                maximum[1]=value
                maximum[0]=index
            index+=1
for i in range(m):
    for j in range(n):
        if image[i][j][0]==maximum[0]:
            image[i][j][0]=255
            image[i][j][1]=255
            image[i][j][2]=255
        else:
            image[i][j][0]=0
            image[i][j][1]=0
            image[i][j][2]=0
cv2.imwrite("binary.png", image)
