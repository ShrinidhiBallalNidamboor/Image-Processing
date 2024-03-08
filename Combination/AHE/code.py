import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
m=len(image)
n=len(image[0])
clahe=cv2.createCLAHE(clipLimit=m*n+1, tileGridSize=(7, 7))
image=clahe.apply(image)
cv2.imwrite('enhance.png', image)