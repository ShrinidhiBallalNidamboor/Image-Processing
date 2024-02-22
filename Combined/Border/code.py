import cv2
import numpy as np

image=cv2.imread('image.png')
kernel=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, threshold=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
dilate=cv2.dilate(threshold, kernel, iterations=1)
image=dilate-threshold
dilate=cv2.dilate(image, kernel, iterations=1)
cv2.imwrite('border.png', dilate)