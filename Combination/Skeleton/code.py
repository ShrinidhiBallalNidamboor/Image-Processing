import cv2
import numpy as np

kernel=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
for i in range(10):
    image=cv2.morphologyEx(image, cv2.MORPH_HITMISS, kernel)
cv2.imwrite('thin.png', image)