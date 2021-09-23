'''
15.เขียนโปรแกรมรับ input 2 ตัว ที่เป็นจำนวนเต็ม และตรวจสอบว่า ผลบวกของจำนวนทั้งสองมีค่ามากกว่า 0, น้อยกว่า 0, หรือเท่ากับ 0
    -ถ้ามีค่ามากกว่า 0 ให้ตรวจสอบว่าเป็นเลขคู่หรือไม่
        -ถ้าเป็นเลขคู่ให้พิมพ์ Positive Even
        -ถ้าเป็นเลขคี่ให้พิมพ์ Positive Odd
    -ถ้ามีค่าน้อยกว่า 0 ให้ตรวจสอบว่าเป็นเลขคู่หรือไม่
        -ถ้าเป็นเลขคู่ให้พิมพ์ Negative Even
        -ถ้าเป็นเลขคี่ให้พิมพ์ Negative Odd
    -ถ้ามีค่าเท่ากับ 0 ให้พิมพ์ Zero
'''

from datetime import datetime


def positionFunction(a, b):
    if((a + b) % 2 == 0):
        return 'Positive Even'
    else:
        return 'Positive Odd'

def negativeFunction(a, b):
    if((a + b) % 2 == 0):
        return 'Negative Even'
    else:
        return 'Negative Odd'

def main(a, b):
    if(a + b == 0):
        print('Zero')
    if(a + b > 0):
        print(positionFunction(a, b))
    if(a + b < 0):
        print(negativeFunction(a, b))

main(int(input('Input A : ')), int(input('Input B : ')))

