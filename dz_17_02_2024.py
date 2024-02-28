import tkinter as tk

def replace_text():
    global x, number_of_times_entered
    if x == 'Пайтон класний':
        x = 'Пайтон крутий'
    else:
        x = 'Пайтон класний'
    text.config(text=x)
    number_of_times_entered += 1
    update_count_label()
def update_count_label():
    number_of_times_entered_text.config(text=f'Кнопку нажато {number_of_times_entered} разів',bg='#367bb6')

x = 'пайтон клас'
number_of_times_entered = 0
font=10

root = tk.Tk()
root.geometry('400x200')
root[ 'bg' ]='#367bb6'

button1 = tk.Button(root, text='Змінити текст', width='25', height='3',font=font, command=replace_text,bg='#f49826')
button1.pack(side='left')
number_of_times_entered_text = tk.Label(text=f'Кнопку нажато {number_of_times_entered} разів',font=font,bg='#f49826')
number_of_times_entered_text.place(x=120,y=10)
text = tk.Label(text=x,font=font,bg='#f49826')
text.place(x=250,y=90)

root.mainloop()