import cv2

#อ่านภาพ
img = cv2.imread("images/cat.jpg")

#กำหนดขนาด
imgResize = cv2.resize(img, (700, 500))
cv2.imshow("Output", imgResize)

#วาดข้อความบนภาพ
# putText(ภาพ, ข้อความ, พิกัดที่จะแสดงในภาพ(x,y), font, ขนาดข้อความ, สี, ความหนา)
cv2.putText(imgResize, "This is a Cat.", (150,200), 0, 1.4, (0,0,255), 3)


cv2.imshow("Output", imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()


