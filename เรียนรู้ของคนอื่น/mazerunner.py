import numpy as np 
from matplotlib import pyplot as plt
from tkinter import messagebox

def display(map, i, j):
    img = np.zeros((*map.shape, 3), dtype = np.uint8)   
    img[map == '#'] = [255, 200, 200]    
    img[map == '0'] = 255
    img[map == 'E'] = [0, 255, 0]
    img[i, j] = [255, 0, 0]
    plt.imshow(img)
    plt.axis('off')
    plt.pause(0.25)
    plt.cla()

def check1(a, b):
    i, j = a
    for m, n in zip([i - 1, i, i + 1, i], [j, j - 1, j, j + 1]):
        if m == b[0] and n == b[1]:
            return True
    return False

map = np.array([list('1111111111111111111'),
                list('10101000010010001E1'),
                list('1000001100000010101'),
                list('1111110001111010001'),
                list('1000110110110001111'),
                list('1110000100110101001'),
                list('1000110110100000011'),
                list('1S10100000101010001'),
                list('1111111111111111111')])

stack = []
start = np.where(map == 'S')
i, j = start[0][0], start[1][0]
display(map, i, j)
path = []
while map[i, j] != 'E':
    map[i, j] = '#'
    path.append([i, j])
    for m, n in zip([i - 1, i, i + 1, i], [j, j + 1, j, j - 1]):
        if map[m, n] == '0' or map[m, n] == 'E':
            stack.append([m, n])
    if len(stack) > 0:
        i, j = stack.pop()
    else:
        print('cannot exit')
        break
    for [I, J] in path[::-1]:
        if check1([i, j], [I, J]): break
        path.pop()
        display(map, path[-1][0], path[-1][1])
    display(map, i, j)
for i in path:
    print(i)
   
print(len(path), 'STEP TO CLOSE')
print(stack)

plt.show()
