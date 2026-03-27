import tkinter as tk
from tkinter import messagebox
import time

class BaseGenerator:
    def __init__(self, b, m, seed):
        self.b = b
        self.m = m
        self.x = seed

    def rand(self):
        self.x = (self.b * self.x) % self.m
        return self.x / self.m

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Дай ответ")
        self.root.geometry("400x350")
        
        self.b = 2**32 + 3
        self.m = 2**63
        self.seed = self.b
        self.generator = BaseGenerator(self.b, self.m, self.seed)

        for _ in range(100):
            self.generator.rand()

        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Твой вопрос:").pack(pady=10)
        self.question_entry = tk.Entry(self.root, width=40)
        self.question_entry.pack(pady=5)
        
        tk.Label(self.root, text="Вероятность, что будет ДА:").pack(pady=5)
        self.prob_entry = tk.Entry(self.root, width=10)
        self.prob_entry.pack(pady=5)
        
        self.answer_button = tk.Button(
            self.root,
            text="ответ",
            command=self.generate_answer,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        self.answer_button.pack(pady=20)
        
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 24, "bold"),
            pady=20
        )
        self.result_label.pack()
    
    def generate_answer(self):
        question = self.question_entry.get().strip()
        if not question:
            messagebox.showerror("Ошибка", "Вопрос то не написали")
            return
        try:
            prob = float(self.prob_entry.get())
            if prob < 0 or prob > 1:
                messagebox.showerror("Ошибка", "Вероятность должна быть от 0 до 1")
                return
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректное число")
            return
        
        alpha = self.generator.rand()
        
        if alpha < prob:
            result = "ДА!"
            color = "#FF1493"
        else:
            result = "НЕТ!"
            color = "#9370DB"
        
        self.result_label.config(text=result, fg=color)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
