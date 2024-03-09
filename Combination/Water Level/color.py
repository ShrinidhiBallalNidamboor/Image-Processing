import cv2
import numpy as np

full=cv2.imread('half.png', 0)
half=cv2.imread('half.png', 0)
quarter=cv2.imread('quarter.png', 0)
empty=cv2.imread('empty.png', 0)

full=cv2.resize(full, (220, 500), 3)
half=cv2.resize(half, (220, 500), 3)
quarter=cv2.resize(quarter, (220, 500), 3)

m, n=full.shape
for i in range(m):
    for j in range(n):
        if full[i][j]>220:
            full[i][j]=255
        else:
            full[i][j]=0    
cv2.imwrite('binary1.png', full)