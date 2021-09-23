from tkinter import *
import random

def clear():
    global expression
    global label_show_cal
    result = "0"
    expression = ""
    label_show_cal.set(result)

dice = [1,2,3,4,5,6]
show = random.choice(dice)

tk1 = Tk()
tk1.option_add("*Font", "consolas 20")
f1 = Frame(tk1, bg="green")
f1.grid(row=0, column=0, columnspan=7)
f2 = Frame(tk1, bg="red")
f2.grid(row=1, column=0)
f3 = Frame(tk1, bg="blue")
f3.grid(row=2, column=0)
Label(f1, text=show, width=25).pack(padx=10, pady=10)

Label(f2, text=show, width=25).pack(padx=10, pady=10)

Button(tk1, text="HIHG", command=lambda: press("7")).grid(row=2, column=0)
Button(tk1, text="LOW", command=lambda: press("8")).grid(row=2, column=1)
Button(tk1, text="clear", command=clear).grid(row=1, column=0, columnspan=4, sticky="news")
Button(tk1, text="QUIT", command=lambda: press("/")).grid(row=2, column=3)



tk1.mainloop()