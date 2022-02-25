import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

gold_counted = 'А и Б сидели на трубе'

def gold(event, c):
    b = c/1.618
    a = b/1.618
    gold_counted = "a = {}, b = {}".format(a, b)
    label2['text'] = gold_counted

label = tk.Entry(root, text="Insert length:")
label.pack()

entry = tk.Entry(width='25', bd='2')
entry.pack()
entry.focus()

butn = tk.Button(root, text=u"Расчитать золотое сечение")
butn.bind("<ButtonRelease-1>", lambda event: gold(event, float(entry.get())))
butn.pack()

label2 = tk.Label(root, text=gold_counted)
label2.pack()

root.mainloop()
