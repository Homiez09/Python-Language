'''
8.เขียนโปรแกรมรับ input 1 ตัว เป็นปีคริสต์ศักราช (จำนวนเต็ม) แบะตรวจสอบว่า จำนวนที่รับมามีค่ามากกว่าหรือเท่ากับ 0 หรือไม่
    -ถ้ามีค่ามากกว่า 0 ให้คำนวณปีพุทธศักราช(ปี ค.ศ + 543) และพิมพ์ค่าออกมา
    -ถ้ามีค่าน้อยกว่า 0 ให่พิมพ์ Please insert nuber that is greater or equal zero
'''

number = int(input('Number : '))

if (number >= 0):
    print(number+543)
else:
    print('Please insert number that is greater or equal zero')
