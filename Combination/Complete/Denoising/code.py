import cv2
import numpy as np

image=cv2.imread('image.png')
image_clear=cv2.GaussianBlur(image, (9, 9), 2)
image_average=cv2.blur(image, (3, 3))
image_nlocal=cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 2)
psnr1=cv2.PSNR(image, image_clear)
psnr2=cv2.PSNR(image, image_average)
psnr3=cv2.PSNR(image, image_nlocal)

print('Similarity is given gaussian as: ', psnr1)
print('Similarity is given averaging as: ', psnr2)
print('Similarity is given non-local as: ', psnr3)
cv2.imwrite('denoise.png', image_clear)