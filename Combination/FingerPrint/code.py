import cv2
import numpy as np

kernel=np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]).astype("uint8")
image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        image[i][j]=255-image[i][j]
image=image-cv2.morphologyEx(image, cv2.MORPH_HITMISS, kernel)
cv2.imwrite('fingerprint.png', image)