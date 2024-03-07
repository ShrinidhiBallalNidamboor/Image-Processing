import cv2
import numpy as np

image = cv2.imread('image.jpg')
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
        image[i][j][0]=(duplicate1[i][j][0]**2+duplicate2[i][j][0]**2)**0.5
        image[i][j][1]=(duplicate1[i][j][1]**2+duplicate2[i][j][1]**2)**0.5
        image[i][j][2]=(duplicate1[i][j][2]**2+duplicate2[i][j][2]**2)**0.5

cv2.imwrite("central.png", image)