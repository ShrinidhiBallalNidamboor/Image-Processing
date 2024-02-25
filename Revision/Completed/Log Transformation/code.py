import cv2
import numpy as np

image=cv2.imread('image.png')

m=len(image)
n=len(image[0])
o=len(image[0][0])

maximum=0
for i in range(m):
    for j in range(n):
        for k in range(o):
            if maximum<image[i][j][k]:
                maximum=image[i][j][k]

for i in range(m):
    for j in range(n):
        for k in range(o):
            image[i][j][k]=np.log(image[i][j][k]+1)*255/np.log(maximum+1)

cv2.imwrite('log.png', image)