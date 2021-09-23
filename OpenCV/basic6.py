#เปิดกล้องด้วย OpenCV
import cv2

cap = cv2.VideoCapture(1)

while(True):
    check, frame = cap.read() #รับภาพจากกล้อง frame by frame  
    cv2.imshow("output", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
                               



