import tkinter as tk
from tkinter import messagebox
import numpy as np

def btn_click(event):
    i, j = event.widget.pst
    print(i, j)
    nbs = [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for name in event.widget.master.children:
        if event.widget.master.children[name].pst in nbs:
            toggle(event.widget.master.children[name])
    if win(event.widget.master.children):
        messagebox.showinfo('You are win')
        event.widget.master.destroy()
        newgame()

def toggle(button):
    button['bg']='yellow' if button['bg']=='black' else 'black'

def win(buttons):
    for name in buttons:
        if buttons[name]['bg']=='yellow':
            return False
    return True

def newgame(size=3, lights=[(0,1), (1,2), (2,0)]):
    frame = tk.Frame(master=window, width=size*btn_size, height=size*btn_size)
    frame.pack()
    for i in range(size): #row
        for j in range(size): #column
            button = tk.Button(master=frame, width=btn_size, height=btn_size, bg='yellow' if (i,j) in lights else 'black')
            button.place(x=j*btn_size, y=i*btn_size)
            button.pst = (i, j)
            button.bind("<Button-1>", btn_click)
    print(size,'x',size) 
    create_matrix(frame)

def create_matrix(frame):
    size = int(np.sqrt(len(frame.children)))
    A = np.zeros((size**2, size**2+1), dtype=int)
    for i in range(size):
        for j in range(size):
            nbs = [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            J = i*size+j  
            for nb in nbs:
                if 0 <= nb[0] < size and 0 <= nb[1] < size :
                    I = nb[0] * size + nb[1]
                    A[I, J] = 1
    for name in frame.children:
        if frame.children[name]['bg'] == 'yellow':
            i, j = frame.children[name].pst
            I = i*size+j
            A[I, -1] = 1
    print(A)
    print('solve')
    reduced_row_echelon_form(A)

def reduced_row_echelon_form(A):
    for c in range(A.shape[1]):
        I = -1
        for r in range(A.shape[0]):
            if A[r, c] == 1 and np.sum(A[r, :c]) == 0:
                if I < 0:
                    I = r    
        if I >= 0:
            A[[I, c], :] = A[[c, I], :] 
            for r in range(A.shape[0]):
                if c != r and A[r, c] == 1:
                    A[r, :] = A[r, :] + A[c, :]
        A[A==2] = 0
    print(A) 

btn_size = 50

if __name__ == '__main__':
    window = tk.Tk()
    newgame(size=2, lights=[(1,0)])
    window.mainloop()

