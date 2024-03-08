import cv2
import numpy as np

kernel=np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
for i in range(2):
    image=cv2.morphologyEx(image, cv2.MORPH_HITMISS, kernel)
cv2.imwrite('thin.png', image)