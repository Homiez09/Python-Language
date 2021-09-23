# Jannnn1235 (github)
# Phumrapee Soenvanichakul

import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(2) # Select your camera
cap.set(640,480) # Width and Height
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS() # FPS

listImg = os.listdir('images')
print(listImg)
imgList = [] 
for imgPath in listImg:
    img = cv2.imread(f'images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0

while True:      
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold = 0.75)

    imgStacked = cvzone.stackImages([imgOut],1,1)
    _, imgStacked = fpsReader.update(imgStacked, color=(0,0,255)) # แสดง fps 
    print(indexImg)
    cv2.imshow("Live Without BG", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList)-1:
            indexImg += 1
    elif key == ord('q'):
        break
