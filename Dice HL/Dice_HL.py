#credit by phum         7 june 2021
#github Jannnn1235

import os
import random

#You must change line 33 if you change this line.
dice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

p = 5 #set point value in game
w = 0 #This value will increase When you keep winning

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')  #mac and linux
    else:
     
        _ = os.system('cls') #window

def my_point():
    global p 
    print('point :',p,'\n')

def main(): 
    global p  
    global w
    show = random.choice(dice)
    my_point()    
    play = input('high or low\n:') #type h or l
    screen_clear()
    my_point()  
    print('dice = ',show)
    if show >= 9:
        A = 'h'
    else:
        A = 'l'

    if play == A : 
        w = w+1
        p = p+1*w
        print('\nYou are win ')
        print('+',(p/p)*w,'point\n')
    else:
        w = 0
        p = p-1
        print('You are lose\n')
        print('-',p/p,'point\n')

    x = input('if you want to leave type quit\npress enter to continue...\n:')
    if x == 'quit' or x == 'q':
        screen_clear() 
    else:
        screen_clear()  
        main()  
main()

