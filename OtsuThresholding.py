import cv2

image=cv2.imread("images/image2.png",0)

#simple thresholding
ret1,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

#otsu thresholding
ret2,thresh2=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("original",image)
cv2.imshow("simple threshold",thresh1)
cv2.imshow("otsu",thresh2)


cv2.waitKey(0)
cv2.destroyAllWindows()