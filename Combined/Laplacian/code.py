import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel=np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
structural_element=np.array([[1, 1], [1, 1]])

gaussian=cv2.GaussianBlur(image, (5, 5), 2)
border1=cv2.filter2D(gaussian, -1, kernel)
result, border1=cv2.threshold(border1, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
border1=cv2.erode(border1, structural_element, iterations=1)
border1=cv2.dilate(border1, structural_element, iterations=1)
border1=cv2.erode(border1, structural_element, iterations=1)
border1=cv2.dilate(border1, structural_element, iterations=1)
cv2.imwrite('border1.png', border1)

gaussian1=cv2.GaussianBlur(image, (7, 7), 2)
gaussian2=cv2.GaussianBlur(image, (5, 5), 2)
border2=gaussian2-gaussian1
result, border2=cv2.threshold(border2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
m=len(image)
n=len(image[0])
border2=cv2.erode(border2, structural_element, iterations=1)
border2=cv2.dilate(border2, structural_element, iterations=1)
border2=cv2.erode(border2, structural_element, iterations=1)
border2=cv2.dilate(border2, structural_element, iterations=1)
cv2.imwrite('border2.png', border2)