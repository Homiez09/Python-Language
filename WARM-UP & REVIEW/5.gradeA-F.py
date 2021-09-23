'''
5.เขียนโปรแกรมรับ input 1 ตัว ที่เป็นอักขระ (A, B, C, D, F) และตรวจสอบอักขระ
    -ถ้าเป็น A ให้พิมพ์ [80, 100]
    -ถ้าเป็น B ให้พิมพ์ [70, 80)
    -ถ้าเป็น C ให้พิมพ์ [60, 70)
    -ถ้าเป็น D ให้พิมพ์ [50, 60)
    -ถ้าเป็น F ให้พิมพ์ [0, 50)
'''

gradeInput = input('Grade : ')

if(gradeInput == 'A'):
    print('[80, 100]')
if(gradeInput == 'B'):
    print('[70, 80)')
if(gradeInput == 'C'):
    print('[60, 70]')
if(gradeInput == 'D'):
    print('[50, 60)')
if(gradeInput == 'F'):
    print('[0 ,50)')
