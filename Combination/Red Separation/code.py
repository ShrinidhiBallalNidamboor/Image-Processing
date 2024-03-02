import cv2
import numpy as np

red=cv2.imread('image.png')
green=cv2.imread('image.png')
blue=cv2.imread('image.png')
yellow=cv2.imread('image.png')
orange=cv2.imread('image.png')
pink=cv2.imread('image.png')

m=len(red)
n=len(red[0])

for i in range(m):
    for j in range(n):
        if not(red[i][j][2]>100 and red[i][j][1]<100 and red[i][j][0]<100):
            value=red[i][j][0]/3+red[i][j][1]/3+red[i][j][2]/3
            red[i][j][0], red[i][j][1], red[i][j][2]=value, value, value
            green[i][j][0], green[i][j][1], green[i][j][2]=value, value, value
            blue[i][j][0], blue[i][j][1], blue[i][j][2]=value, value, value
            yellow[i][j][0], yellow[i][j][1], yellow[i][j][2]=value, value, value
            orange[i][j][0], orange[i][j][1], orange[i][j][2]=value, value, value
            pink[i][j][0], pink[i][j][1], pink[i][j][2]=value, value, value
        else:
            green[i][j][1], green[i][j][2]=green[i][j][2], green[i][j][1]
            blue[i][j][0], blue[i][j][2]=blue[i][j][2], blue[i][j][0]
            yellow[i][j][1]=yellow[i][j][2]
            orange[i][j][1]+=20
            pink[i][j][1]=0

cv2.imwrite('red.png', red)
cv2.imwrite('green.png', green)
cv2.imwrite('blue.png', blue)
cv2.imwrite('yellow.png', yellow)
cv2.imwrite('orange.png', orange)
cv2.imwrite('pink.png', pink)
