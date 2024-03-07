import cv2
import numpy as np 

image = cv2.imread('image.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

for i in range(m):
    for j in range(n):
        for k in range(o):
            image[i][j][k]=32*np.log2(image[i][j][k])

cv2.imwrite('transform.png', image)