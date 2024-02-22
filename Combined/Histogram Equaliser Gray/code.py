import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image=cv2.equalizeHist(image)
image=cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.imwrite('enhance.png', image)