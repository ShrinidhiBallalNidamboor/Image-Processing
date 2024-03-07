import cv2
import numpy as np

value=cv2.imread('image.png')
temp=cv2.imread('image.png')

value=cv2.cvtColor(value, cv2.COLOR_BGR2RGB).astype("uint8")
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

kernel=np.matrix([[0.299, 0.587, 0.114],
    [0.59590059, -0.27455667, -0.32134392],
    [0.21153661, -0.52273617, 0.31119955]])

m=len(value)
n=len(value[0])

for i in range(m):
    for j in range(n):
        result=np.matrix([[value[i][j][0]], [value[i][j][1]], [value[i][j][2]]])
        result=kernel*result
        value[i][j][0]=result[0][0]
        value[i][j][1]=result[1][0]
        value[i][j][2]=result[2][0]
    
for i in range(m):
    for j in range(n):
        temp[i][j]=value[i][j][0]
temp=cv2.equalizeHist(temp)
for i in range(m):
    for j in range(n):
        value[i][j][0]=temp[i][j]

for i in range(m):
    for j in range(n):
        temp[i][j]=value[i][j][1]
temp=cv2.equalizeHist(temp)
for i in range(m):
    for j in range(n):
        value[i][j][1]=temp[i][j]

for i in range(m):
    for j in range(n):
        temp[i][j]=value[i][j][2]
temp=cv2.equalizeHist(temp)
for i in range(m):
    for j in range(n):
        value[i][j][2]=temp[i][j]

for i in range(m):
    for j in range(n):
        result=np.matrix([[value[i][j][0]], [value[i][j][1]], [value[i][j][2]]])
        result=(kernel**-1)*result
        value[i][j][0]=result[0][0]
        value[i][j][1]=result[1][0]
        value[i][j][2]=result[2][0]

image=cv2.cvtColor(value, cv2.COLOR_RGB2BGR)
cv2.imwrite('enhance.png', image)