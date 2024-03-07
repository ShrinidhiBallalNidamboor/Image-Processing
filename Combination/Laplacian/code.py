import cv2
import numpy as np

difference=1.6
image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

laplacian=np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
image1=cv2.GaussianBlur(image, (5, 5), 2)
image1=cv2.filter2D(image1, -1, laplacian)
result, image1=cv2.threshold(image1, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('border1.png', image1)

border1=cv2.GaussianBlur(image, (5, 5), 2)
border2=cv2.GaussianBlur(image, (5, 5), 2*difference)
image2=border2-border1
cv2.imwrite('border2.png', image2)