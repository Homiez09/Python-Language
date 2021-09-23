#รูปแบบภาพ
import cv2
img = cv2.imread("images/cat.jpg")
imgResize = cv2.resize(img, (400, 250))

#แสดงจอภาพ
cv2.imshow("Output", imgResize)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()




