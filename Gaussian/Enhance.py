import cv2
import numpy as np

image = cv2.imread('Image.png')
image_duplicate = cv2.imread('Image.png')
image = np.array(image)
image_duplicate = np.array(image_duplicate)

m=len(image)
n=len(image[0])
o=len(image[0][0])

def getValue(i, j, k):
    if i<0 or j<0 or i>=m or j>=n:
        return 0
    return image[i][j][k]

def getGaussian(std, x, y):
    return np.exp(-(x**2+y**2)/(2*std**2))/(2*3.14*std**2)

kernel=10

for i in range(m):
    for j in range(n):
        data = []
        for a in range(i-kernel, i+kernel+1):
            for b in range(j-kernel, j+kernel+1):
                data.append(getValue(a, b, 0))
        std=np.round(np.std(data))
        value=0
        for a in range(i-kernel, i+kernel+1):
            for b in range(j-kernel, j+kernel+1):
                index=getGaussian(std, i-a, j-b)
                value+=getValue(a, b, 0)*index
        image[i][j][0]=value
        image[i][j][1]=value
        image[i][j][2]=value

cv2.imwrite("result.png", image_duplicate)