import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    #HUE SATURATION AND VALUE(hsv) 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,0,0])
    upper_red = np.array([255,255,255])

    #Mask will show image in 0 or 1(binary)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    #if pixel is in the range it will show color otherwise black
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF 
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
