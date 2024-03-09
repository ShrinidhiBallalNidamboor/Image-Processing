import cv2
import numpy as np

image=cv2.imread('image.png')
kernel=cv2.imread('kernel.png')
image=cv2.matchTemplate(image, kernel, cv2.TM_CCOEFF_NORMED)
low, high, lowcord, highcord=cv2.minMaxLoc(image)
m, n=image.shape
maximum=0
for i in range(m):
    for j in range(n):
        maximum=max([maximum, image[i][j]])
for i in range(m):
    for j in range(n):
        image[i][j]=np.log2(image[i][j]+1)*255/np.log2(maximum+1)
cv2.imwrite('shape.png', image)