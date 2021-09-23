#การ Export ภาพ
import cv2

imgOutput = "output/output.jpg"

img = cv2.imread("images/cat.jpg", 0)
imgResize = cv2.resize(img, (400, 250))
cv2.imshow("My Cat", imgResize)

cv2.imwrite(imgOutput, imgResize)

cv2.waitKey(0)
cv2.destroyAllWindows()
