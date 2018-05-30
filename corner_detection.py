import cv2
import numpy as np   

#img = cv2.imread('Data/corner_1.jpg')
#img = cv2.imread('Data/corner_2.jpeg')
img = cv2.imread('Data/corner_3.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corner', img)
#cv2.imwrite('Output/corner_detection1.jpg', img)
#cv2.imwrite('Output/corner_detection2.jpg', img)
cv2.imwrite('Output/corner_detection3.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

