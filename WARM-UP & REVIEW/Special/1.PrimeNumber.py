'''
1.ให้รับ input จากผู้ใช้แล้วตรวจสอบว่าจำนวนนั้นเป็นจำนวนเฉพาะหรือไม่ 
    -ถ้าเป็นจำนวนเฉพาะให้พิมพ์ It's prime number
    -ถ้าไม่เป็นจำนวนเฉพาะให้พิมพ์ It's not prime number
พอเช็คเสร็จให้สามารถทำต่อ หรือพิมพ์ /quit เพื่อออก
'''

def main():
    numberInput = int(input("Input your number : "))
    primeCheck(numberInput)

def primeCheck(x):
    number = []
    for i in range(1, x+1):
        if(x % i == 0):
            number.append(i)
    
    if(len(number) == 2):
        print("It's prime number")
        if(input("Press any key to continue or /quit to Exit ") == '/quit'):
            pass
        else:
            main()
    else:
        print("It's not prime number")
        if(input("Press any key to continue or /quit to Exit ") == '/quit'):
            pass
        else:
            main()


main()

