#Дуже карява програма, більшість функціоналу який мав бути в програмі немає, тому що мені нехватило часу
#в майбутньому допишу її, зараз кидаю вже як є,в планах ще було добавити акаунт, в якому була б аватарка, імя ітд
#також добавлю час виконання програми, і зроблю нормальний інтерфейс, бо зараз це капець якийсь

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ======================================================================================================
def write_to_file(name, username, age, password):
    with open('users.txt', 'a') as file:
        file.write(f"{name},{username},{age},{password}\n")

# ======================================================================================================
def check_user(username, password):
    with open('users.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[1] == username and data[3] == password:
                return True
    return False
# ======================================================================================================
def login():
    root.withdraw()
    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.geometry("180x200")
    login_window.configure(bg="#595959")

    def confirm():
        entered_login = entry_username.get()
        entered_password = entry_password.get()

        if check_user(entered_login, entered_password):
            login_window.destroy()
            open_new_window()
        else:
            messagebox.showerror("Помилка", "Неправильний логін або пароль")

    label_username = tk.Label(login_window, text="Login:",bg="#595959")
    label_username.grid(row=0, column=0, padx=10, pady=5)

    label_password = tk.Label(login_window, text="Password:",bg="#595959")
    label_password.grid(row=1, column=0, padx=10, pady=5)

    entry_username = tk.Entry(login_window, bg="#7e7e7e", bd=0)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    entry_password = tk.Entry(login_window, show="*", bg="#7e7e7e", bd=0)
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    button_confirm = tk.Button(login_window, text="Confirm", command=confirm, bg="#7e7e7e", fg="white", activebackground="#6e6e6e", bd=0)
    button_confirm.grid(row=2, columnspan=2, padx=10, pady=10)
# ======================================================================================================


import tkinter as tk
from tkinter import ttk, messagebox

def on_hover(event):
    event.widget.config(bg="#a9a9a9")  # колір фону при наведенні
    event.widget.config(activebackground="#848484")  # колір фону при натисканні

def on_leave(event):
    event.widget.config(bg="#d9d9d9")  # колір фону при виїзді курсора
    event.widget.config(activebackground="#a9a9a9")  # повернення коліру фону при натисканні

def open_new_window():
    def show_results(test_window, task_answers):
        correct_count = sum(task_answers.values())
        total_tasks = len(task_answers)
        accuracy = (correct_count / total_tasks) * 100
        result_message = f"Ви відповіли правильно на {correct_count} з {total_tasks} завдань.\nТочність: {accuracy:.2f}%"
        messagebox.showinfo("Результати", result_message)

        # Показуємо кількість правильних відповідей у вікні результатів
        result_window = tk.Toplevel(test_window)
        result_window.title("Результати тестування")
        result_label = tk.Label(result_window, text=result_message)
        result_label.pack(padx=20, pady=10)

    def record_answer(task_answers, task_name, answer):
        task_answers[task_name] = answer

    def window1():
        root = tk.Tk()
        test_window = tk.Toplevel(root)
        test_window.title("Тестування")

        notebook = ttk.Notebook(test_window)
        notebook.pack(fill='both', expand=True)

        tasks = {
            "2+2": [4, 5, 6, 7],
            "8- 2": [6, 7, 8, 9],
            "6*2": [10, 11, 12, 13],
            "34/2": [16, 17, 18, 19],
            "45+12": [55, 56, 57, 58]
        }
        task_answers = {}  # Зберігає правильні відповіді для кожного завдання

        for task_name, options in tasks.items():
            task_frame = tk.Frame(notebook)
            notebook.add(task_frame, text=task_name)

            task_answer = tk.StringVar()  # Перемінна для зберігання відповіді

            # Генеруємо арифметичні завдання
            label_task = tk.Label(task_frame, text=f"{task_name} = ?", font=("Arial", 12))
            label_task.pack(pady=5)

            for option in options:
                radio_button = tk.Radiobutton(task_frame, text=str(option), variable=task_answer, value=str(option))
                radio_button.pack(anchor="w")

            task_answers[task_name] = task_answer

        finish_button = tk.Button(test_window, text="Закінчити тестування",
                                  command=lambda: show_results(test_window,
                                                               {task_name: task_answer.get() == str(correct_answer) for
                                                                task_name, task_answer, correct_answer in
                                                                zip(tasks.keys(), task_answers.values(),
                                                                    tasks.values())}), bg="#a9a9a9", fg="white", activebackground="#848484", bd=0)
        finish_button.pack(pady=10)
        finish_button.bind("<Enter>", on_hover)
        finish_button.bind("<Leave>", on_leave)

        root.mainloop()

    def window2():
        root = tk.Tk()
        test_window = tk.Toplevel(root)
        test_window.title("Тестування")

        notebook = ttk.Notebook(test_window)
        notebook.pack(fill='both', expand=True)

        tasks = {
            "2+2": [4, 5, 6, 7],
            "8- 2": [6, 7, 8, 9],
            "6*2": [10, 11, 12, 13],
            "34/2": [16, 17, 18, 19],
            "45+12": [55, 56, 57, 58]
        }
        task_answers = {}  # Зберігає правильні відповіді для кожного завдання

        for task_name, options in tasks.items():
            task_frame = tk.Frame(notebook)
            notebook.add(task_frame, text=task_name)

            task_answer = tk.StringVar()  # Перемінна для зберігання відповіді

            # Генеруємо арифметичні завдання
            label_task = tk.Label(task_frame, text=f"{task_name} = ?", font=("Arial", 12))
            label_task.pack(pady=5)

            for option in options:
                radio_button = tk.Radiobutton(task_frame, text=str(option), variable=task_answer, value=str(option))
                radio_button.pack(anchor="w")

            task_answers[task_name] = task_answer

        finish_button = tk.Button(test_window, text="Закінчити тестування",
                                  command=lambda: show_results(test_window,
                                                               {task_name: task_answer.get() == str(correct_answer) for
                                                                task_name, task_answer, correct_answer in
                                                                zip(tasks.keys(), task_answers.values(),
                                                                    tasks.values())}), bg="#a9a9a9", fg="white", activebackground="#848484", bd=0)
        finish_button.pack(pady=10)
        finish_button.bind("<Enter>", on_hover)
        finish_button.bind("<Leave>", on_leave)

        root.mainloop()

    def window3():
        root = tk.Tk()
        test_window = tk.Toplevel(root)
        test_window.title("Тестування")

        notebook = ttk.Notebook(test_window)
        notebook.pack(fill='both', expand=True)

        tasks = {
            "654*123": [80442, 80423, 40442, 72442],
            "√40": [6.3,        7.5, 8.1, 4.3],
            "6*22": [10, 11, 12, 13],
            "34/2": [132, 17, 18, 19],
            "45+12": [55, 56, 57, 58]
        }
        task_answers = {}  # Зберігає правильні в

        for task_name, options in tasks.items():
            task_frame = tk.Frame(notebook)
            notebook.add(task_frame, text=task_name)

            task_answer = tk.StringVar()  # Перемінна для зберігання відповіді

            # Генеруємо арифметичні завдання
            label_task = tk.Label(task_frame, text=f"{task_name} = ?", font=("Arial", 12))
            label_task.pack(pady=5)

            for option in options:
                radio_button = tk.Radiobutton(task_frame, text=str(option), variable=task_answer, value=str(option))
                radio_button.pack(anchor="w")

            task_answers[task_name] = task_answer

        finish_button = tk.Button(test_window, text="Закінчити тестування",
                                  command=lambda: show_results(test_window,
                                                               {task_name: task_answer.get() == str(correct_answer) for
                                                                task_name, task_answer, correct_answer in
                                                                zip(tasks.keys(), task_answers.values(),
                                                                    tasks.values())}), bg="#a9a9a9", fg="white",
                                  activebackground="#848484", bd=0)
        finish_button.pack(pady=10)
        finish_button.bind("<Enter>", on_hover)
        finish_button.bind("<Leave>", on_leave)

        root.mainloop()

    def open_window():
        selected_item = combo_box.get()
        if selected_item in window_functions:
            window_functions[selected_item]()

    root = tk.Tk()
    root.title("Головне вікно")

    combo_box = ttk.Combobox(root, values=["Вікно 1", "Вікно 2", "Вікно 3"])
    combo_box.pack(pady=10)

    open_button = tk.Button(root, text="Відкрити вікно", command=open_window, bg="#a9a9a9", fg="white",
                            activebackground="#848484", bd=0)
    open_button.pack()

    window_functions = {
        "Вікно 1": window1,
        "Вікно 2": window2,
        "Вікно 3": window3
    }

    root.mainloop()
# ======================================================================================================
def register():
    register_window = tk.Toplevel()
    register_window.title("Register")
    register_window.geometry("180x200")
    register_window.configure(bg="#595959")

    def confirm():
        username = entry_username.get()
        age = entry_age.get()
        password = entry_password.get()
        name = entry_name.get()

        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            messagebox.showerror("Помилка", "Пароль повинен містити принаймні 8 символів і містити букви та цифри.")
            return
        if any(char in username for char in ['.', ',', '(', ')', '[', ']', '{', '}']):
            messagebox.showerror("Помилка", "Логін не повинен містити спеціальних символів.")
            return
        try:
            age = int(age)
            if age < 12 or age > 90:
                messagebox.showerror("Помилка", "Вік повинен бути від 12 до 90 років.")
                return
        except ValueError:
            messagebox.showerror("Помилка", "Неправильно введений вік.")
            return

        write_to_file(name, username, age, password)
        messagebox.showinfo("Успіх", "Ви успішно зареєстровані!")
        register_window.destroy()
        open_main_window()

    label_name = tk.Label(register_window, text="Ім'я:",bg="#595959")
    label_name.grid(row=0, column=0, padx=10, pady=5)

    label_username = tk.Label(register_window, text="Логін:",bg="#595959")
    label_username.grid(row=1, column=0, padx=10, pady=5)

    label_age = tk.Label(register_window, text="Вік:",bg="#595959")
    label_age.grid(row=2, column=0, padx=10, pady=5)

    label_password = tk.Label(register_window, text="Пароль:",bg="#595959")
    label_password.grid(row=3, column=0, padx=10, pady=5)

    entry_name = tk.Entry(register_window, bg="#7e7e7e", bd=0)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    entry_username = tk.Entry(register_window, bg="#7e7e7e", bd=0)
    entry_username.grid(row=1, column=1, padx=10, pady=5)

    entry_age = tk.Entry(register_window, bg="#7e7e7e", bd=0)
    entry_age.grid(row=2, column=1, padx=10, pady=5)

    entry_password = tk.Entry(register_window, show="*", bg="#7e7e7e", bd=0)
    entry_password.grid(row=3, column=1, padx=10, pady=5)

    button_confirm = tk.Button(register_window, text="Підтвердити", command=confirm, bg="#7e7e7e", fg="white", activebackground="#6e6e6e", bd=0)
    button_confirm.grid(row=4, columnspan=2, padx=10, pady=10)

    button_confirm.bind("<Enter>", on_hover)
    button_confirm.bind("<Leave>", on_leave)



def open_main_window():
    root.deiconify()


def on_hover1(event):
    event.widget.config(bg="#6e6e6e")  # зміна коліру фону при наведенні
    event.widget.config(activebackground="#4a4a4a")  # зміна коліру фону при натисканні
def on_leave1(event):
    event.widget.config(bg="#7e7e7e")  # зміна коліру фону при виїзді курсора
    event.widget.config(activebackground="#6e6e6e")  # повернення коліру фону при натисканні


root = tk.Tk()
root.geometry("180x200")
root.configure(bg="#595959")
root.title("Тестування")

label = tk.Label(root, text="Тестування", bg="#595959", font=("Anime Ace", 20))
label.pack(pady=20)

login_button = tk.Button(root, text="Login", width=10, command=login, bg="#7e7e7e", fg="white", bd=0)
login_button.pack(pady=10)
login_button.bind("<Enter>", on_hover1)
login_button.bind("<Leave>", on_leave1)

register_button = tk.Button(root, text="Register", width=10, command=register, bg="#7e7e7e", fg="white", bd=0)
register_button.pack(pady=10)
register_button.bind("<Enter>", on_hover1)
register_button.bind("<Leave>", on_leave1)

root.mainloop()


