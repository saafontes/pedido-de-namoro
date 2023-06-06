import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox


root = tk.Tk()
root.title('Aceita?')
root.geometry('500x500')
root.configure(background='#EBB8C1')


def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 50:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo(
        'Meu amor', 'Eu te amo meu amor, bora jogar?')


def denied():
    button_1.destroy()


margin = Canvas(root, width=500, bg='#EBB8C1', height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#EBB8C1', text='Quer namorar comigo?',
                fg='#5C053A', font=('Century Gothic', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#EBB8C1', command=denied,
                     relief=RIDGE, bd=3, font=('Century Gothic', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)
button_2 = tk.Button(root, text='Sim', bg='#EBB8C1', relief=RIDGE,
                     bd=3, command=accepted, font=('Century Gothic', 14, 'bold'))
button_2.pack()


root.mainloop()
