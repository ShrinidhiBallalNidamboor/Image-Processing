import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m=len(image)
n=len(image[0])
maximum=0
for i in range(m):
    for j in range(n):
        maximum=max([maximum, image[i][j]])
maximum=np.log2(maximum+1)
for i in range(m):
    for j in range(n):
        image[i][j]=np.log2(image[i][j]+1)*255/maximum
cv2.imwrite('log.png', image)