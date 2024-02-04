import cv2
import numpy as np

image = cv2.imread('image.png')

std=0.1
size=3
kernel1=[]

for i in range(2*size+1):
    array=[]
    for j in range(2*size+1):
        array.append(0)
    kernel1.append(array)
kernel2=[]
for i in range(2*size+1):
    array=[]
    for j in range(2*size+1):
        array.append(0)
    kernel2.append(array)

count=0
for i in range(2*size+1):
    for j in range(2*size+1):
        x=i-size
        y=j-size
        kernel1[i][j]=np.exp((-x**2-y**2)/2*(std**2))/(2*3.14*(std**2))
        count+=kernel1[i][j]

for i in range(2*size+1):
    for j in range(2*size+1):
        kernel1[i][j]=kernel1[i][j]/count

std-=0.01

count=0
for i in range(2*size+1):
    for j in range(2*size+1):
        x=i-size
        y=j-size
        kernel2[i][j]=np.exp((-x**2-y**2)/2*(std**2))/(2*3.14*(std**2))
        count+=kernel2[i][j]

for i in range(2*size+1):
    for j in range(2*size+1):
        kernel2[i][j]=kernel2[i][j]/count

for i in range(2*size+1):
    for j in range(2*size+1):
        kernel1[i][j]=kernel1[i][j]-kernel2[i][j]

kernel1=np.array(kernel1)
kernel2=np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
kernel=cv2.filter2D(kernel1, -1, kernel2)
duplicate=cv2.filter2D(image, -1, kernel)

cv2.imwrite("laplacian_gaussian.png", duplicate)