import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext

def copy_text():
    try:
        lab1.config(text=en1.get('sel.first', 'sel.last'))
    except:
        pass

def insert_text():
    en1.insert('insert', lab1.cget('text'))

def clear_all():
    en1.delete('1.0', 'end')
    lab1.config(text='')

def align_text(align):
    en1.tag_configure(align, justify=align)
    en1.tag_add(align, 'insert', 'end')

root = tk.Tk()
root.geometry('420x310')

en1 = tk.scrolledtext.ScrolledText(root, font=(None, 16), height=6, width=31)
en1.place(x=10, y=20)

but1 = tk.Button(root, text='Копіювати', font=(None, 16), command=copy_text)
but1.place(x=10, y=180)
but2 = tk.Button(root, text='Вставити', font=(None, 16), command=insert_text)
but2.place(x=140, y=180)
clear_button = tk.Button(root, text='Очистити всі', font=(None, 16), command=clear_all)
clear_button.place(x=260, y=180)

lab1 = tk.Label(root, text='', font=(None, 20))
lab1.place(x=10, y=250)


label_frame = tk.LabelFrame(root, text='Вирівнювання тексту', font=(None, 14))
label_frame.place(x=170, y=240)
left_button = tk.Button(label_frame, text='Ліво', font=(None, 12), command=lambda: align_text('left'))
left_button.pack(side='left', padx=10)
center_button = tk.Button(label_frame, text='Центр', font=(None, 12), command=lambda: align_text('center'))
center_button.pack(side='left', padx=10)
right_button = tk.Button(label_frame, text='Право', font=(None, 12), command=lambda: align_text('right'))
right_button.pack(side='left', padx=10)

root.mainloop()