import cv2
import numpy as np  

img = cv2.imread('Data/kitten.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]

#print(px)

img[55, 55] = [255, 255, 255]
# print(px)

#roi = img[100:150, 100:150]
#img[100:150, 100:150] = [255, 255, 255]

kitten_face = img[37:211, 107:304]
img[0:174, 0:197] = kitten_face

#print(roi)
cv2.imshow('image', img)
#cv2.imwrite('Output/roi_white.jpg', img)
cv2.imwrite('Output/kitten_face_roi.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()