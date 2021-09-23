'''
6.เขียนโปรแกรมรับ input 1 ตะว ทีเ่ป็นจำนวนจริง และตรวจสอบว่า จำนวนที่่รับมามีค่ามากกว่าหรือเท่ากับ 0 หรือไม่
    -ถ้ามีค่าน้อยกว่า 0 ให้พิมพ์ Please insert the numer is greater or equal zero
    -ถ้ามีค่ามากกว่าหรือเท่ากับ 0 มห้ตรวจสอบว่าจำนวนที่รับ input มามีค่ามากกว่าหรือเท่ากับ 50 หรือไม่
    -ถ้ามีค่ามากว่าหรือเท่ากับ 50 ให้พิมพ์ pass
    -ถ้าน้อยกว่าให้พิมพ์ fail
'''

number = int(input('Number : '))

if(number >= 0):
    if(number >=50):
        print('pass')
    else:
        print('fail')
else:
    print('Please insert the number that is greater or equal zero')