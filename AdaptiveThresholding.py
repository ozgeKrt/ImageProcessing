import cv2
image=cv2.imread("images/image3.png",0)

image=cv2.blur(image,(3,3))

#simple thresholding
ret,thresh1=cv2.threshold(image,160,255,cv2.THRESH_BINARY)

#adaptive thresholding
thresh2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                              cv2.THRESH_BINARY,11,2)
    
thresh3=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                              cv2.THRESH_BINARY,11,2)


cv2.imshow("original",image)
cv2.imshow("simple thresholding",thresh1)
cv2.imshow("mean",thresh2)
cv2.imshow("gaussian",thresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()