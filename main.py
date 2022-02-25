import tkinter as tk
import math

"""Нахождение НОД"""
def NOD():
    a = int(input("Введите первоё число"))
    b = int(input("Введите второе число"))

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    nod = a + b

    print("НОД",nod)

def matNOD():
    print("Введите числа в чётном колличестве")
    val1 = list(map(int, input('Введите первые числа: ').split()))
    val2 = list(map(int, input('Введите вторые числа: ').split()))

    x = 0
    while True:

        if len(val1) > x:
            print(f"НОД {x+1} пары:", math.gcd(val1[x], val2[x]))
            x += 1
        else:
            break



matNOD()