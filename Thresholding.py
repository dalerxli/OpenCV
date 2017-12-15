#THRESHOLDING /////////////////////////////////////////////
import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

#Convert into Gray color
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Now apply threshold on converted IMAGE
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

#Able to read images of low weights 
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#OTSU another kind of THRESHOLDING -- Used depending on image weights.
retval2, otsu = cv2.threshold(grayscaled, 125,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus',gaus )
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
