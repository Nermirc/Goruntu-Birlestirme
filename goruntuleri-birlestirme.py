import cv2
import numpy as np 
#resmi içe aktar
img = cv2.imread("messi.jpg")
cv2.imshow("Messi",img)

hor = np.hstack((img,img))
cv2.imshow("Horizontal",hor)

# dikey
ver = np.vstack((img,img))
cv2.imshow("Vertical",ver)