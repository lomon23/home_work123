import tkinter as tk
from random import randint

def one_click():
    global remaining_attempts
    var = int(in_value.get())
    remaining_attempts -= 1

    if remaining_attempts == 0:
        out_text.config(text=f'Ви використали всі спроби. Загадане число було {number}.')
        button.config(state='disabled')
        in_value.config(state='disabled')
        restart.config(state='active')

    if var < number:
        out_text.config(text=f'Спробуй більше')
        text_try.config(text=f'ввас лишилось:{remaining_attempts} спроби')
    elif var > number:
        out_text.config(text=f'Спробуй менше')
        text_try.config(text=f'В вас залишилось:{remaining_attempts} спроби')
    else:
        out_text.config(text=f'Вгадав! Загадане число: {number}')
        text_try.config(text=f'В вас залишилось:{remaining_attempts} спроби')

    if remaining_attempts == 0:
        out_text.config(text=f'Ви використали всі спроби. Загадане число було {number}.')
        restart.config(state='active')

def update_numbers():
    global number, remaining_attempts
    remaining_attempts = 5
    min_val = int(entry_min.get())
    max_val = int(entry_max.get())
    number = randint(min_val, max_val)
    out_text.config(text='')
    button.config(state='active')
    in_value.config(state='normal')
    restart.config(state='disabled')
def restart_game():
    update_numbers()
    text_try.config(text='')
    restart.config(state='disabled')

window = tk.Tk()
window.title('Вгадай число')
window.geometry('160x320')
window[ 'bg' ]='#0F6B36'
in_text = tk.Label(text='Введіть число від 1 до 10:',bg='#0F6B36')
in_text.pack()
in_value = tk.Entry()
in_value.pack()
button = tk.Button(text='Вгадати',bg = '#074A24', command=one_click)
button.pack()


text1 = tk.Label(text='',bg='#0F6B36')
text1.pack()
text_try = tk.Label(text='',bg='#0F6B36')
text_try.pack()


text1 = tk.Label(text='',bg='#0F6B36')
text1.pack()
out_text = tk.Label(text='',bg='#0F6B36')
out_text.pack()


text = tk.Label(text='min',bg='#0F6B36')
text.pack()

entry_min = tk.Entry()
entry_min.pack()
text1 = tk.Label(text='max',bg='#0F6B36')
text1.pack()
entry_max = tk.Entry()
entry_max.pack()


update_button = tk.Button(text='Ввести числа',bg = '#074A24', command=update_numbers)
update_button.pack()
text1 = tk.Label(text='',bg='#0F6B36')
text1.pack()
restart = tk.Button(text='Почати заново?',bg = '#074A24', command=restart_game, state='disabled')
restart.pack()
remaining_attempts = 5

window.mainloop()