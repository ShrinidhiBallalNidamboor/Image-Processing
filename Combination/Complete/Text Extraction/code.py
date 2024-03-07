import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
clahe=cv2.createCLAHE(clipLimit=10)
image=clahe.apply(image)
cv2.imwrite('enhanced.png', image)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('binary.png', image)
