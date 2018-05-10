"""
Image gradients can be used to measure directional itensity, and edge detection finds the 
edge.
"""

import cv2
import numpy as np  

img = cv2.imread('Data/wild-strawberries.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([30, 150, 150])
upper_red = np.array([255, 255, 100])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask = mask)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)

cv2.imshow('img', img)
cv2.imshow('Mask', mask)
cv2.imshow('Laplacian',laplacian)
cv2.imshow('Sobelx', sobelx)
cv2.imshow('Sobely', sobely)

cv2.imwrite('Output/laplacian.jpg', laplacian)
cv2.imwrite('Output/sobelx.jpg', sobelx)
cv2.imwrite('Output/sobely.jpg', sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
