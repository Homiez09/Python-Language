#ตรวจจับค่าสีด้วย Mouse
import cv2
import numpy
img = cv2.imread("images/cat.jpg")

def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x , 1]
        red = img[y, x , 2]
        imgColor = numpy.zeros([300, 300, 3], numpy.uint8) 
        imgColor[:] = [blue, green, red]
        print(blue, green, red)
        cv2.imshow("Result", imgColor)

#แสดงภาพ
cv2.imshow("Output", img)
#ทำงานกับ Mouse
cv2.setMouseCallback("Output", clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()