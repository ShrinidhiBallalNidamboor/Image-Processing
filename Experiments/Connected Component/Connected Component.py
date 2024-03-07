import cv2
import numpy as np

image = cv2.imread('MRI.png')
temp = cv2.imread('MRI.png')
image_N4 = cv2.imread('MRI.png')
image_N8 = cv2.imread('MRI.png')

m=len(image)
n=len(image[0])
o=len(image[0][0])

hashing={}

def valid(array, x, y, m, n):
    if x<0 or y<0 or x>=m or y>=n:
        return
    if image[x][y][0]==255:
        try:
            hashing[(x, y)]
            return
        except:
            hashing[(x, y)]=1
        array.append([x, y])

for i in range(m):
    for j in range(n):
        for k in range(o):
            if temp[i][j][k]>=50:
                temp[i][j][k]=255
            else:
                temp[i][j][k]=0
            image_N4[i][j][k]=0
            image_N8[i][j][k]=0

cv2.imwrite("binary.png", temp)


for i in range(m):
    for j in range(n):
        for k in range(o):
            image[i][j][k]=temp[i][j][k]

result=[0, [0, 0]]
for i in range(m):
    for j in range(n):
        if image[i][j][0]==255:
            count=0
            hashing={}
            value=[[i, j]]
            while value!=[]:
                p=value.pop(0)
                count+=1
                image[p[0]][p[1]][0]=0
                image[p[0]][p[1]][1]=0
                image[p[0]][p[1]][2]=0
                array=[]
                valid(array, p[0]-1, p[1], m, n)
                valid(array, p[0]+1, p[1], m, n)
                valid(array, p[0], p[1]-1, m, n)
                valid(array, p[0], p[1]+1, m, n)
                for k in array:
                    value.append(k)
            if count>result[0]:
                result[0]=count
                result[1][0]=i
                result[1][1]=j

for i in range(m):
    for j in range(n):
        for k in range(o):
            image[i][j][k]=temp[i][j][k]
maximum=result
print(result[0])
value=[[maximum[1][0], maximum[1][1]]]
hashing={}
while value!=[]:
    p=value.pop(0)
    image[p[0]][p[1]][0]=0
    image[p[0]][p[1]][1]=0
    image[p[0]][p[1]][2]=0
    image_N4[p[0]][p[1]][0]=255
    image_N4[p[0]][p[1]][1]=255
    image_N4[p[0]][p[1]][2]=255
    array=[]
    valid(array, p[0]-1, p[1], m, n)
    valid(array, p[0]+1, p[1], m, n)
    valid(array, p[0], p[1]-1, m, n)
    valid(array, p[0], p[1]+1, m, n)
    for k in array:
        value.append(k)


for i in range(m):
    for j in range(n):
        for k in range(o):
            image[i][j][k]=temp[i][j][k]

result=[0, [0, 0]]
for i in range(m):
    for j in range(n):
        if image[i][j][0]==255:
            count=0
            hashing={}
            value=[[i, j]]
            while value!=[]:
                p=value.pop(0)
                count+=1
                image[p[0]][p[1]][0]=0
                image[p[0]][p[1]][1]=0
                image[p[0]][p[1]][2]=0
                array=[]
                valid(array, p[0]-1, p[1], m, n)
                valid(array, p[0]+1, p[1], m, n)
                valid(array, p[0], p[1]-1, m, n)
                valid(array, p[0], p[1]+1, m, n)
                valid(array, p[0]-1, p[1]-1, m, n)
                valid(array, p[0]-1, p[1]+1, m, n)
                valid(array, p[0]+1, p[1]-1, m, n)
                valid(array, p[0]+1, p[1]+1, m, n)
                for k in array:
                    value.append(k)
            if count>result[0]:
                result[0]=count
                result[1][0]=i
                result[1][1]=j

for i in range(m):
    for j in range(n):
        for k in range(o):
            image[i][j][k]=temp[i][j][k]
maximum=result
print(result[0])
value=[[maximum[1][0], maximum[1][1]]]
hashing={}
while value!=[]:
    p=value.pop(0)
    image[p[0]][p[1]][0]=0
    image[p[0]][p[1]][1]=0
    image[p[0]][p[1]][2]=0
    image_N8[p[0]][p[1]][0]=255
    image_N8[p[0]][p[1]][1]=255
    image_N8[p[0]][p[1]][2]=255
    array=[]
    valid(array, p[0]-1, p[1], m, n)
    valid(array, p[0]+1, p[1], m, n)
    valid(array, p[0], p[1]-1, m, n)
    valid(array, p[0], p[1]+1, m, n)
    valid(array, p[0]-1, p[1]-1, m, n)
    valid(array, p[0]-1, p[1]+1, m, n)
    valid(array, p[0]+1, p[1]-1, m, n)
    valid(array, p[0]+1, p[1]+1, m, n)
    for k in array:
        value.append(k)

cv2.imwrite("binary_N4.png", image_N4)
cv2.imwrite("binary_N8.png", image_N8)

