import cv2
import numpy as np

full=cv2.imread('full.png')
half=cv2.imread('half.png')
quarter=cv2.imread('quarter.png')
empty=cv2.imread('emptyglass.png')

full=cv2.cvtColor(full, cv2.COLOR_BGR2GRAY)
half=cv2.cvtColor(half, cv2.COLOR_BGR2GRAY)
quarter=cv2.cvtColor(quarter, cv2.COLOR_BGR2GRAY)
empty=cv2.cvtColor(empty, cv2.COLOR_BGR2GRAY)

full=cv2.resize(full, (200, 300))
half=cv2.resize(half, (200, 300))
quarter=cv2.resize(quarter, (200, 300))
empty=cv2.resize(empty, (200, 300))

full=full-empty
half=half-empty
quarter=quarter-empty

result, full=cv2.threshold(full, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result, half=cv2.threshold(half, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result, quarter=cv2.threshold(quarter, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Opening
kernel=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
full=cv2.erode(full, kernel, iterations=5)
full=cv2.dilate(full, kernel, iterations=5)

half=cv2.erode(half, kernel, iterations=5)
half=cv2.dilate(half, kernel, iterations=5)

quarter=cv2.erode(quarter, kernel, iterations=5)
quarter=cv2.dilate(quarter, kernel, iterations=5)

(number, label, values, centroid)=cv2.connectedComponentsWithStats(full, 4, cv2.CV_32S)
maximum1=[0, 0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>maximum1[0]:
        maximum1[0]=area
        maximum1[1]=i
cv2.imwrite('binary1.png', (label==maximum1[1]).astype("uint8")*255)

(number, label, values, centroid)=cv2.connectedComponentsWithStats(half, 4, cv2.CV_32S)
maximum2=[0, 0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>maximum2[0]:
        maximum2[0]=area
        maximum2[1]=i
cv2.imwrite('binary2.png', (label==maximum2[1]).astype("uint8")*255)

(number, label, values, centroid)=cv2.connectedComponentsWithStats(quarter, 4, cv2.CV_32S)
maximum3=[0, 0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>maximum3[0]:
        maximum3[0]=area
        maximum3[1]=i
cv2.imwrite('binary3.png', (label==maximum3[1]).astype("uint8")*255)

print('Percentage half: ', np.round(maximum2[0]*100/maximum1[0]))
print('Percentage quarter: ', np.round(maximum3[0]*100/maximum1[0]))