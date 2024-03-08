import cv2
import numpy as np

image=cv2.imread('image.png')
visit=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
zoom=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m=len(image)
n=len(image[0])

def get(i, j, x, y, result):
    if i<0 or j<0 or i>=m or j>=n or x<0 or y<0 or x>=m or y>=n:
        return
    if visit[x][y]==0:
        result.append([[x, y], image[i][j]])

def set(i, j, value):
    if i<0 or j<0 or i>=m or j>=n:
        return
    zoom[i][j]=value

for k in range(10):
    start=[20, 20]
    array=[[start, image[start[0]][start[1]]]]
    for i in range(m):
        for j in range(n):
            visit[i][j]=0
    while array!=[]:
        value=array.pop()
        i, j=value[0][0], value[0][1]
        visit[i][j]=1
        result=[]
        get(i-1, j-1, i-3, j-3, result)
        get(i-1, j, i-3, j, result)
        get(i+1, j-1, i+3, j-3, result)
        get(i, j-1, i, j-3, result)
        get(i+1, j, i+3, j, result)
        get(i+1, j+1, i+3, j+3, result)
        get(i+1, j, i+3, j, result)
        get(i-1, j+1, i-3, j+3, result)
        array+=result
        for p in range(i-1, i+2):
            for q in range(j-1, j+2):
                set(p, q, value[1])
    image=zoom.copy()

cv2.imwrite('zoom.png', image)