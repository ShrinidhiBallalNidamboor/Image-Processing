import cv2
import numpy as np

image=cv2.imread('image.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def addNoise(image):
    noise=np.random.normal(0, 20, image.shape)
    image=(image+noise).astype("uint8")
    cv2.imwrite('noise.png', image)
    return image

def estimatenoise(image):
    histogram={}
    m=len(image)
    n=len(image[0])

    def get(i, j, result):
        if i<0 or j<0 or i>=m or j>=n:
            return
        result.append(image[i][j])

    result=[]
    for i in range(m):
        for j in range(n):
            result.append(image[i][j])
    std=np.std(result)
    print('Noise in image: ', std)

    neighbour=2
    for i in range(m):
        for j in range(n):
            result=[]
            for k in range(i-neighbour, i+neighbour+1):
                for l in range(j-neighbour, j+neighbour+1):
                    get(k, l, result)
            std=np.round(np.std(result))
            try:
                histogram[std]+=1
            except:
                histogram[std]=1

    maximum=[0, -1]
    for i in histogram:
        if histogram[i]>maximum[0]:
            maximum[0]=histogram[i]
            maximum[1]=i

    print('Amount of noise image: ', maximum[1])

def applyfilter(image):
    difference=2**0.5
    border1=cv2.GaussianBlur(image, (5, 5), 3)
    border2=cv2.GaussianBlur(image, (5, 5), 3*difference)
    image1=border2-border1
    cv2.imwrite('border1.png', image1)

    laplacian=np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    image2=cv2.GaussianBlur(image, (5, 5), 3)
    image2=cv2.filter2D(image2, -1, laplacian)
    result, image2=cv2.threshold(image2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite('border2.png', image2)

image=addNoise(image)
estimatenoise(image)
applyfilter(image)