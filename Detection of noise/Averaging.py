import cv2
import numpy as np

image = cv2.imread('Image.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

kernel = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])
duplicate = cv2.filter2D(image, -1, kernel)

cv2.imwrite('duplicate.png', duplicate)
