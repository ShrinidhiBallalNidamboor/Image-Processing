import cv2
import numpy as np

image=cv2.imread('image.png')
temp=cv2.imread('image.png')

temp1=cv2.imread('image.png')
temp2=cv2.imread('image.png')
temp3=cv2.imread('image.png')
temp4=cv2.imread('image.png')

canny=cv2.Canny(image, 50, 80)
cv2.imwrite('canny.png', canny)

m=len(image)
n=len(image[0])
o=len(image[0][0])

image1=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image2=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image3=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

laplacian=np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
sharpen=np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

robertsx=np.array([[1, 0], [0, -1]])
prewittx=np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
sobelx=np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

robertsy=np.array([[0, -1], [1, 0]])
prewitty=np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
sobely=np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

imagex=cv2.filter2D(image1, -1, robertsx)
imagey=cv2.filter2D(image1, -1, robertsy)
for i in range(m):
    for j in range(n):
        temp1[i][j][0]=(imagex[i][j]**2+imagey[i][j]**2)**0.5
        temp1[i][j][1]=(imagex[i][j]**2+imagey[i][j]**2)**0.5
        temp1[i][j][2]=(imagex[i][j]**2+imagey[i][j]**2)**0.5

imagex=cv2.filter2D(image2, -1, prewittx)
imagey=cv2.filter2D(image2, -1, prewitty)
for i in range(m):
    for j in range(n):
        temp2[i][j][0]=(imagex[i][j]**2+imagey[i][j]**2)**0.5
        temp2[i][j][1]=(imagex[i][j]**2+imagey[i][j]**2)**0.5
        temp2[i][j][2]=(imagex[i][j]**2+imagey[i][j]**2)**0.5

imagex=cv2.filter2D(image3, -1, sobelx)
imagey=cv2.filter2D(image3, -1, sobely)
for i in range(m):
    for j in range(n):
        temp3[i][j][0]=(imagex[i][j]**2+imagey[i][j]**2)**0.5
        temp3[i][j][1]=(imagex[i][j]**2+imagey[i][j]**2)**0.5
        temp3[i][j][2]=(imagex[i][j]**2+imagey[i][j]**2)**0.5

temp5=cv2.filter2D(temp4, -1, sharpen)
temp4=cv2.filter2D(temp4, -1, laplacian)

cv2.imwrite('roberts.png', temp1)
cv2.imwrite('prewitt.png', temp2)
cv2.imwrite('sobel.png', temp3)
cv2.imwrite('laplacian.png', temp4)
cv2.imwrite('sharpen.png', temp5)