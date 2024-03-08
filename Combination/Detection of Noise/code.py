import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
noise=np.random.normal(0, 10, image.shape)
image=(image+noise).astype("uint8")
histogram={}
m=len(image)
n=len(image[0])

def get(i, j, result):
    if i<0 or j<0 or i>=m or j>=n:
        return
    result.append(image[i][j])

result=[]
for i in range(m):
    for j in range(n):
        result.append(image[i][j])
std=np.std(result)
print('Noise in image: ', std)

neighbour=2
for i in range(m):
    for j in range(n):
        result=[]
        for k in range(i-neighbour, i+neighbour+1):
            for l in range(j-neighbour, j+neighbour+1):
                get(k, l, result)
        std=np.floor(np.std(result))
        try:
            histogram[std]+=1
        except:
            histogram[std]=1

maximum=[0, -1]
for i in histogram:
    if histogram[i]>maximum[0]:
        maximum[0]=histogram[i]
        maximum[1]=i

print('Sigma in the image: ', maximum[1])

image1=cv2.blur(image, (5, 5))
image2=cv2.GaussianBlur(image, (5, 5), maximum[1])

cv2.imwrite('denoise1.png', image1)
cv2.imwrite('denoise2.png', image2)