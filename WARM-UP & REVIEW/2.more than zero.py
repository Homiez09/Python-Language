''' 
2. เขียนโปรแกรมรับ input 1 ตัว ที่เป็นจำนวนเต็ม และตรวจสอบว่า จำนวนที่รับมามีค่ามากกว่า 0 หรือไม่
    -ถ้ามีค่ามากกว่า 0 ให้พิมพ์ more that zero
    -ถ้ามีค่าน้อยกว่าหรือเท่ากับ 0 ให้พิมพ์ less re equal zero
'''

number = int(input('Number : '))
if(number>0):
    print('more than zero')
else:
    print('less or equal zero')