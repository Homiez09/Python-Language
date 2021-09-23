'''
13.เขียนโปรแกรมรับ input 1 ตัว ที่เป็นจำนวนเต็มบวก และตรวจสอบว่า รากที่สองของจำนวนที่รับมาเป็นจำนวนเต็มหรือไม่
( Hint 1: x**(1/2) = รากที่ 2 ของ x, Hint 2: ถ้า x เป็นจำนวนเต็มแล้ว x % 1 = 0 หรือไม่ )
    -ถ้าเป็นจำนวนเต็มให้พิมพ์ Yes, It's integer
    -ถ้าไม่เป็นจำนวนเต็มให้พิมพ์ No, It isn't integer
'''

number = int(input('Enter you number : '))

def rootAnswer(number):
    root = number**(1/2)
    if(root % 1 == 0):
        return "Yes, It's integer"
    else:
        return "No, It isn't integer"

print(rootAnswer(number))
