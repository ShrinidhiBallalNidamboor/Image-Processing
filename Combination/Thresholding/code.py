import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold=127
histogram=[0]*256
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        histogram[image[i][j]]+=1
for i in range(100):
    a=0
    b=0
    count1=0
    count2=0
    for j in range(threshold+1):
        a+=j*histogram[j]
        count1+=histogram[j]
    for j in range(threshold+1, 256):
        b+=j*histogram[j]
        count2+=histogram[j]
    a/=count1
    b/=count2
    threshold=int((a+b)//2)
for i in range(m):
    for j in range(n):
        if image[i][j]<=threshold:
            image[i][j]=0
        else:
            image[i][j]=255
cv2.imwrite('binary1.png', image)
image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
x=0
y=255
for i in range(100):
    a=0
    b=0
    count1=0
    count2=0
    for j in range(256):
        if np.abs(histogram[j]-x)<=np.abs(histogram[j]-y):
            a+=j*histogram[j]
            count1+=histogram[j]
        else:
            b+=j*histogram[j]
            count2+=histogram[j]
    x=a/count1
    y=b/count2
for i in range(m):
    for j in range(n):
        if np.abs(x-image[i][j])<=np.abs(y-image[i][j]):
            image[i][j]=x
        else:
            image[i][j]=y
cv2.imwrite('binary2.png', image)