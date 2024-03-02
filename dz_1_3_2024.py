#Послання пану Тарасу:
#цей код має багато недоробок, таких як деякі функції не вірно працюють, я не дуже розібрався в функці math, деколи не не працює, но думаю це не критично, тому що не робитьтільки %
#також в настройки я хоітів добавити більше но часу  трохи не вистачило, думаю в майбутньому добавлю, також після зміни теми виходить помилка, но вона не критична тому я її вирішив не фіксити, в майбутньому думаю вирішу,
#також я хоітів зробити округлі кнопки но в ткінтері так не можна, якщо придивитись то програма схожу на ту яка є в стандартному віндовсі, тому що як не дивно дизайн я скопіював звідти.
#також є кнопка очистити все, це я хотів в налаштуваннях або в основному інтерфесі добавити щоб воно записувало но час тікає

import tkinter as tk
import math

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, current)

def clear_all():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, round(result, 5))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Помилка")

def calculate_percent():
    try:
        expression = entry.get()
        operand, percentage = map(float, expression.split('%'))
        result = operand * (percentage / 100)
        entry.delete(0, tk.END)
        entry.insert(tk.END, round(result, 5))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Помилка")

def calculate_sqrt():
    try:
        expression = entry.get()
        result = math.sqrt(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, (result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Помилка")




def choose_theme(theme):
    global selected_theme
    selected_theme = theme
    print("Вибрана тема:", theme)

def confirm_theme():
    if selected_theme == "Темна":
        root.configure(bg="#383838")
        for widget in root.winfo_children():
            widget.configure(bg="#545353", fg="white", borderwidth=0, highlightthickness=0)
    elif selected_theme == "Світла":
        root.configure(bg="#ffffff")
        for widget in root.winfo_children():
            widget.configure(bg="#dddddd", fg="black", borderwidth=0, highlightthickness=0)

def show_settings():
    global selected_theme
    # Створення вікна налаштувань
    settings_window = tk.Toplevel(root)
    settings_window.title("Налаштування")
    settings_window.configure(bg="#383838")

    view_label = tk.Label(settings_window, text="Тема", font=('Arial', 14), bg="#383838", fg="white")
    view_label.grid(row=0, column=0, pady=2, columnspan=1)

    # Список
    view_options = ["Світла", "Темна"]
    view_variable = tk.StringVar(settings_window)
    view_variable.set(view_options[0])
    view_menu = tk.OptionMenu(settings_window, view_variable, *view_options)
    view_menu.config(font=('Arial', 14), bg="#545353", fg="white", borderwidth=0, highlightthickness=0)
    view_menu.grid(row=1, column=0, pady=10, columnspan=2)

    confirm_button = tk.Button(settings_window, text="Підтвердити", font=('Arial', 14), command=lambda: [choose_theme(view_variable.get()), confirm_theme(), settings_window.destroy()], bg="#545353", fg="white", borderwidth=0)
    confirm_button.grid(row=2, column=0, columnspan=2, pady=10)

    settings_window.wait_window()

#старт
root = tk.Tk()
root.title("Калькулятор")
root.configure(bg="#383838")


settings_button = tk.Button(root, text="⚙️", width=4, height=2, font=('Arial', 14), command=show_settings, borderwidth=0, bg="#545353", fg="white")
settings_button.grid(row=0, column=0, padx=1,pady=1)

entry = tk.Entry(root, width=14, font=('Arial', 20), justify='right', bd=0, state='normal', bg="#383838", fg="#ffffff")
entry.grid(row=0, column=1, columnspan=3, padx=1, pady=1)

buttons = [
    '%', '√', 'C', '⌫',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

row_val = 1
col_val = 0

button_padding = {'padx': 5, 'pady': 5}

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=4, height=2, font=('Arial', 14), command=calculate, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    elif button == 'C':
        tk.Button(root, text=button, width=4, height=2, font=('Arial', 14), command=clear_entry, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    elif button == '⌫':
        tk.Button(root, text=button, width=4, height=2, font=('Arial', 14), command=backspace, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    elif button == '':
        tk.Button(root, text=button, width=4, height=2, font=('Arial', 14), command=clear_all, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    elif button == '%':
        tk.Button(root, text=button, width=4, height=2, font=('Arial', 14), command=calculate_percent, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    elif button == '√':
        tk.Button(root, text=button, width=4, height=2, font=('Arial', 14), command=calculate_sqrt, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    else:
        tk.Button(root, text=button, width=4, height=2, font=('Arial', 14),
                  command=lambda b=button: button_click(b), borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
