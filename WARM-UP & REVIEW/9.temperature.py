'''
9.เขียนโปรมแกรมรับ input 1 ตัว เป็นอุณหภูมิในหน่วยฟาเรนไฮต์(Real number) และตรวจสอบว่าจำนวนที่
รับมามีค่ามากกว่าหรือน้อยกว่า 32 หรือไม่
    -ถ้ามีค่ามากกว่าหรือเท่ากับ 32 ให้คำนวณอุณหภูมิในหน่วยองศาเซลเซียส C = ( 5 *( F-32 ) ) / 9 และพิมพ์ค่าออกมา
    -ถ้ามีค่าน้อยกว่า 32 ให้พิมพ์ Too cold to live
'''

temInput = int(input('Temperature : '))
if(temInput >= 32):
    C = ( 5 *( temInput-32 ) ) / 9
    print(C)
else:
    print('Too cold to live')