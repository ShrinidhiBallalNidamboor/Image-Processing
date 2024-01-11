import cv2
import numpy as np

image = cv2.imread('image.png')
image_duplicate = cv2.imread('image_duplicate.png')
image = np.array(image)
image_duplicate = np.array(image_duplicate)
m=len(image)
n=len(image[0])
o=len(image[0][0])
for i in range(m):
    for j in range(n):
        for k in range(o):
            image_duplicate[i][j][k]=(image[i][j][k]-image_duplicate[i][j][k])%256
            image[i][j][k]=(255-image[i][j][k])%256
cv2.imwrite("reverse.png", image)
cv2.imwrite("subtraction.png", image_duplicate)