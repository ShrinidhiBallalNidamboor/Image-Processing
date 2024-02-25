import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.GaussianBlur(image, (5, 5), 1)
laplacian=np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
image=cv2.filter2D(image, -1, laplacian)
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('border1.png', image)

difference=0.1
image=cv2.imread('image.png')
image1=cv2.GaussianBlur(image, (5, 5), 1)
image2=cv2.GaussianBlur(image, (5, 5), 1+difference)
image=image2-image1
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('border2.png', image)