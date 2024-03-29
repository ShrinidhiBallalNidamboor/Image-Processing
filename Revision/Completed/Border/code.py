import cv2
import numpy as np

image=cv2.imread('image.png')
kernel=np.array([[1, 1], [1, 1]])
image1=cv2.dilate(image, kernel, iterations=1)
image2=cv2.erode(image, kernel, iterations=1)
image=cv2.cvtColor(image1-image2, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('border.png', image)