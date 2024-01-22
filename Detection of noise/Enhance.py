import cv2
import numpy as np

image = cv2.imread('Image.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

def getValue(i, j, k):
    if i<0 or j<0 or i>=m or j>=n:
        return 0
    return image[i][j][k]

hashing={}
kernel=4

for i in range(m):
    for j in range(n):
        data = []
        for a in range(i-kernel, i+kernel+1):
            for b in range(j-kernel, j+kernel+1):
                data.append(getValue(a, b, 0))
        std=np.round(np.std(data))
        try:
            hashing[std]+=1
        except:
            hashing[std]=1

array=[]
for i in hashing:
    array.append([hashing[i], i])

print(max(array)[1])
