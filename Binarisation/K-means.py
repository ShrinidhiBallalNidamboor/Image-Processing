import cv2
import numpy as np

image = cv2.imread('nature.jpg')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

array=[0]*256

for i in range(m):
    for j in range(n):
        array[image[i][j][0]]+=1

a=100
b=200

def k_means(a, b, array):
    p, x=0, 0
    q, y=0, 0
    for i in range(256):
        if np.abs(i-a)<=np.abs(i-b):
            p+=i*array[i]
            x+=array[i]
        else:
            q+=i*array[i]
            y+=array[i]
    return p/x, q/y
    
for i in range(10):
    a, b=k_means(a, b, array)

for i in range(m):
    for j in range(n):
        if np.abs(image[i][j][0]-a)<=np.abs(image[i][j][0]-b):
            image[i][j][0]=a
        else:
            image[i][j][0]=b
        image[i][j][1]=image[i][j][0]
        image[i][j][2]=image[i][j][0]
        
print(a, b)
cv2.imwrite("enhanced.jpg", image)