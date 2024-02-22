import cv2
import numpy as np

image=cv2.imread('image.png')
temp=cv2.imread('image.png')

image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
temp=cv2.cvtColor(temp, cv2.COLOR_BGR2HSV)

m=len(temp)
n=len(temp[0])
o=len(temp[0][0])

for i in range(m):
    for j in range(n):
        temp[i][j][0]=temp[i][j][2]
        temp[i][j][1]=temp[i][j][2]

temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
temp=cv2.equalizeHist(temp)
temp=cv2.cvtColor(temp, cv2.COLOR_GRAY2BGR)

for i in range(m):
    for j in range(n):
        temp[i][j][0]=image[i][j][0]
        temp[i][j][1]=image[i][j][1]

temp=cv2.cvtColor(temp, cv2.COLOR_HSV2BGR)
image=cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

image=np.hstack(((temp), (image)))
image=cv2.resize(image, (1000, 600))
cv2.imwrite('enhance.png', image)