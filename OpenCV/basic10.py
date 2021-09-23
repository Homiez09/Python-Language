import cv2

#อ่านภาพ
img = cv2.imread("images/cat.jpg")

#กำหนดขนาด
imgResize = cv2.resize(img, (700, 550))
cv2.imshow("Output", imgResize)

#วาดเส้นตรง
# line ( ภาพ, จุดเริ่มต้น(x,y), จุดสุดท้าย(x,y), สี(BGR), ความหนา)
cv2.arrowedLine(imgResize, (0,0), (700,550), (255,0,0), 5)
cv2.arrowedLine(imgResize, (700,0), (0,550), (0,255,0), 5)
cv2.arrowedLine(imgResize, (350,0), (350,550), (0,0,255), 5)

cv2.imshow("Output", imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()


