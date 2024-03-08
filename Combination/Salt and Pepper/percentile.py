import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m=len(image)
n=len(image[0])
number=np.random.randint(50, 1000)
for i in range(number):
    x=np.random.randint(0, m-1)
    y=np.random.randint(0, n-1)
    image[x][y]=255
for i in range(number):
    x=np.random.randint(0, m-1)
    y=np.random.randint(0, n-1)
    image[x][y]=0
histogram=[0]*256
for i in range(m):
    for j in range(n):
        histogram[image[i][j]]+=1
for i in range(1, 256):
    histogram[i]+=histogram[i-1]
for i in range(256):
    histogram[i]/=histogram[-1]
a=0.05
b=0.95
minimum1=[np.abs(histogram[0]-a), 0]
for i in range(256):
    if minimum1[0]>np.abs(histogram[i]-a):
        minimum1[0]=np.abs(histogram[i]-a)
        minimum1[1]=i
minimum2=[np.abs(histogram[0]-b), 0]
for i in range(256):
    if minimum2[0]>np.abs(histogram[i]-b):
        minimum2[0]=np.abs(histogram[i]-b)
        minimum2[1]=i
for i in range(256):
    histogram[i]=i
for i in range(minimum1[1]+1):
    histogram[i]=minimum1[1]
for i in range(255, minimum2[1]-1, -1):
    histogram[i]=minimum2[1]
for i in range(m):
    for j in range(n):
        image[i][j]=histogram[image[i][j]]
cv2.imwrite('denoise.png', image)

maximum=0
minimum=255
for i in range(m):
    for j in range(n):
        if maximum<image[i][j]:
            maximum=image[i][j]
        if minimum>image[i][j]:
            minimum=image[i][j]
for i in range(m):
    for j in range(n):
        image[i][j]=(image[i][j]-minimum)*255/(maximum-minimum)
image=cv2.medianBlur(image, 5)
cv2.imwrite('enhance.png', image)