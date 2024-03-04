import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp=cv2.imread('enhance.png')
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

histogram1=[0]*256
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        histogram1[image[i][j]]+=1
for i in range(256):
    histogram1[i]/=(m*n)
for i in range(1, 256):
    histogram1[i]+=histogram1[i-1]
for i in range(256):
    histogram1[i]=np.floor(255*histogram1[i])

histogram2=[0]*256
m=len(temp)
n=len(temp[0])
for i in range(m):
    for j in range(n):
        histogram2[temp[i][j]]+=1
for i in range(256):
    histogram2[i]/=(m*n)
for i in range(1, 256):
    histogram2[i]+=histogram2[i-1]
for i in range(256):
    histogram2[i]=np.floor(255*histogram2[i])

for i in range(256):
    minimum=[np.abs(histogram1[i]-histogram2[0]), 0]
    for j in range(1, 256):
        if minimum[0]>np.abs(histogram1[i]-histogram2[j]):
            minimum[0]=np.abs(histogram1[i]-histogram2[j])
            minimum[1]=j
    histogram1[i]=minimum[1]

m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        image[i][j]=histogram1[image[i][j]]
    
cv2.imwrite('enhanced.png', image)