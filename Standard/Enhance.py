import cv2
import numpy as np

image = cv2.imread('nature.jpg')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

kernel=np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])
value=[]
for i in range(m):
    for j in range(n):
        value.append(image[i][j][0])
print(np.std(value))
image=cv2.filter2D(image, -1, kernel)
value=[]
for i in range(m):
    for j in range(n):
        value.append(image[i][j][0])
print(np.std(value))
cv2.imwrite("enhance.jpg", image)