import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
clahe=cv2.createCLAHE(clipLimit=10)
image=clahe.apply(image)
cv2.imwrite('enhance.png', image)