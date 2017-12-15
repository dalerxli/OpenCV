import cv2
import numpy as np

img = cv2.imread('rose.jpg', cv2.IMREAD_COLOR)

#Used to print colour of Particular region of IMAGE
img[55,55] = [255,255,255]
px = img[55,55]
print(px)

#Used to draw a square of white color on image 
img[100:150, 100:150] = [255,255,255]
px2 = img[100:150, 100:150]
print(px2)

#Used to Crop the image of particular Region i.e ROI
rose_face = img[37:111, 107:194]
img[0:74, 0:87] = rose_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

