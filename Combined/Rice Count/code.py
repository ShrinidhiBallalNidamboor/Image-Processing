import numpy as np
import cv2

image=cv2.imread('rice.png')
kernel=np.array([[1, 1], [1, 1]])
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, threshold=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
threshold=cv2.erode(threshold, kernel, iterations=1)
cv2.imwrite('binary.png', threshold)
(number, label, values, centroid)=cv2.connectedComponentsWithStats(threshold, 4, cv2.CV_32S)
for i in range(1, number):
    componentMask = (label==i).astype("uint8")*255
    cv2.imwrite('binary'+str(i)+'.png', componentMask)

print('Rice count: ', number-1)
