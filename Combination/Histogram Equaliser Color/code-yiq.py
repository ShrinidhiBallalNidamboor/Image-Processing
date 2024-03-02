import cv2
import numpy as np

image=cv2.imread('image.png')
temp1=cv2.imread('image.png')
temp2=cv2.imread('image.png')
temp3=cv2.imread('image.png')

image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
temp1=cv2.cvtColor(temp1, cv2.COLOR_BGR2GRAY)
temp2=cv2.cvtColor(temp2, cv2.COLOR_BGR2GRAY)
temp3=cv2.cvtColor(temp3, cv2.COLOR_BGR2GRAY)

kernel=np.matrix([[0.299, 0.587, 0.114],
    [0.59590059, -0.27455667, -0.32134392],
    [0.21153661, -0.52273617, 0.31119955]])

m=len(image)
n=len(image[0])

for i in range(m):
    for j in range(n):
        value=np.matrix([[image[i][j][0]], [image[i][j][1]], [image[i][j][2]]])
        value=kernel*value
        image[i][j][0]=value[0][0]
        image[i][j][1]=value[1][0]
        image[i][j][2]=value[2][0]
        temp1[i][j]=image[i][j][0]
        temp2[i][j]=image[i][j][1]
        temp3[i][j]=image[i][j][2]

temp1=cv2.equalizeHist(temp1)
temp2=cv2.equalizeHist(temp2)
temp3=cv2.equalizeHist(temp3)

for i in range(m):
    for j in range(n):
        image[i][j][0]=temp1[i][j]
        image[i][j][1]=temp2[i][j]
        image[i][j][2]=temp3[i][j]
        value=np.matrix([[image[i][j][0]], [image[i][j][1]], [image[i][j][2]]])
        value=kernel**-1*value
        image[i][j][0]=value[0][0]
        image[i][j][1]=value[1][0]
        image[i][j][2]=value[2][0]

image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imwrite('enhance.png', image)