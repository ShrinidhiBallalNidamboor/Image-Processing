import cv2
import numpy as np

array=cv2.imread('image.png')
result=cv2.imread('image.png')
temp=cv2.imread('image.png')

array=cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
image=[]
m=len(temp)
n=len(temp[0])

for i in range(m):
    value=[]
    for j in range(n):
        value.append([0, 0, 0])
    image.append(value)

for i in range(m):
    for j in range(n):
        image[i][j][0]=array[i][j][0]
        image[i][j][1]=array[i][j][1]
        image[i][j][2]=array[i][j][2]

kernel=np.matrix([[0.299, 0.587, 0.114],
                [0.59590059, -0.27455667, -0.32134392],
                [0.21153661, -0.52273617, 0.31119955]])

for i in range(m):
    for j in range(n):
        value=np.matrix([[image[i][j][0]], [image[i][j][1]], [image[i][j][2]]])
        value=kernel*value
        image[i][j][0]=value[0][0]
        image[i][j][1]=value[1][0]
        image[i][j][2]=value[2][0]

for i in range(m):
    for j in range(n):
        temp[i][j]=image[i][j][0]
temp=cv2.equalizeHist(temp)
for i in range(m):
    for j in range(n):
        image[i][j][0]=temp[i][j]

for i in range(m):
    for j in range(n):
        temp[i][j]=image[i][j][1]
temp=cv2.equalizeHist(temp)
for i in range(m):
    for j in range(n):
        image[i][j][1]=temp[i][j]

for i in range(m):
    for j in range(n):
        temp[i][j]=image[i][j][2]
temp=cv2.equalizeHist(temp)
for i in range(m):
    for j in range(n):
        image[i][j][2]=temp[i][j]

for i in range(m):
    for j in range(n):
        value=np.matrix([[image[i][j][0]], [image[i][j][1]], [image[i][j][2]]])
        value=((kernel)**-1)*value
        image[i][j][0]=value[0][0]
        image[i][j][1]=value[1][0]
        image[i][j][2]=value[2][0]

image=np.array(image)
for i in range(m):
    for j in range(n):
        result[i][j][0]=image[i][j][0]
        result[i][j][1]=image[i][j][1]
        result[i][j][2]=image[i][j][2]
result=cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
cv2.imwrite('enhance.png', result)