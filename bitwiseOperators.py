import cv2
import numpy as np

resim1=cv2.imread("1.png")
resim2=cv2.imread("2.png")

#bit_And=cv2.bitwise_and(resim1,resim2)
#bit_Or=cv2.bitwise_or(resim1,resim2)
#bit_Xor=cv2.bitwise_xor(resim1,resim2)
#bit_Not1=cv2.bitwise_not(resim1)
bit_Not2=cv2.bitwise_not(resim2)

cv2.imshow("ilk resim",resim1)
cv2.imshow("ikinci resim", resim2)
#cv2.imshow("bitwise and",bit_And)
#cv2.imshow("bitwise or",bit_Or)
#cv2.imshow("bitwise xor",bit_Xor)
#cv2.imshow("bitwise not-1",bit_Not1)
cv2.imshow("bitwise not-2",bit_Not2)

cv2.waitKey(0)
cv2.destroyAllWindows()