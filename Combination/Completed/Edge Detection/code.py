import cv2
import numpy as np

image=cv2.imread('image.png')
temp1=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp2=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp3=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp4=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
temp5=cv2.imread('image.png')
temp6=cv2.imread('image.png')

robertsx=np.array([[1, 0], [0, -1]])
robertsy=np.array([[0, -1], [1, 0]])
prewittx=np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitty=np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
sobelx=np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobely=np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
laplacian=np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
sharpen=np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

result, temp1=cv2.threshold(np.abs(cv2.filter2D(temp1, -1, robertsx))+np.abs(cv2.filter2D(temp1, -1, robertsy)), 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result, temp2=cv2.threshold(np.abs(cv2.filter2D(temp2, -1, prewittx))+np.abs(cv2.filter2D(temp2, -1, prewitty)), 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result, temp3=cv2.threshold(np.abs(cv2.filter2D(temp3, -1, sobelx))+np.abs(cv2.filter2D(temp3, -1, sobely)), 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
temp5=cv2.filter2D(temp5, -1, sharpen)
result, temp4=cv2.threshold(cv2.filter2D(temp4, -1, laplacian), 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
temp6=cv2.Canny(temp6, 50, 80)

cv2.imwrite('roberts.png', temp1)
cv2.imwrite('prewitt.png', temp2)
cv2.imwrite('sobel.png', temp3)
cv2.imwrite('laplacian.png', temp4)
cv2.imwrite('sharpen.png', temp5)
cv2.imwrite('canny.png', temp6)