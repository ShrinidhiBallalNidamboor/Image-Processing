import cv2
import numpy as np

image=cv2.imread('image.png', 0)
fourier=cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
fourier=np.fft.fftshift(fourier)
row, col=image.shape
x, y=row//2, col//2
mask=np.zeros((row, col, 2), np.uint8)
neighbour=30
mask[x-neighbour:x+neighbour, y-neighbour:y+neighbour]=1
fourier=fourier*mask
fourier=cv2.magnitude(fourier[:,:,0], fourier[:,:,1])
maximum=0
for i in range(row):
    for j in range(col):
        maximum=max([maximum, fourier[i][j]])
for i in range(row):
    for j in range(col):
        fourier[i][j]=np.log2(fourier[i][j]+1)*255/np.log2(maximum+1)
cv2.imwrite('mask.png', fourier)