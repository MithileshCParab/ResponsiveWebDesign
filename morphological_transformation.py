"""
MORPHOLOGICAL TRANSFORMATION :
These are some simple operations that we perform based on umage's shape.
These tend to come in pairs. 

 1. Errosion : it is where we "erode" the edges.  The way it works is we work 
               with a slider(kernel). We give the slider a size, let's say 5 x 5 pixels.
               Then, we slide the slider around, and if all of pixels are white, then we get 
               white otherwise black. -- this may help to eliminate some white noise.

  2, Dilation : Slides around, if the enitre area ins't black, then it is converted to ehite.


"""
import cv2
import numpy as np   

img =  cv2.imread("Data/wild-strawberries.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([30, 150, 50])
upper_red = np.array([255, 255, 180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask = mask)


kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(mask, kernel, iterations = 1)
dilation = cv2.dilate(mask, kernel, iterations = 1)

cv2.imshow('Image', img)
cv2.imshow('Mask', mask)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilate', dilation)

cv2.imwrite('Output/erosion.jpg', erosion)
cv2.imwrite('Output/dilation.jpg', dilation)



cv2.waitKey(0)
cv2.destroyAllWindows()
