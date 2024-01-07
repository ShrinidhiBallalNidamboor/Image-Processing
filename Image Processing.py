import cv2
import numpy as np

image = cv2.imread('image.png')
image_duplicate = cv2.imread('image_duplicate.png')
image_enhanced = cv2.imread('image.png')
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
for i in range(m):
    for j in range(n):
        temp=max([image_enhanced[i][j][0], image_enhanced[i][j][1], image_enhanced[i][j][2]])
        if temp>=255/2:
            image_enhanced[i][j][0]+=40
            image_enhanced[i][j][1]+=40
            image_enhanced[i][j][2]+=40
        image_enhanced[i][j][0]*=255/295
        image_enhanced[i][j][1]*=255/295
        image_enhanced[i][j][2]*=255/295
cv2.imwrite("reverse.png", image)
cv2.imwrite("subtraction.png", image_duplicate)
cv2.imwrite("enhanced.png", image_enhanced)