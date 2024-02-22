import numpy as np
import cv2

empty=cv2.imread('emptyglass.png')
full=cv2.imread('full.png')
half=cv2.imread('half.png')
quarter=cv2.imread('quarter.png')

empty=cv2.resize(empty, (270, 126))
full=cv2.resize(full, (270, 126))
half=cv2.resize(half, (270, 126))
quarter=cv2.resize(quarter, (270, 126))

empty=cv2.cvtColor(empty, cv2.COLOR_BGR2GRAY)
full=cv2.cvtColor(full, cv2.COLOR_BGR2GRAY)
half=cv2.cvtColor(half, cv2.COLOR_BGR2GRAY)
quarter=cv2.cvtColor(quarter, cv2.COLOR_BGR2GRAY)

area1=full-empty
area2=half-empty
area3=quarter-empty

kernel=np.array([[1, 1, 1, 1, 1], 
                 [1, 1, 1, 1, 1], 
                 [1, 1, 1, 1, 1], 
                 [1, 1, 1, 1, 1], 
                 [1, 1, 1, 1, 1]])

area1=cv2.erode(area1, kernel, iterations=2)
area2=cv2.erode(area2, kernel, iterations=2)
area3=cv2.erode(area3, kernel, iterations=2)

result1, threshold1=cv2.threshold(area1, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result2, threshold2=cv2.threshold(area2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
result3, threshold3=cv2.threshold(area3, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

(number1, label1, values1, centroid1)=cv2.connectedComponentsWithStats(threshold1, 4, cv2.CV_32S)
(number2, label2, values2, centroid2)=cv2.connectedComponentsWithStats(threshold2, 4, cv2.CV_32S)
(number3, label3, values3, centroid3)=cv2.connectedComponentsWithStats(threshold3, 4, cv2.CV_32S)

maximum1=[0, 0]
for i in range(1, number1):
    area=values1[i, cv2.CC_STAT_AREA]
    if maximum1[0]<area:
        maximum1[0]=area
        maximum1[1]=i

maximum2=[0, 0]
for i in range(1, number2):
    area=values2[i, cv2.CC_STAT_AREA]
    if maximum2[0]<area:
        maximum2[0]=area
        maximum2[1]=i

maximum3=[0, 0]
for i in range(1, number3):
    area=values3[i, cv2.CC_STAT_AREA]
    if maximum3[0]<area:
        maximum3[0]=area
        maximum3[1]=i


componentMask1=(label1==maximum1[1]).astype("uint8")*255
componentMask1=cv2.dilate(componentMask1, kernel, iterations=2)
componentMask2=(label2==maximum2[1]).astype("uint8")*255
componentMask2=cv2.dilate(componentMask2, kernel, iterations=2)
componentMask3=(label3==maximum3[1]).astype("uint8")*255
componentMask3=cv2.dilate(componentMask3, kernel, iterations=2)

cv2.imwrite('binary1.png', componentMask1)
cv2.imwrite('binary2.png', componentMask2)
cv2.imwrite('binary3.png', componentMask3)

print('Percentage filled half: ', np.round(maximum2[0]*100/maximum1[0]), '%')
print('Percentage filled quarter: ', np.round(maximum3[0]*100/maximum1[0]), '%')
