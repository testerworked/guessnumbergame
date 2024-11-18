import tkinter as tk
from tkinter import messagebox
import random
import pandas as pd

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Игра: Угадай число")

        self.width = 500
        self.height = 800
        master.geometry(f"{self.width}x{self.height}")

        self.center_window()

        self.low = 1
        self.high = 100
        self.target_number = random.randint(self.low, self.high)
        self.attempts = 0
        self.history = []

        self.label = tk.Label(master, text=f"Введите число от {self.low} до {self.high}:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=15, font=("Arial", 88))
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(master, text="Угадать", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.history_button = tk.Button(master, text="Показать историю попыток", command=self.show_history)
        self.history_button.pack(pady=5)

        self.show_number_button = tk.Button(master, text="Показать загаданное число", command=self.show_target_number)
        self.show_number_button.pack(pady=5)

        self.label = tk.Label(master, text=f"Картинка - подсказка")
        self.label.pack(pady=10)

        self.arrow_label = tk.Label(master)
        self.arrow_label.pack(pady=10)

        self.up_arrow = tk.PhotoImage(file="up_arrow.png")
        self.down_arrow = tk.PhotoImage(file="down_arrow.png")

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x = int((screen_width - self.width) / 2)
        y = int((screen_height - self.height) / 2)

        self.master.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1
            self.history.append(user_guess)

            if user_guess < self.low or user_guess > self.high:
                messagebox.showwarning("Ошибка", f"Введите число от {self.low} до {self.high}.")
                self.arrow_label.config(image='')
                self.entry.configure(bg="red")
            elif user_guess < self.target_number:
                messagebox.showinfo("Результат", "Слишком низкое число. Попробуйте снова.")
                self.arrow_label.config(image=self.up_arrow)
                self.entry.configure(bg="red")
            elif user_guess > self.target_number:
                messagebox.showinfo("Результат", "Слишком высокое число. Попробуйте снова.")
                self.arrow_label.config(image=self.down_arrow)
                self.entry.configure(bg="red")
            else:
                messagebox.showinfo("Поздравляем!", f"Вы угадали число {self.target_number} за {self.attempts} попыток!")
                self.arrow_label.config(image='')
                self.reset_game()
        except ValueError:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите допустимое число.")
            self.arrow_label.config(image='')
            self.entry.configure(bg="red")
    def show_history(self):
        if not self.history:
            messagebox.showinfo("История попыток", "У вас еще нет попыток.")
            return
        
        history_df = pd.DataFrame(self.history, columns=["Попытки"])
        history_str = history_df.to_string(index=False)
        messagebox.showinfo("История попыток", history_str)

    def show_target_number(self):
        messagebox.showinfo("Загаданное число", f"Загаданное число: {self.target_number}")

    def reset_game(self):
        self.target_number = random.randint(self.low, self.high)
        self.attempts = 0
        self.history = []
        self.entry.delete(0, tk.END)
        self.arrow_label.config(image='')
        self.entry.configure(bg="white")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()