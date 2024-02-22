import cv2
import numpy as np

image=cv2.imread('image.png')
distance=0.0001

image1=cv2.GaussianBlur(image, (5, 5), distance)
image2=cv2.GaussianBlur(image, (5, 5), 0)

image=-image1+image2
cv2.imwrite('border1.png', image)

image=cv2.imread('image.png')

image=cv2.GaussianBlur(image, (5, 5), distance)
kernel=np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
image=cv2.filter2D(image, -1, kernel)
cv2.imwrite('border2.png', image)