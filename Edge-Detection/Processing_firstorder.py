import cv2
import numpy as np

image = cv2.imread('image.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

kernel=np.array([[1/2, 0, -1/2]])
duplicate1=cv2.filter2D(image, -1, kernel)
kernel=np.array([[1/2], [0], [-1/2]])
duplicate2=cv2.filter2D(image, -1, kernel)

for i in range(m):
    for j in range(n):
        for k in range(o):
            image[i][j][k]=(duplicate1[i][j][k]**2+duplicate2[i][j][k]**2)**0.5

cv2.imwrite("edge.png", image)