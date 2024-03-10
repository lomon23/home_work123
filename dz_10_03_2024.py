import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates
import math
import ast


#pip install forex_python.converter

selected_theme = "Світла"

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
        result = math.sqrt(ast.literal_eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, round(result, 5))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Помилка")

def choose_theme(event):
    global selected_theme
    selected_theme = view_variable.get()
    print("Вибрана тема:", selected_theme)
    update_themes()

def update_themes():
    if selected_theme == "Темна":
        root.configure(bg="#383838")
        settings_window.configure(bg="#383838")
        entry.configure(bg="#383838", fg="#ffffff")
        for widget in root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#545353", fg="white")
    elif selected_theme == "Світла":
        root.configure(bg="#ffffff")
        settings_window.configure(bg="#ffffff")
        entry.configure(bg="#ffffff", fg="#000000")
        for widget in root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#dddddd", fg="#000000")


def show_settings():
    global selected_theme
    global settings_window

    if 'settings_window' in globals() and settings_window.winfo_exists():
        settings_window.deiconify()
        return

    settings_window = tk.Toplevel(root)
    settings_window.title("Налаштування")
    settings_window.configure(bg="#383838")
    settings_window.geometry('230x390')

    settings_button = tk.Button(settings_window, text="⚙️", width=6, height=2, font=('Arial', 14),
                                command=exit_settings, borderwidth=0, bg="#545353", fg="white")
    settings_button.grid(row=0, column=0, padx=1, pady=1, sticky='w')

    view_options = ["Світла", "Темна"]
    global view_variable
    view_variable = tk.StringVar(settings_window)
    view_variable.set(selected_theme)

    view_combobox = ttk.Combobox(settings_window, values=view_options, textvariable=view_variable, font=('Arial', 14), state='readonly')
    view_combobox.bind("<<ComboboxSelected>>", choose_theme)
    view_combobox.set("Тема")
    view_combobox.grid(row=1, column=0, pady=3, padx=10)

    currency_button = tk.Button(settings_window, text="Валюта", width=10, height=2, font=('Arial', 12),
                                borderwidth=0, bg="#545353", fg="white", command=open_currency_window)
    currency_button.grid(row=2, column=0, padx=1, pady=1, sticky='w')  # Нова кнопка "Валюта"

    settings_window.geometry(f'+{root.winfo_x()}+{root.winfo_y()}')

    settings_window.protocol("WM_DELETE_WINDOW", lambda: settings_window.iconify())
    settings_window.mainloop()


def open_currency_window():
    global currency_window

    if 'currency_window' in globals() and currency_window.winfo_exists():
        currency_window.deiconify()
        return

    def convert_currency(event=None):
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()

        currency_rates = CurrencyRates()
        exchange_rate = currency_rates.get_rate(from_currency, to_currency)
        result = round(amount * exchange_rate, 2)

        label_result.config(text=f"Результат: {result} {to_currency}")

    def exit_window():
        currency_window.destroy()

    currency_window = tk.Toplevel(root)
    currency_window.title("Вибір валюти")
    currency_window.geometry('295x390')
    currency_window.configure(bg="#383838")

    x = root.winfo_x()
    y = root.winfo_y()

    currency_window.geometry(f'+{x - currency_window.winfo_width()}+{y}')

    settings_label = tk.Label(currency_window, text="Валютний калькулятор", font=("Helvetica", 14),bg="#383838", fg="#ffffff", bd=0)
    settings_label.grid(row=0, column=0, padx=10, pady=10)

    exit = tk.Button(currency_window, text='⚙️', command=exit_window, bg="#545353", fg="#ffffff", bd=0)
    exit.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entry_amount = tk.Entry(currency_window, font=("Helvetica", 18), width=20, bg="#545353", fg="#ffffff", bd=0)
    entry_amount.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    entry_amount.bind("<Return>", convert_currency)

    currencies = ["USD", "EUR", "GBP", "JPY"]
    combo_from = tk.StringVar()
    combo_from.set(currencies[0])
    combo_from_menu = tk.OptionMenu(currency_window, combo_from, *currencies)
    combo_from_menu.configure(bg="#545353", fg="#ffffff", bd=0)
    combo_from_menu.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    label_result = tk.Label(currency_window, text="", font=("Helvetica", 18), bg="#383838", fg="#ffffff", bd=0)
    label_result.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    combo_to = tk.StringVar()
    combo_to.set(currencies[1])
    combo_to_menu = tk.OptionMenu(currency_window, combo_to, *currencies)
    combo_to_menu.configure(bg="#545353", fg="#ffffff", bd=0)
    combo_to_menu.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    btn_convert = tk.Button(currency_window, text="Конвертувати", command=convert_currency, font=("Helvetica", 18), bg="#545353", fg="#ffffff", bd=0)
    btn_convert.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    currency_window.mainloop()


def close_currency_window():
    global currency_window
    currency_window.destroy()

def exit_settings():
    settings_window.destroy()

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

root = tk.Tk()
root.title("Калькулятор")
root.configure(bg="#383838")
root.geometry('295x390')

settings_button = tk.Button(root, text="⚙️", width=6, height=2, font=('Arial', 14), command=show_settings, borderwidth=0, bg="#545353", fg="white")
settings_button.grid(row=0, column=0, padx=1, pady=1, sticky='w')


entry = tk.Entry(root, width=14, font=('Arial', 20), justify='right', bd=0, state='normal', bg="#383838", fg="#ffffff")
entry.grid(row=2, column=1, columnspan=3, padx=1, pady=1)

buttons = [
    '%', '√', 'C', '⌫',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

row_val = 3
col_val = 0
button_padding = {'padx': 1, 'pady': 1}

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=6, height=2, font=('Arial', 14), command=calculate, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    elif button == 'C':
        tk.Button(root, text=button, width=6, height=2, font=('Arial', 14), command=clear_entry, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    elif button == '⌫':
        tk.Button(root, text=button, width=6, height=2, font=('Arial', 14), command=backspace, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    elif button == '':
        tk.Button(root, text=button, width=6, height=2, font=('Arial', 14), command=clear_all, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    elif button == '%':
        tk.Button(root, text=button, width=6, height=2, font=('Arial', 14), command=calculate_percent, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    elif button == '√':
        tk.Button(root, text=button, width=6, height=2, font=('Arial', 14), command=calculate_sqrt, borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)
    else:
        tk.Button(root, text=button, width=6, height=2, font=('Arial', 14),
                  command=lambda b=button: button_click(b), borderwidth=0, bg="#545353", fg="white").grid(row=row_val, column=col_val, **button_padding)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
