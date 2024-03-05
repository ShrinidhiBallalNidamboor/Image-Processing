import cv2
import numpy as np

difference=1.6
image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result1=cv2.GaussianBlur(image, (7, 7), 3)
result2=cv2.GaussianBlur(image, (7, 7), 3*difference)
result=result2-result1
val, result=cv2.threshold(result, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result3=cv2.GaussianBlur(image, (7, 7), 3)
kernel=np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
image=cv2.filter2D(result3, -1, kernel)
val, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('border1.png', result)
cv2.imwrite('border2.png', image)