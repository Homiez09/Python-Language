import cv2

#อ่านภาพ
img = cv2.imread("images/cat.jpg")

#กำหนดขนาด
imgResize = cv2.resize(img, (700, 500))
cv2.imshow("Output", imgResize)

#วาดวงกลม
# circle( ภาพ, ตำแหน่งจุดศูนย์กลางวงกลม (x,y), รัศมี, สี(BGR), ความหนา)
cv2.circle(imgResize, (350,250), 100, (0,0,255), 3)


cv2.imshow("Output", imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()


