import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m=len(image)
n=len(image[0])
maximum=0
for i in range(m):
    for j in range(n):
        if maximum<image[i][j]:
            maximum=image[i][j]
maximum=np.log(maximum+1)
for i in range(m):
    for j in range(n):
        image[i][j]=255*(np.log(image[i][j]+1)/maximum)
cv2.imwrite('log.png', image)