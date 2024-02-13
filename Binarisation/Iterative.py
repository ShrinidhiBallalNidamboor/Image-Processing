import cv2
import numpy as np

image = cv2.imread('nature.jpg')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

array=[0]*256
threshold=100

def iterate(threshold):
    u1, u2, count1, count2 = 0, 0, 0, 0
    for i in range(threshold+1):
        u1+=i*array[i]
        count1+=array[i]
    for i in range(threshold+1, 256):
        u2+=i*array[i]
        count2+=array[i]
    u1=u1/count1
    u2=u2/count2
    threshold=(u1+u2)/2
    return int(np.round(threshold))

for i in range(m):
    for j in range(n):
        array[image[i][j][0]]+=1

for i in range(100):
    threshold=iterate(threshold)

for i in range(m):
    for j in range(n):
        if image[i][j][0]<=threshold:
            image[i][j][0]=0
        else:
            image[i][j][0]=255
        image[i][j][1]=image[i][j][0]
        image[i][j][2]=image[i][j][0]

cv2.imwrite("enhanced.jpg", image)