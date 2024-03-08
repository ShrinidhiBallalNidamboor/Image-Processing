import cv2
import numpy as np

kernel=np.array([[1, 1], [1, 1]]).astype("uint8")
image=cv2.imread('image.png')
value=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m=len(image)
n=len(image[0])
for i in range(m):
    for j in range(n):
        image[i][j]=255-image[i][j]
for i in range(m):
    for j in range(n):
        if image[i][j]>115:
            image[i][j]=255
        else:
            image[i][j]=0
image=cv2.erode(image, kernel, iterations=6)
cv2.imwrite('binary.png', image)
(number, label, values, centroid)=cv2.connectedComponentsWithStats(image, 4, cv2.CV_32S)
for i in range(1, number):
    if i==36 or i==40 or i==41 or i==42:
        component=(label==i).astype("uint8")
        component=cv2.dilate(component, kernel, iterations=6)
        cv2.imwrite('binary'+str(i)+'.png', component*value)