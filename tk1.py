import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

nod_info = 'Тут будет ответ на задание'

def poisk_nod(event, a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    nod = a+b
    nod_info = "NOD={}".format(nod)
    label2['text'] = nod_info

label = tk.Entry(root, width='25', bd='2')
label.pack()
label.focus()

entry = tk.Entry(width='25', bd='2')
entry.pack()
entry.focus()

butn = tk.Button(root, text=u"Расчитать НОД")
butn.bind("<ButtonRelease-1>", lambda event: poisk_nod(event, int(entry.get()), int(label.get())))
butn.pack()

label2 = tk.Label(root, text=nod_info)
label2.pack()

root.mainloop()
