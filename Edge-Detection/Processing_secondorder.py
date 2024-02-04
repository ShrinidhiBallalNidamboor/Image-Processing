import cv2
import numpy as np

image = cv2.imread('image.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

kernel=np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
duplicate=cv2.filter2D(image, -1, kernel)

for i in range(m):
    for j in range(n):
        for k in range(o):
            if duplicate[i][j][k]==0:
                image[i][j][k]=255
            else:
                image[i][j][k]=0

cv2.imwrite("secondorder.png", duplicate)