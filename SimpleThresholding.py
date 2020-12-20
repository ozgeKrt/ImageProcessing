import cv2

image=cv2.imread("images/image2.png",0)

ret,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("original",image)
cv2.imshow("thresh1",thresh1)
cv2.imshow("thresh2",thresh2)
cv2.imshow("thresh3",thresh3)
cv2.imshow("thresh4",thresh4)
cv2.imshow("thresh5",thresh5)


cv2.waitKey(0)
cv2.destroyAllWindows()

