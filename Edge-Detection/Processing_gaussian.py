import cv2
import numpy as np

image = cv2.imread('image.png')

std=0.1
size=3
kernel=[]
for i in range(2*size+1):
    array=[]
    for j in range(2*size+1):
        array.append(0)
    kernel.append(array)

count=0
for i in range(2*size+1):
    for j in range(2*size+1):
        x=i-size
        y=j-size
        kernel[i][j]=np.exp((-x**2-y**2)/2*(std**2))/(2*3.14*(std**2))
        count+=kernel[i][j]

for i in range(2*size+1):
    for j in range(2*size+1):
        kernel[i][j]=kernel[i][j]/count

kernel=np.array(kernel)
print(kernel)
duplicate=cv2.filter2D(image, -1, kernel)
cv2.imwrite("gaussian.png", duplicate)