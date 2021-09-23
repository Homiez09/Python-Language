'''
12.ให้เขียนโปรแกรมรับ input 1 ตัว ที่เป็นจำนวนเต็ม และตรวจสอบว่า จำนวนที่รับมามีค่ามากกว่า 0, น้อยกว่า 0, มากกว่า 0
    -ถ้ามีค่า = 0 ให้พิมพ์ zero
    -ถ้ามีค้า > 0 ให้ตรวจสอบว่าเป็นเลขคู่หรือเลขคี่
        -ถ้าเป็นเลขคู่ให้พิมพ์ Positive Even
        -ถ้าเป็นเลขคี่ให้พิมพ์ Positive Odd
    -ถ้ามีค่า < 0 ให้ตรวจสอบว่าเป็นเลขคู่หรือเลขคี่
        -ถ้าเป็นเลขคู่ให้พิมพ์ Negative Even
        -ถ้าเป็นเลขคี่ให้พิมพ์ Negative Odd
'''

number = int(input('Enter your number : '))

def positiveFunction(number):
    if(number % 2 == 0):
        return 'Positive Even'
    else:
        return 'Positive Odd'

def negativeFunction(number):
    if(number % 2 == 0):
        return 'Negative Even'
    else:
        return 'Negative Odd'

if(number == 0):
    print('zero')

if(number > 0):
    print(positiveFunction(number))

if(number < 0):
    print(negativeFunction(number))