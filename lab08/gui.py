import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import poisson
from main import PoissonSimulator

class ModernApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторная №8")
        
        self.root.geometry("1400x850")
        self.root.configure(bg="#f5f6f7")
        self.sim = PoissonSimulator()
        
        self.default_font = ("Segoe UI", 14) 
        self.log_font = ("Consolas", 13) 
        
        style = ttk.Style()
        style.configure(".", font=self.default_font)
        style.configure("TButton", font=("Segoe UI", 14, "bold"))
        
        self.setup_ui()

    def setup_ui(self):
        self.root.columnconfigure(0, weight=3) 
        self.root.columnconfigure(1, weight=1) 
        self.root.rowconfigure(0, weight=1)

        self.plot_frame = tk.Frame(self.root, bg="white", bd=1, relief="flat")
        self.plot_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        
        self.fig, self.ax = plt.subplots(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

        right_panel = tk.Frame(self.root, bg="#f5f6f7")
        right_panel.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        right_panel.rowconfigure(1, weight=1) 
        right_panel.columnconfigure(0, weight=1)

        input_group = tk.LabelFrame(right_panel, text=" Параметры системы ", bg="white", padx=15, pady=15, font=("Segoe UI", 14, "bold"))
        input_group.grid(row=0, column=0, sticky="ew")
        input_group.columnconfigure(0, weight=1)

        self.params = {}
        fields = [("Интенсивность (λ):", "5.0"), 
                  ("Интервал контроля (T):", "1.0"), 
                  ("Время работы (сек):", "1000")]
        
        for i, (label, default) in enumerate(fields):
            tk.Label(input_group, text=label, bg="white", font=self.default_font).grid(row=i*2, column=0, sticky="w", pady=(10,0))
            ent = ttk.Entry(input_group, font=self.default_font)
            ent.insert(0, default)
            ent.grid(row=i*2+1, column=0, sticky="ew", pady=(5,10))
            self.params[label] = ent

        self.btn_run = tk.Button(input_group, text="ЗАПУСТИТЬ МОДЕЛИРОВАНИЕ", bg="#007bff", fg="white", 
                                 relief="flat", font=("Segoe UI", 14, "bold"), cursor="hand2",
                                 command=self.run_sim)
        self.btn_run.grid(row=7, column=0, sticky="ew", pady=15, ipady=10)

        self.log_box = tk.Text(right_panel, font=self.log_font, bg="#e9ecef", state="disabled", relief="flat")
        self.log_box.grid(row=1, column=0, sticky="nsew", pady=(20, 0))

    def log(self, text):
        self.log_box.config(state="normal")
        self.log_box.insert(tk.END, text + "\n")
        self.log_box.see(tk.END)
        self.log_box.config(state="disabled")

    def run_sim(self):
        try:
            L = float(self.params["Интенсивность (λ):"].get())
            T = float(self.params["Интервал контроля (T):"].get())
            Total = float(self.params["Время работы (сек):"].get())

            if L <= 0 or T <= 0 or Total <= T:
                messagebox.showwarning("Внимание", "λ и T должны быть > 0. \nОбщее время должно быть больше T!")
                return
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения.")
            return

        self.log_box.config(state="normal")
        self.log_box.delete(1.0, tk.END)
        self.log_box.config(state="disabled")
        
        self.log(f"> Моделирование по Алгоритму 2")
        self.log(f"> Параметры: λ={L}, T={T}")
        
        counts, total_ev = self.sim.simulate_continuous_flow(L, T, Total)
        m, v, r = self.sim.get_statistics(counts)
        
        self.log(f"> Событий в потоке: {total_ev}")
        self.log(f"> Выборка интервалов N: {len(counts)}")
        self.log("-" * 35)
        self.log(f"Ср. значение (E): {m:.4f}")
        self.log(f"Дисперсия (D):   {v:.4f}")
        self.log(f"Индекс (D/E):    {r:.4f}")
        self.log("-" * 35)
        
        self.ax.clear()
        self.ax.set_title(f"Эмпирическое распределение числа запросов", fontsize=14)
        
        bins = np.arange(-0.5, np.max(counts) + 1.5, 1)
        self.ax.hist(counts, bins=bins, density=True, color="#007bff", alpha=0.6, edgecolor="white", label="Эксперимент")
        
        k = np.arange(0, np.max(counts) + 1)
        theo = poisson.pmf(k, L*T)
        self.ax.plot(k, theo, 'o-', color="#dc3545", linewidth=2, label=f"Теория (λT={L*T:.2f})")
        
        self.ax.set_xlabel("Число событий k", fontsize=12)
        self.ax.set_ylabel("Вероятность P(k)", fontsize=12)
        self.ax.legend(fontsize=12)
        self.ax.grid(True, alpha=0.2)
        self.fig.tight_layout()
        self.canvas.draw()
        
        if abs(r - 1) < 0.1:
            self.log("[ВЫВОД] Свойства стационарного\nпуассоновского потока подтверждены.")
        else:
            self.log("[ВЫВОД] Есть отклонение от теории.\nРекомендуется увеличить время.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernApp(root)
    root.mainloop()
