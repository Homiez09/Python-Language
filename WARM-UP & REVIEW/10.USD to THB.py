'''
10.เขียนโปรแกรมรับค่า input 1 ตัว เป็นจำนวนเงินในดอลล่าสหรัฐ (Real number) 
และตรวจสอบว่าจำนวนที่รับมามีค่ามากว่า 0 หรือไม่
    -ถ้ามีค่ามากกว่า 0 ให้คำนวณจำนวนใหม่ในหน่วยบาท (THB = USD x 32.5)
    -ถ้ามีค่าน้อยกว่าหรือเท่ากับ 0 ให้พิมพ์ You don't have money
'''

usdInput = int(input('USD : '))
if(usdInput > 0):
    THB = usdInput * 32.5
    print(THB)
else:
    print("You don't have money")