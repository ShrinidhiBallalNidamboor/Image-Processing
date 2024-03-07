import cv2
import numpy as np

image = cv2.imread('grey.png')

hsv = cv2.imread('nature.png')
image_hsv = cv2.imread('nature.png')

image_hsv = cv2.cvtColor(image_hsv, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image_hsv, cv2.COLOR_RGB2HSV)

image=np.array(image)
image_hsv=np.array(image_hsv)
hsv=np.array(hsv)

m=len(hsv)
n=len(hsv[0])
o=len(hsv[0][0])

array=[]
for i in range(256):
    hashing={}
    array.append([0, [0.0, 0.0]])

for i in range(m):
    for j in range(n):
        array[image_hsv[i][j][2]][0]+=1
        array[image_hsv[i][j][2]][1][0]+=image_hsv[i][j][0]
        array[image_hsv[i][j][2]][1][1]+=image_hsv[i][j][1]

for i in range(256):
    try:
        array[i][1][0]/=array[i][0]
    except:
        print('',end='')
    try:
        array[i][1][1]/=array[i][0]
    except:
        print('',end='')
    array[i][1][0]=np.floor(array[i][1][0])
    array[i][1][1]=np.floor(array[i][1][1])

m=len(image)
n=len(image[0])
o=len(image[0][0])

for i in range(m):
    for j in range(n):
        image[i][j][0]=array[image[i][j][0]][1][0]
        image[i][j][1]=array[image[i][j][0]][1][1]

print(array)

image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

cv2.imwrite("color.png", image)
