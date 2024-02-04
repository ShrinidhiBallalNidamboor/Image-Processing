import cv2
import numpy as np

image = cv2.imread('image.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

kernel=np.array([
    [1/7, 1/7, 1/7],
    [1/7, 1/7, 1/7],
    [1/7, 1/7, 1/7]
])

x=len(kernel)
y=len(kernel[0])
size=x//2

a=cv2.filter2D(image, -1, kernel)
b=0
c=0

for i in range(x):
    for j in range(y):
        c+=kernel[i][j]**2

def get(i, j):
    if i<0 or j<0 or i>=m or j>=n:
        return 0
    return image[i][j][0]

maximum=0
for i in range(m):
    for j in range(n):
        for k in range(o):
            c=0
            for x in range(i-size, i+size+1):
                for y in range(j-size, j+size+1):
                    c+=get(x, y)**2
            value=b**0.5*c**0.5
            if value==0:
                image[i][j][k]=255
            else:
                image[i][j][k]=a[i][j][k]/((b**0.5)*(c**0.5))
            

cv2.imwrite("duplicate.png", image)