import cv2
import numpy as np   

img =  cv2.imread("Data/wild-strawberries.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([30, 150, 50])
upper_red = np.array([255, 255, 180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask = mask)

kernel = np.ones((15, 15), np.float32) / 225
smoothed = cv2.filter2D(res, -1, kernel)

blur = cv2.GaussianBlur(res, (15, 15), 0)

median = cv2.medianBlur(res, 15)

bilateral = cv2.bilateralFilter(res, 15, 75, 75)


cv2.imshow('bilateralFilter', bilateral)
cv2.imwrite('Output/bilateralFilter.jpg', bilateral)

#cv2.imshow('median Blur', median)
#cv2.imwrite('Output/Median_Blur.jpg', smoothed)

#cv2.imshow('Gaussian Blurring', blur)
#cv2.imwrite('Output/gaussian_blurring.jpg', smoothed)

#cv2.imshow('Averaging', smoothed)
#cv2.imwrite('Output/blurring_smoothing.jpg', smoothed)

#cv2.imshow('img', img)
#cv2.imshow('mask', mask)
#cv2.imshow('res', res)

#cv2.imwrite('Output/strawberry_mask.jpg', mask)
#cv2.imwrite('Output/strawberry_res.jpg', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
