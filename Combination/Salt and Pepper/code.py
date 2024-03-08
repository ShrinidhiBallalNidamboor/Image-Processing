import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m=len(image)
n=len(image[0])
number=np.random.randint(50, 1000)
for i in range(number):
    x=np.random.randint(0, m-1)
    y=np.random.randint(0, n-1)
    image[x][y]=255
for i in range(number):
    x=np.random.randint(0, m-1)
    y=np.random.randint(0, n-1)
    image[x][y]=0
cv2.imwrite('noise.png', image)
image=cv2.medianBlur(image, 5)
cv2.imwrite('denoise.png', image)

maximum=0
minimum=255
for i in range(m):
    for j in range(n):
        if maximum<image[i][j]:
            maximum=image[i][j]
        if minimum>image[i][j]:
            minimum=image[i][j]
for i in range(m):
    for j in range(n):
        image[i][j]=(image[i][j]-minimum)*255/(maximum-minimum)
cv2.imwrite('enhance.png', image)