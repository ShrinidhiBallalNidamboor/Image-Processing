import cv2
import numpy as np

image=cv2.imread('image.png')
kernel=cv2.imread('kernel.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel=cv2.cvtColor(kernel, cv2.COLOR_BGR2GRAY)
image=cv2.filter2D(image, -1, kernel)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('shape.png', image)