'''
11.เขียนโปรแกรมรับค่า input 1 ตัวเป็นจำนวนเงินในหน่วยบาท(Real number) และตรวจสอบว่า จำนวนที่รับมามีค่า
มากกว่า 0 หรือไม่
    -ถ้ามีค่ามากกว่า 0 ให้หาจำนวนเงินในหน่วยดอลล่าที่สามารถแลกได้ และกำไรที่ธนาคารได้ ถ้าธนาคารขายเงิน
    ดอลล่าที่ราคา 32.80 บาท (ซึ่งธนาคารจะได้กำไร 0.30 บาท) พิมพ์จำนวนเงินดอลล่าที่แลกได้ และกำไรของธนาคาร
    -ถ้ามีค่าน้อยกว่าหรือเท่ากับ 0 ให้พิมพ์ You don't have money!
'''

bath = int(input('THB : '))

def convertToUsd(bath):
    convert = bath/32.80
    return convert

def profitBank():
    profit = (bath//32.80)*0.30
    return profit


if (bath > 0):
    print("Your money is ", convertToUsd(bath), '$', 'Profit is ', profitBank(), "bath")
else:
    print("You don't have money!")