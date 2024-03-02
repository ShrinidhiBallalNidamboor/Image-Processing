import cv2
import numpy as np

kernel=np.array([[1, 1], [1, 1]])
image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image1=cv2.erode(image, kernel, iterations=1)
image2=cv2.dilate(image, kernel, iterations=1)
image=image2-image1
cv2.imwrite('border.png', image)