import cv2
import numpy as np

image = cv2.imread('nature.jpg')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

array=[0]*256

count=m*n
for i in range(m):
    for j in range(n):
        array[image[i][j][0]]+=1

for i in range(256):
    array[i]/=count
for i in range(1, 256):
    array[i]+=array[i-1]

thresh=[]
for t in range(256):
    q1, q2, u1, u2, s1, s2 = 0, 0, 0, 0, 0, 0 
    for i in range(t+1):
        q1+=array[i]
    for i in range(t+1):
        try:
            u1+=array[i]*i/q1
        except:
            print('',end='')
    for i in range(t+1, 256):
        q2+=array[i]
    for i in range(t+1, 256):
        try:
            u2+=array[i]*i/q2
        except:
            print('',end='')
    
    for i in range(t+1):
        try:
            s1+=array[i]*(i-u1)**2/q1
        except:
            print('',end='')
    for i in range(t+1, 256):
        try:
            s2+=array[i]*(i-u2)**2/q2
        except:
            print('',end='')

    value=q1*s1+q2*s2
    thresh.append([value, t])

threashold=min(thresh)[1]

for i in range(m):
    for j in range(n):
        if threashold>=image[i][j][0]:
            image[i][j][0]=0
        else:
            image[i][j][0]=255
        image[i][j][1]=image[i][j][0]
        image[i][j][2]=image[i][j][0]
        
cv2.imwrite("enhanced.jpg", image)