import numpy as np 
import cv2

myCan = np.zeros((100,200,3), dtype="uint8")


#Note in CV it is BGR
cv2.line(myCan,(0,0),(200,100),(255,0,0),4)
cv2.imshow("My Line",myCan)
cv2.waitKey(0)