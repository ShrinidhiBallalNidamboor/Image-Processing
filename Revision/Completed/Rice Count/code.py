import cv2
import numpy as np

image=cv2.imread('rice.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
image=cv2.erode(image, kernel, iterations=1)
result, threshold=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('binary.png', threshold)
(number, label, values, centroid)=cv2.connectedComponentsWithStats(threshold, 4, cv2.CV_32S)

count=0
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>=20:
        component=(label==i).astype("uint8")*255
        count+=1
        cv2.imwrite('binary'+str(i)+'.png', component)

print('Number of rice grains: ', count)