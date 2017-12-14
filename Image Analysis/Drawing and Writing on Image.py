#DRAWING AND WRITING AN IMAGE///////////////////////////////////

import cv2
import numpy as np

img = cv2.imread('rose.jpg', cv2.IMREAD_COLOR)

#Used to make a line on IMAGE-- cv2.line(image variable, inital_point, final_pont, color, linewidth )
cv2.line(img, (0,0), (150,150), (255,255,255), 5)

#Used to make rectangle om IMAGE -- argument same as line 
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)

#Used to make Circle --- cv2.circle(image, center, radius, color, -1 used to fill the shape)
cv2.circle(img, (100,63), 55, (0,0,255), -1)

#Used to make Polygon using numpy with datatype int32
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
cv2.polylines(img, [pts], True , (0,255,255), 5)

#Used to write something on IMAGE
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV Tuts!",  (0,160), font, 1, (200, 255, 255), 5 )

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
