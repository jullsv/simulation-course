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

class MagicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Шар предсказаний (Magic 8-Ball)")
        self.root.geometry("500x700")
        
        self.b = 2**32 + 3
        self.m = 2**63
        self.seed = int(time.time() * 1000) % self.m
        self.generator = BaseGenerator(self.b, self.m, self.seed)
        
        self.answers = [
            "Определённо да",
            "Скорее да, чем нет",
            "Безусловно",
            "Хорошие перспективы",
            "Знаки говорят - да",
            "Пока не ясно",
            "Спроси позже",
            "Возможно ты кот",
            "Сейчас нельзя предсказать",
            "Очень сомнительно"
        ]
        
        self.prob_entries = []
        
        for _ in range(100):
            self.generator.rand()
        
        self.create_widgets()
    
    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text=" ШАР ПРЕДСКАЗАНИЙ ",
            font=("Arial", 20, "bold"),
            pady=10
        )
        title_label.pack()
        
        tk.Label(self.root, text="Твой вопрос:", font=("Arial", 12)).pack(pady=5)
        self.question_entry = tk.Entry(self.root, width=50)
        self.question_entry.pack(pady=5)
        
        tk.Label(self.root, text="Вероятности ответов:", font=("Arial", 12, "bold")).pack(pady=10)
        
        self.prob_frame = tk.Frame(self.root)
        self.prob_frame.pack(pady=5)
        
        for i in range(len(self.answers) - 1):
            frame = tk.Frame(self.prob_frame)
            frame.pack(pady=2)
            
            tk.Label(frame, text=f"P({self.answers[i][:25]}...): ", width=35, anchor='w').pack(side=tk.LEFT)
            entry = tk.Entry(frame, width=10)
            entry.insert(0, "0.09")
            entry.pack(side=tk.LEFT, padx=5)
            self.prob_entries.append(entry)
        
        last_frame = tk.Frame(self.prob_frame)
        last_frame.pack(pady=2)
        
        self.last_prob_label = tk.Label(last_frame, text="", width=35, anchor='w')
        self.last_prob_label.pack(side=tk.LEFT)
        
        self.last_prob_value_label = tk.Label(last_frame, text="")
        self.last_prob_value_label.pack(side=tk.LEFT, padx=5)
        
        self.ask_button = tk.Button(
            self.root,
            text="Спросить шааар",
            command=self.get_answer,
            bg="#9370DB",
            fg="white",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=10
        )
        self.ask_button.pack(pady=20)
        
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 18, "bold"),
            fg="#FF1493",
            pady=20,
            wraplength=400
        )
        self.result_label.pack()
    
    def get_answer(self):
        question = self.question_entry.get().strip()
        if not question:
            messagebox.showerror("Ошибка", "Введите вопрос")
            return
        
        try:
            probs = []
            for entry in self.prob_entries:
                p = float(entry.get())
                if p < 0 or p > 1:
                    messagebox.showerror("Ошибка", "Вероятность должна быть от 0 до 1")
                    return
                probs.append(p)
            
            sum_probs = sum(probs)
            if sum_probs >= 1:
                messagebox.showerror("Ошибка", f"Сумма вероятностей не может быть >= 1 (сейчас {sum_probs})")
                return
            
            last_prob = 1.0 - sum_probs
            probs.append(last_prob)
            
            self.last_prob_label.config(text=f"P({self.answers[-1][:25]}...): ")
            self.last_prob_value_label.config(text=f"{last_prob:.4f}")
            
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа")
            return
        
        alpha = self.generator.rand()
        
        A = alpha
        k = 0
        
        while k < len(probs):
            A = A - probs[k]
            if A <= 0:
                break
            k = k + 1
        
        answer = self.answers[k]
        self.result_label.config(text=answer)

def main():
    root = tk.Tk()
    app = MagicApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
