import os
from time import sleep


def screen_clear():
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      _ = os.system('cls')


def calcAnswer(item, amount):
    total = {1000 : 50, 500 : 50, 100 : 50, 50 : 50, 20 : 50, 10 : 50, 5 : 50, 2 : 50, 1 : 50}
    x = amount - item

    print('ต้องทอนทั้งหมด : ', x, 'บาท')
    print('--------------------')

    if(x>=1000):
        i = x
        i //= 1000
        if(i>=total[1000]):
            i = total[1000]
            total[1000] = total[1000] - i
            print("แบงค์ 1000 :", i, "ใบ คงเหลือ :", total[1000])
            x = x - (i*1000)
            pass
        else:
            total[1000] = total[1000] - i
            print("แบ้ง 1000 :", i, "ใบ คงเหลือ :", total[1000])
            x = x - (i*1000)
     
    if(x>=500):
        i = x
        i //= 500
        if(i>=total[500]):
            i = total[500]
            total[500] = total[500] - i
            print("แบงค์ 500 :", i, "ใบ --> คงเหลือ :", total[500])
            x = x - (i*500)
            pass
        else:
            total[500] = total[500] - i
            print("แบงค์ 500 :", i, "ใบ --> คงเหลือ :", total[500])
            x = x - (i*500)

    if(x>=100):
        i = x
        i //= 100
        if(i>=total[100]):
            i = total[100]
            total[100] = total[100] - i
            print("แบงค์ 100 :", i, "ใบ --> คงเหลือ :", total[100])
            x = x - (i*100)
            pass
        else:
            total[100] = total[100] - i
            print("แบงค์ 100 :", i, "ใบ --> คงเหลือ :", total[100])
            x = x - (i*100)
       
    if(x>=50):
        i = x
        i //= 50
        if(i>=total[50]):
            i = total[50]
            total[50] = total[50] - i
            print("แบงค์ 50 :", i, "ใบ --> คงเหลือ :", total[50])
            x = x - (i*50)
            pass
        else:
            total[50] = total[50] - i
            print("แบงค์ 50 :", i, "ใบ --> คงเหลือ :", total[50])
            x = x - (i*50)
       
    if(x>=20):
        i = x
        i //= 20
        if(i>=total[20]):
            i = total[20]
            total[20] = total[20] - i
            print("แบงค์ 20 :", i, "ใบ --> คงเหลือ :", total[20])
            x = x - (i*20)
            pass
        else:
            total[20] = total[20] - i
            print("แบงค์ 20 :", i, "ใบ --> คงเหลือ :", total[20])
            x = x - (i*20)

    if(x>=10):
        i = x
        i //= 10
        if(i>=total[10]):
            i = total[10]
            total[10] = total[10] - i
            print("เหรียญ 10 :", i, "เหรียญ --> คงเหลือ :", total[10])
            x = x - (i*10)
            pass
        else:
            total[10] = total[10] - i
            print("เหรียญ 10 :", i, "เหรียญ --> คงเหลือ :", total[10])
            x = x - (i*10)

    if(x>=5):
        i = x
        i //= 5
        if(i>=total[5]):
            i = total[5]
            total[5] = total[5] - i
            print("เหรียญ 5 :", i, "เหรียญ --> คงเหลือ :", total[5])
            x = x - (i*5)
            pass
        else:
            total[5] = total[5] - i
            print("เหรียญ 5 :", i, "เหรียญ --> คงเหลือ :", total[5])
            x = x - (i*5)

    if(x>=2):
        i = x
        i //= 2
        if(i>=total[2]):
            i = total[2]
            total[2] = total[2] - i
            print("เหรียญ 2 :", i, "เหรียญ --> คงเหลือ :", total[2])
            x = x - (i*2)
            pass
        else:
            total[2] = total[2] - i
            print("เหรียญ 2 :", i, "เหรียญ --> คงเหลือ :", total[2])
            x = x - (i*2)

    if(x>=1):
        i = x
        i //= 1
        if(i>=total[1]):
            i = total[1]
            total[1] = total[1] - i
            print("เหรียญ 1 :", i, "เหรียญ --> คงเหลือ :", total[1])
            x = x - (i*1)
            pass
        else:
            total[1] = total[1] - i
            print("เหรียญ 1 :", i, "เหรียญ --> คงเหลือ :", total[1])
            x = x - (i*1)

    print('--------------------')
    print('คงเหลือ : ', x, 'บาท')

    quitProgram = input('continue? (press anykey or quit type /quit \n --> ')
    if(quitProgram == '/quit'):
        print('closed!')
        pass
    else:  
        main() 
    
def main(): 
    screen_clear()
    inputItemPrice = int(input("ราคาของ : "))
    inputMoney = int(input("เงินลูกค้า : "))
    calcAnswer(inputItemPrice, inputMoney) 
    
main()
