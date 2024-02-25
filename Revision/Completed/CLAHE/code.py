import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
clahe=cv2.createCLAHE(clipLimit=20)
image=clahe.apply(image)
image=cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.imwrite('enhance.png', image)