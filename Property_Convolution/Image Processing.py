import cv2
import numpy as np

image = cv2.imread('image.png')
image = np.array(image)
scalar = 0.5

kernel=np.array([
    [2/7, 1/7, 0],
    [1/7, 0, 1/7],
    [0, 1/7, 1/7]
])

duplicate1=cv2.filter2D(scalar*image, -1, kernel) 
duplicate2=cv2.filter2D(image, -1, scalar*kernel) 

cv2.imwrite("duplicate1.png", duplicate1)
cv2.imwrite("duplicate2.png", duplicate2)