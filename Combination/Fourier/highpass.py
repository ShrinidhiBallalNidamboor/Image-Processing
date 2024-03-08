import cv2
import numpy as np

image=cv2.imread('image.png', 0)
fourier=cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
fourier=np.fft.fftshift(fourier)
row, col=image.shape
x, y=row//2, col//2
mask=np.ones((row, col, 2), np.uint8)
neighbour=30
mask[x-neighbour:x+neighbour, y-neighbour:y+neighbour]=0
fourier=fourier*mask
fourier=np.fft.ifftshift(fourier)
fourier=cv2.idft(fourier)
image=cv2.magnitude(fourier[:,:,0], fourier[:,:,1])
maximum=0
for i in range(row):
    for j in range(col):
        maximum=max([maximum, image[i][j]])
for i in range(row):
    for j in range(col):
        image[i][j]=image[i][j]*255/maximum
cv2.imwrite('change.png', image)
