from numpy import *
from ast import literal_eval
import tkinter as tk
from tkinter import PhotoImage
    

def calculate():
    A = array(literal_eval(entry.get()))
    assert shape(A) == (3, 3)

    S = {
        0: [[[1,1],[1,2]], [[2,1],[2,2]]],
        1: [[[1,0],[1,2]], [[2,0],[2,2]]],
        2: [[[1,0],[1,1]], [[2,0],[2,1]]],
        3: [[[0,1],[0,2]], [[2,1],[2,2]]],
        4: [[[0,0],[0,2]], [[2,0],[2,2]]],
        5: [[[0,0],[0,1]], [[2,0],[2,1]]],
        6: [[[0,1],[0,2]], [[1,1],[1,2]]],
        7: [[[0,0],[0,2]], [[1,0],[1,2]]],
        8: [[[0,0],[0,1]], [[1,0],[1,1]]]
    }
    W = { 0 : [0,0] , 1 : [0,1] , 2 : [0,2] , 3 : [1,0] , 4 : [1,1] , 5 : [1,2] , 6 : [2,0] , 7 : [2,1] , 8 : [2,2] }
    H = [ [1,-1,1] , [-1,1,-1] , [1,-1,1] ]

    Minor_Matrix = zeros([3,3])
    x , y = 0 , 0
    for n in range(9):
        sn = S[n]
        # D = A[sn[0][0][0] , sn[0][0][1]] * A[sn[1][1][0] , sn[1][1][1]]  -  A[sn[0][1][0] , sn[0][1][1]] * A[sn[1][0][0] , sn[1][0][1]] 
        D = A[tuple(sn[0][0])] * A[tuple(sn[1][1])]  -  A[tuple(sn[1][0])] * A[tuple(sn[0][1])] 
        Minor_Matrix[x,y] = D
        y += 1
        if n in [2 , 5 ]:
            x += 1
            y = 0

    Cofactor_Matrix = multiply(Minor_Matrix , H)

    _01 , _02 , _12 = Cofactor_Matrix[0,1] , Cofactor_Matrix[0,2] , Cofactor_Matrix[1,2]
    Cofactor_Matrix[0,1] , Cofactor_Matrix[0,2] , Cofactor_Matrix[1,2] = Cofactor_Matrix[1,0] , Cofactor_Matrix[2,0] , Cofactor_Matrix[2,1]
    Cofactor_Matrix[1,0] , Cofactor_Matrix[2,0] , Cofactor_Matrix[2,1] = _01 , _02 , _12
    Adjugate_Matrix = Cofactor_Matrix

    a,b,c,d,e_,f,g,h,i = A[0][0] , A[0][1] , A[0][2] , A[1][0] , A[1][1] , A[1][2] , A[2][0] , A[2][1] , A[2][2]

    IAI = a*(e_*i - f*h) - b*(d*i - f*g) + c*(d*h - e_*g)
    if isclose(IAI, 0):
        print("The matrix is singular and has no inverse.")
    else:
        IAI = 1 / IAI
        A_1 = IAI * Adjugate_Matrix
        Output.config(text=A_1)

win = tk.Tk()
win.geometry("700x466")
win.resizable (False,False)
image_path = PhotoImage(file=r"Pictures\Wallpaper.png")
bg_image = tk.Label(win , image= image_path)
bg_image.place(relheight= 1 , relwidth= 1)
Output = tk.Label(win)

button = tk.Button(win,text="Calculate",font=100,command=calculate,bg="light green")
button.place(x= 345 , y= 50)
entry = tk.Entry(win)
entry.place(x=320, y=20)
Output.place(x=300,y=200)


win.mainloop()