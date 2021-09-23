import cv2

#อ่านภาพ
img = cv2.imread("images/cat.jpg")

#กำหนดขนาด
imgResize = cv2.resize(img, (700, 500))
cv2.imshow("Output", imgResize)

#วาดสี่เหลี่ยม**
# rectangle ( ภาพ, มุมที่ 1(บนซ้าย), มุมที่ 2(ล่างขวา), สี(BGR), ความหนา)
cv2.rectangle(imgResize, (50,50), (450,450), (0,0,255), 5)


cv2.imshow("Output", imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()


