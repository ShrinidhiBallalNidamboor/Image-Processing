import cv2
import numpy as np

image=cv2.imread('Image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m=len(image)
n=len(image[0])

histogram={}
neighbour=2
def get(i, j, result):
    if i<0 or j<0 or i>=m or j>=n:
        return
    result.append([i, j])

for i in range(m):
    for j in range(n):
        result=[]
        for k in range(i-2*neighbour, i+2*neighbour+1):
            for l in range(j-2*neighbour, j+2*neighbour+1):
                get(k, l, result)
        std=np.round(np.std(result))
        try:
            histogram[std]+=1
        except:
            histogram[std]=1
maximum=[0, -1]
for i in histogram:
    if histogram[i]>maximum[0]:
        maximum[0]=histogram[i]
        maximum[1]=i
image=cv2.GaussianBlur(image, (5, 5), maximum[1])
print('Standard Deviation: ', maximum[1])
cv2.imwrite('denoise.png', image)
