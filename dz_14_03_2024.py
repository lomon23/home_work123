import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
from datetime import datetime


def start_game(difficulty):
    global current_word, remaining_time, timer_running
    current_word = random.choice(words)
    random_color = random.choice(color)
    word_label.config(text=current_word, fg=random_color)
    score.set(0)
    remaining_time = get_time(difficulty)
    timer_label.config(text="Час: {}".format(remaining_time))
    timer_running = True
    threading.Thread(target=run_timer).start()


def run_timer():
    global remaining_time, timer_running
    while remaining_time > 0 and timer_running:
        time.sleep(1)
        remaining_time -= 1
        timer_label.config(text="Час: {}".format(remaining_time))
    if timer_running:
        messagebox.showinfo("Кінець гри", "Час вийшов! Ви програли!")
        timer_running = False
        save_score()


def get_time(difficulty):
    if difficulty == "Легко":
        return 20
    elif difficulty == "Середньо":
        return 10
    elif difficulty == "Важко":
        return 5


def check_word(event=None):
    global current_word, remaining_time
    entered_color = entry.get().strip()
    current_color_rgb = word_label.winfo_rgb(word_label.cget('fg'))
    current_color_hex = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: int(x / 256), current_color_rgb))

    if entered_color.lower() == colors[current_color_hex].lower() and timer_running:
        score.set(score.get() + 1)
        current_word = random.choice(words)
        random_color = random.choice(color)
        word_label.config(text=current_word, fg=random_color)
        entry.delete(0, tk.END)
        remaining_time += 3
        timer_label.config(text="Час: {}".format(remaining_time))
    else:
        score.set(score.get() - 1)
        entry.delete(0, tk.END)

def save_score():
    filename = "scores.txt"
    with open(filename, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"result: {score.get()}, date and time: {timestamp}\n")
        messagebox.showinfo("Збережено", f"Рахунок {score.get()} збережено у файлі {filename}")


def clear_statistics():
    filename = "scores.txt"
    try:
        with open(filename, "w") as file:
            file.write("")  # Просто очищаємо вміст файлу
        messagebox.showinfo("Статистика очищена", "Статистика успішно очищена.")
    except FileNotFoundError:
        messagebox.showinfo("Помилка", "Файл статистики не знайдено.")


def show_statistics():
    stats_window = tk.Toplevel(root)
    stats_window.title("Статистика")
    stats_window.geometry("300x200")
    stats_window.attributes("-topmost", True)
    stats_label = tk.Label(stats_window, text="Збереження:")
    stats_label.pack()
    stats_listbox = tk.Listbox(stats_window)
    stats_listbox.pack(fill='both', expand=True)
    filename = "scores.txt"
    try:
        with open(filename, "r") as file:
            statistics = file.readlines()
            for line in statistics:
                stats_listbox.insert('END', line.strip())
    except FileNotFoundError:
        stats_listbox.insert('END', "Файл статистики не знайдено.")

    def save_selected():
        selected_index = stats_listbox.curselection()
        if selected_index:
            selected_item = stats_listbox.get(selected_index)
            selected_file = selected_item.split(": ")[1]
            with open(selected_file, "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"result: {score.get()}, date and time: {timestamp}\n")
                messagebox.showinfo("Збережено", f"Рахунок {score.get()} збережено у файлі {selected_file}")
    save_button = tk.Button(stats_window, text="Зберегти", command=save_selected)
    save_button.pack(side='left')
    clear_button = tk.Button(stats_window, text="Очистити статистику", command=clear_statistics)
    clear_button.pack(side='left')


root = tk.Tk()
root.title("bebra")

label111=tk.Label(text='гра кольорів',font=("Helvetica", 20))
label111.pack()


score = tk.IntVar()
score.set(0)


words = ["чорний", "червоний", "синій", "зелений", "жовтий", "рожевий", "фіолетовий", "оранджевий", "коричневий"]
color = ['#000000','#ff0000','#0006ff','#146524','#d5a716','#dc00a8','#9200dc','#dc4f00','#5d2200']
colors = {
    '#000000': 'Чорний',
    '#ff0000': 'Червоний',
    '#0006ff': 'Синій',
    '#146524': 'Зелений',
    '#d5a716': 'Жовтий',
    '#dc00a8': 'Рожевий',
    '#9200dc': 'Фіолетовий',
    '#dc4f00': 'Оранджевий',
    '#5d2200': 'Коричневий'
}


current_word = random.choice(words)
word_label = tk.Label(root, text=current_word, font=("Helvetica", 20))
word_label.pack()

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack()
entry.bind("<Return>", check_word)

score_label = tk.Label(root, text="Рахунок: ", font=("Helvetica", 14))
score_label.pack()
score_display = tk.Label(root, textvariable=score, font=("Helvetica", 14))
score_display.pack()
timer_label = tk.Label(root, text="Час: ", font=("Helvetica", 14))
timer_label.pack()

easy_button = tk.Button(root, text="Легко", font=("Helvetica", 14), command=lambda: start_game("Легко"))
easy_button.pack(side='left', padx=20, pady=10)
medium_button = tk.Button(root, text="Середньо", font=("Helvetica", 14), command=lambda: start_game("Середньо"))
medium_button.pack(side='left', padx=20, pady=10)
hard_button = tk.Button(root, text="Важко", font=("Helvetica", 14), command=lambda: start_game("Важко"))
hard_button.pack(side='left', padx=20, pady=10)
stats_button = tk.Button(root, text="Статистика", font=("Helvetica", 14), command=show_statistics)
stats_button.pack(side='right', padx=20, pady=10)

root.mainloop()