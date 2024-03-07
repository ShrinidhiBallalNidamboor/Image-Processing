import cv2
import numpy as np

image=cv2.imread('image.png')
prewittx=np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitty=np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
sobelx=np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobely=np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
robertsx=np.array([[1, 0], [0, -1]])
robertsy=np.array([[0, -1], [1, 0]])
laplacian=np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
sharpen=np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

laplacian=cv2.filter2D(image, -1, laplacian)
sharpen=cv2.filter2D(image, -1, sharpen)
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

result, prewitt=cv2.threshold(np.abs(cv2.filter2D(image, -1, prewittx))+np.abs(cv2.filter2D(image, -1, prewitty)), 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result, sobel=cv2.threshold(np.abs(cv2.filter2D(image, -1, sobelx))+np.abs(cv2.filter2D(image, -1, sobely)), 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result, roberts=cv2.threshold(np.abs(cv2.filter2D(image, -1, robertsx))+np.abs(cv2.filter2D(image, -1, robertsy)), 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
canny=cv2.Canny(image, 50, 80)

cv2.imwrite('prewitt.png', prewitt)
cv2.imwrite('sobel.png', sobel)
cv2.imwrite('roberts.png', roberts)
cv2.imwrite('laplacian.png', laplacian)
cv2.imwrite('sharpen.png', sharpen)
cv2.imwrite('canny.png', canny)