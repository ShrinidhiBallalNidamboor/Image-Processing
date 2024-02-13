import cv2
import numpy as np

image = cv2.imread('Image.png')
image = np.array(image)

m=len(image)
n=len(image[0])
o=len(image[0][0])

def getValue(i, j, k):
    if i<0 or j<0 or i>=m or j>=n:
        return 0
    return image[i][j][k]

def getGaussian(std, x, y):
    return np.exp(-(x**2+y**2)/(2*std**2))/(2*3.14*std**2)

def Gaussian(size, std):
    array=[]
    for i in range(size):
        value=[]
        for j in range(size):
            value.append(0)
        array.append(value)
    value=size//2
    for i in range(size):
        for j in range(size):
            array[i][j]=getGaussian(std, i-value, j-value)
    return array

std1=1
std2=std1-0.01

a=np.array(Gaussian(5, std1))
b=np.array(Gaussian(5, std2))
kernel=a-b

duplicate=cv2.filter2D(image, -1, kernel)
cv2.imwrite("result.png", duplicate)