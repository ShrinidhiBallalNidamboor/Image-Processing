import cv2
import numpy as np

image = cv2.imread('Image.png')
duplicate = cv2.imread('Image.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

size=1

def get(i, j, array):
    if i<0 or j<0 or i>=m or j>=n:
        return
    array.append(image[i][j][0])

hashing={}

for i in range(m):
    for j in range(n):
        array=[]
        for a in range(i-size, i+size+1):
            for b in range(j-size, j+size+1):
                get(a, b, array)
        array=np.array(array)
        std=np.round(np.std(array))
        try:
            hashing[std]+=1
        except:
            hashing[std]=1

result=[]
for i in hashing:
    result.append([hashing[i], i])
maximum=max(result)
print(maximum[1])

