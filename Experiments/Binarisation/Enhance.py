import cv2
import numpy as np

image = cv2.imread('nature.jpg')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

count=m*n
array=[0]*256

for i in range(m):
    for j in range(n):
        array[image[i][j][0]]+=1

for i in range(256):
    array[i]/=count

result=[]
for t in range(256):
    q1, q2, u1, u2, s1, s2 = 0, 0, 0, 0, 0, 0
    for i in range(t+1):
        q1+=array[i]
    for i in range(t+1):
        u1+=i*array[i]
    for i in range(t+1, 256):
        q2+=array[i]
    for i in range(t+1, 256):
        u2+=i*array[i]
    try:
        u1/=q1
    except:
        print('',end='')
    try:
        u2/=q2
    except:
        print('',end='')

    for i in range(t+1):
        s1+=(i-u1)**2*array[i]
    for i in range(t+1, 256):
        s2+=(i-u2)**2*array[i]

    try:
        s1/=q1
    except:
        print('',end='')
    try:
        s2/=q2
    except:
        print('',end='')
    
    value=s1*q1+s2*q2
    result.append([value, t])

threshold=min(result)[1]
for i in range(m):
    for j in range(n):
        if image[i][j][0]<=threshold:
            image[i][j][0]=0
        else:
            image[i][j][0]=255
        image[i][j][1]=image[i][j][0]
        image[i][j][2]=image[i][j][0]

cv2.imwrite("enhanced.jpg", image)