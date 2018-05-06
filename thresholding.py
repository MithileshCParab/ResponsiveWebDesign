import cv2 
import numpy as numpy

img = cv2.imread('Data/bookpage.jpg')
"""
A binary threshold is a simple "either" or "threshold", where the pixels are either 
255 or 0.
"""
#retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#retval, threshold = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

#th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval2, threshold2 = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)



cv2.imshow('original', img)
cv2.imshow('threshold', threshold2)
cv2.imwrite('Output/otsu_threshold.jpg', threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()