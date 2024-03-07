import cv2
import numpy as np

image = cv2.imread('Rice.png')
m=len(image)
n=len(image[0])
o=len(image[0][0])

for i in range(m):
    for j in range(n):
        if image[i][j][0]>=121:
            image[i][j][0]=255
            image[i][j][1]=255
            image[i][j][2]=255
        else:
            image[i][j][0]=0
            image[i][j][1]=0
            image[i][j][2]=0

cv2.imwrite("rice_binary.png", image)
            
def order(i, j, m, n):
    array=[[i, j]]
    count=0
    while array!=[]:
        value=array.pop()
        if value[0]<0 or value[1]<0 or value[0]>=m or value[1]>=n:
            continue
        if image[value[0]][value[1]][0]==255:
            count+=1
            image[value[0]][value[1]]=0
            array.append([value[0]-1, value[1]])
            array.append([value[0]+1, value[1]])
            array.append([value[0], value[1]-1])
            array.append([value[0], value[1]+1])
    return count

count=0
for i in range(m):
    for j in range(n):
        if image[i][j][0]==255:
            value=order(i, j, m, n)
            if value>=100:
                count+=1

print("Number of rice grains", count)
