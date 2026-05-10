import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from model import MarkovWeatherCalculate, MarkovWeatherGenerator


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Марковская модель погоды")
        self.root.geometry("1000x600")

        self.names = {1: "Ясно", 2: "Облачно", 3: "Пасмурно"}
        self.colors = {1: "gold", 2: "skyblue", 3: "gray"}

        self.times = []
        self.states = []
        self.index = 0
        self.running = False

        default_q = [[-0.4, 0.3, 0.1], [0.4, -0.8, 0.4], [0.1, 0.4, -0.5]]

        if not self.check_q(default_q):
            messagebox.showerror("Критическая ошибка", "Матрица по умолчанию некорректна!\nПрограмма не может быть запущена.")
            sys.exit(1)

        self.create_widgets()
        self.setup_styles()

    def setup_styles(self):
        style = ttk.Style()
        style.configure('Green.TButton', foreground='black', background='#2ecc71', font=('Arial', 10, 'bold'))
        style.map('Green.TButton', background=[('active', '#27ae60'), ('pressed', '#219150')])
        style.configure('Red.TButton', foreground='black', background='#e74c3c', font=('Arial', 10, 'bold'))
        style.map('Red.TButton', background=[('active', '#c0392b'), ('pressed', '#a93226')])
        style.configure('Orange.TButton', foreground='black', background='#f39c12', font=('Arial', 10, 'bold'))
        style.map('Orange.TButton', background=[('active', '#d35400'), ('pressed', '#ba4a00')])

    def create_widgets(self):
        left_frame = ttk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        right_frame = ttk.Frame(self.root, width=300)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        right_frame.pack_propagate(False)

        weather_frame = ttk.LabelFrame(left_frame, text="Текущее состояние")
        weather_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.weather_label = tk.Label(weather_frame, text="Погода: -", font=("Arial", 16), width=20, height=3)
        self.weather_label.pack(pady=5)

        graph_frame = ttk.LabelFrame(left_frame, text="Графики")
        graph_frame.pack(fill=tk.BOTH, expand=True)
        
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        params_label = ttk.Label(right_frame, text="ПАРАМЕТРЫ МОДЕЛИ", font=('Arial', 12, 'bold'))
        params_label.pack(pady=10)

        q_frame = ttk.LabelFrame(right_frame, text="Матрица интенсивностей Q")
        q_frame.pack(fill=tk.X, pady=5)

        default_q = [[-0.4, 0.3, 0.1], [0.4, -0.8, 0.4], [0.1, 0.4, -0.5]]
        self.q_entries = []

        for i in range(3):
            row = []
            row_frame = ttk.Frame(q_frame)
            row_frame.pack(pady=2)
            for j in range(3):
                entry = ttk.Entry(row_frame, width=6, justify='center')
                entry.insert(0, str(default_q[i][j]))
                entry.pack(side=tk.LEFT, padx=2)
                row.append(entry)
            self.q_entries.append(row)

        start_frame = ttk.LabelFrame(right_frame, text="Начальные условия")
        start_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(start_frame, text="Начальное состояние (1-3):").pack(anchor=tk.W, padx=5)
        self.start_entry = ttk.Entry(start_frame)
        self.start_entry.insert(0, "1")
        self.start_entry.pack(fill=tk.X, padx=5, pady=2)

        ttk.Label(start_frame, text="Время моделирования (дней):").pack(anchor=tk.W, padx=5)
        self.t_entry = ttk.Entry(start_frame)
        self.t_entry.insert(0, "100")
        self.t_entry.pack(fill=tk.X, padx=5, pady=2)

        speed_frame = ttk.LabelFrame(right_frame, text="Визуализация")
        speed_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(speed_frame, text="Скорость (мс):").pack(anchor=tk.W, padx=5)
        self.speed_var = tk.IntVar(value=300)
        speed_scale = ttk.Scale(speed_frame, from_=10, to=1000, variable=self.speed_var, orient=tk.HORIZONTAL)
        speed_scale.pack(fill=tk.X, padx=5, pady=2)
        
        self.speed_label = ttk.Label(speed_frame, text="300 мс")
        self.speed_label.pack(anchor=tk.E, padx=5)
        speed_scale.config(command=lambda e: self.speed_label.config(text=f"{int(float(e))} мс"))

        btn_frame = ttk.Frame(right_frame)
        btn_frame.pack(fill=tk.X, pady=15)

        ttk.Button(btn_frame, text="ЗАПУСТИТЬ", command=self.start, style='Green.TButton').pack(fill=tk.X, pady=5)
        ttk.Button(btn_frame, text="СТОП", command=self.stop, style='Red.TButton').pack(fill=tk.X, pady=5)
        ttk.Button(btn_frame, text="СОХРАНИТЬ РЕЗУЛЬТАТЫ", command=self.save_results, style='Orange.TButton').pack(fill=tk.X, pady=5)
        
        stats_frame = ttk.LabelFrame(right_frame, text="Статистика")
        stats_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.text_stats = tk.Text(stats_frame, width=30, height=10, font=('Courier New', 9), wrap='none')
        self.text_stats.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def read_q(self):
        Q = []
        for i in range(3):
            row = []
            for j in range(3):
                try:
                    val = float(self.q_entries[i][j].get())
                except ValueError:
                    raise ValueError(f"Неверный формат числа в ячейке [{i},{j}]")
                row.append(val)
            Q.append(row)
        return Q

    def check_q(self, Q):
        for i in range(3):
            s = sum(Q[i])
            if abs(s) > 1e-9:
                return False
            if Q[i][i] >= 0:
                return False
            for j in range(3):
                if i != j and Q[i][j] < 0:
                    return False
        return True

    def start(self):
        try:
            Q = self.read_q()
            T = float(self.t_entry.get())
            start_state = int(self.start_entry.get())

            if start_state not in [1, 2, 3]:
                raise ValueError("Начальное состояние должно быть 1, 2 или 3")

            if not self.check_q(Q):
                messagebox.showerror("Ошибка", "Матрица Q неверна:\n1. Сумма строки должна быть 0.\n2. Диагональ < 0.\n3. Остальные элементы >= 0.")
                return

            generator = MarkovWeatherGenerator(Q, start_state)
            calculator = MarkovWeatherCalculate(Q)

            self.times, self.states, durations = generator.experiment(T)
            stats_text, emp, theor = calculator.stats_text(durations)
            
            self.current_calculator = calculator
            self.current_durations = durations

            self.text_stats.delete("1.0", tk.END)
            self.text_stats.insert(tk.END, stats_text)

            self.index = 0
            self.running = True
            self.animate(emp, theor)

        except Exception as e:
            messagebox.showerror("Ошибка ввода", f"Проверьте данные:\n{str(e)}")

    def stop(self):
        self.running = False

    def save_results(self):
        if not hasattr(self, 'current_calculator'):
            messagebox.showwarning("Нет данных", "Сначала запустите моделирование.")
            return
        
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], initialfile="weather_simulation")
        if filename:
            self.current_calculator.export_to_csv(self.current_durations, filename)
            messagebox.showinfo("Успех", f"Результаты сохранены в {filename}")

    def animate(self, emp, theor):
        if not self.running:
            return

        if self.index >= len(self.states):
            self.running = False
            return

        current_state = self.states[self.index]
        current_time = self.times[self.index]

        self.weather_label.config(text=f"День {current_time:.2f}\n{self.names[current_state]}", bg=self.colors[current_state], fg="black" if current_state != 1 else "darkred")

        self.ax1.clear()
        self.ax2.clear()

        self.ax1.step(self.times[: self.index + 1], self.states[: self.index + 1], where="post", color='blue')
        self.ax1.set_title("Смена погоды во времени")
        self.ax1.set_xlabel("t, дни")
        self.ax1.set_ylabel("Состояние")
        self.ax1.set_yticks([1, 2, 3])
        self.ax1.set_yticklabels(["Ясно", "Облачно", "Пасмурно"])
        self.ax1.grid(True, linestyle='--', alpha=0.5)

        x = [1, 2, 3]
        width = 0.35

        self.ax2.bar([i - width / 2 for i in x], emp, width, label="Эмпирическое", color='yellow')
        self.ax2.bar([i + width / 2 for i in x], theor, width, label="Теоретическое", color='purple')
        
        self.ax2.set_title("Стационарное распределение")
        self.ax2.set_xticks(x)
        self.ax2.set_xticklabels(["Ясно", "Облачно", "Пасмурно"])
        self.ax2.set_ylim(0, 1)
        self.ax2.legend(loc='upper right')
        self.ax2.grid(True, linestyle='--', alpha=0.5, axis='y')

        self.canvas.draw()

        self.index += 1
        
        speed = self.speed_var.get()
        self.root.after(speed, lambda: self.animate(emp, theor))


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
