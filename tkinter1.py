from tkinter import *
import tkinter as tk
from tkinter import messagebox
import math

"""Нахождение НОД"""


def matNOD():
    print("Введите числа в чётном колличестве")
    val1 = entry1.get()
    val2 = entry2.get()
    # val1 = list(map(int, input('Введите первые числа: ').split()))
    # val2 = list(map(int, input('Введите вторые числа: ').split()))

    x = 0
    if len(val1) > x:
        # print(f"НОД {x + 1} пары:", math.gcd(val1[x], val2[x]))
        messagebox.showinfo(eval(f"НОД {x + 1} пары:", math.gcd(val1[x], val2[x])))
        x += 1
    else:
        pass


window = tk.Tk()
window.geometry('600x400')
window.title('Нахождение НОД')
window.resizable(width=False, height=False)

label1 = tk.Label(window, text='Введите первые числа', width=25, height=3, anchor='s')

entry1 = tk.Entry(window)

label2 = tk.Label(window, text='Введите вторые числа', width=25, height=3, anchor='s')

entry2 = tk.Entry(window)

btn = Button(window, text='Запустить', command=matNOD)

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
btn.pack()

window.mainloop()
