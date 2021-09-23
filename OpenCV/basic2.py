#แสดงผลภาพ
import cv2
img = cv2.imread("images/cat.jpg")

#แสดงจอภาพ
cv2.imshow("Output", img)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()



