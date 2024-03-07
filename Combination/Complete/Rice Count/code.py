import cv2
import numpy as np

kernel=np.array([[1, 1], [1, 1]]).astype("uint8")
image=cv2.imread('rice.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result, image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

image=cv2.erode(image, kernel, iterations=2)
image=cv2.dilate(image, kernel, iterations=2)

(number, label, values, centroid)=cv2.connectedComponentsWithStats(image, 4, cv2.CV_32S)
count=0
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>=10:
        component=(label==i).astype("uint8")*255
        count+=1
        cv2.imwrite('binary'+str(i)+'.png', component)
print('Rice count: ', count)