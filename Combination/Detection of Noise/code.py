import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
noise=np.random.normal(1, 10, image.shape)
image=image+noise
histogram=[0]*256
m=len(image)
n=len(image[0])

result=[]
for i in range(m):
    for j in range(n):
        result.append(image[i][j])
std=np.std(result)
print('Standard deviation in image: ', std)

def get(i, j, result):
    if i<0 or j<0 or i>=m or j>=n:
        return
    result.append(image[i][j])

neighbours=2
histogram={}
for i in range(m):
    for j in range(n):
        result=[]
        for k in range(i-2*neighbours, i+2*neighbours+1):
            for l in range(j-2*neighbours, j+2*neighbours+1):
                get(k, l, result)
        std=np.round(np.std(result))
        try:
            histogram[std]+=1
        except:
            histogram[std]=1
maximum=[0, 0]
for i in histogram:
    if histogram[i]>maximum[0]:
        maximum[0]=histogram[i]
        maximum[1]=i
print('Amount the noise: ', maximum[1])