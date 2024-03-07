import cv2
import numpy as np

full=cv2.imread('full.png')
half=cv2.imread('half.png')
quarter=cv2.imread('quarter.png')
empty=cv2.imread('empty.png')

full=cv2.resize(full, (220, 500), 3)
half=cv2.resize(half, (220, 500), 3)
quarter=cv2.resize(quarter, (220, 500), 3)
empty=cv2.resize(empty, (220, 500), 3)

full=full-empty
half=half-empty
quarter=quarter-empty

full=cv2.cvtColor(full, cv2.COLOR_BGR2GRAY)
half=cv2.cvtColor(half, cv2.COLOR_BGR2GRAY)
quarter=cv2.cvtColor(quarter, cv2.COLOR_BGR2GRAY)

result, full=cv2.threshold(full, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result, half=cv2.threshold(half, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result, quarter=cv2.threshold(quarter, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]).astype("uint8")

#Opening
full=cv2.erode(full, kernel, iterations=3)
full=cv2.dilate(full, kernel, iterations=3)

half=cv2.erode(half, kernel, iterations=3)
half=cv2.dilate(half, kernel, iterations=3)

quarter=cv2.erode(quarter, kernel, iterations=3)
quarter=cv2.dilate(quarter, kernel, iterations=3)

(number, label, values, centroid)=cv2.connectedComponentsWithStats(full, 4, cv2.CV_32S)
maximum1=[0, 0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>maximum1[0]:
        maximum1[0]=area
        maximum1[1]=i
full=(label==maximum1[1]).astype("uint8")*255
(number, label, values, centroid)=cv2.connectedComponentsWithStats(half, 4, cv2.CV_32S)
maximum2=[0, 0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>maximum2[0]:
        maximum2[0]=area
        maximum2[1]=i
half=(label==maximum2[1]).astype("uint8")*255
(number, label, values, centroid)=cv2.connectedComponentsWithStats(quarter, 4, cv2.CV_32S)
maximum3=[0, 0]
for i in range(1, number):
    area=values[i, cv2.CC_STAT_AREA]
    if area>maximum3[0]:
        maximum3[0]=area
        maximum3[1]=i
quarter=(label==maximum3[1]).astype("uint8")*255

cv2.imwrite('binary1.png', full)
cv2.imwrite('binary2.png', half)
cv2.imwrite('binary3.png', quarter)

print('Percentage half: ', np.round(maximum2[0]*100/maximum1[0]))
print('Percentage quarter: ', np.round(maximum3[0]*100/maximum1[0]))