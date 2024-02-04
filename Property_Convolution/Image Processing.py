import cv2
import numpy as np

image = cv2.imread('image.png')

m=len(image)
n=len(image[0])
o=len(image[0][0])

kernel=np.array([
    [2/7, 1/7, 0],
    [1/7, 0, 1/7],
    [0, 1/7, 1/7]
])

duplicate=cv2.filter2D(image, -1, kernel) 
cv2.imwrite("duplicate.png", duplicate)