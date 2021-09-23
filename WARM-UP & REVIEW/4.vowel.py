'''
4.ให้เขียนโปรแกรม input 1 ตัว ที่เป็นอักขระ และตรวจสอบว่ามี a, e, i, o, u ในสายอักขระหรือไม่
    -ถ้ามีให้พิมพ์ There is vowel 
    -ถ้าไม่มีให้พิมพ์ There is not vowel
'''

chInput = input('Character : ')
if ( chInput == 'A' or chInput == 'a' or chInput == 'E' or chInput == 'e' or chInput == 'I' or chInput == 'i' or chInput == 'O' or chInput == 'o' or chInput == 'U' or chInput == 'u' ):
    print('There is vowel')
else:
    print('There is not vowel')
