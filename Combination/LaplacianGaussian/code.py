import cv2
import numpy as np

difference=1.6
image=cv2.imread('image.png', 0).astype("uint8")
laplacian=np.array([[0.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 0.0]])
gaussianx=np.array([[1.0], [4.0], [6.0], [4.0], [1.0]])/16
gaussiany=np.array([[1.0, 4.0, 6.0, 4.0, 1.0]])/16
gaussian=np.array(np.matrix(gaussianx)*np.matrix(gaussiany))
image1=cv2.filter2D(image, -1, gaussian)
image1=cv2.filter2D(image1, -1, laplacian)
result, image1=cv2.threshold(image1, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('border1.png', image1)

laplacian=cv2.filter2D(gaussian, -1, laplacian)
minimum=255
for i in range(5):
    for j in range(5):
        laplacian[i][j]=np.abs(laplacian[i][j])
image2=cv2.filter2D(image, -1, laplacian)
cv2.imwrite('border2.png', image2)

