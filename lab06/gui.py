import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from models import DiscreteValues, Calculate, NormalRandomVariable
from gen import BaseGenerator

class SimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Моделирование СВ")
        self.root.geometry("1500x1050")
        
        self.font_title = ('Arial', 18, 'bold')
        self.font_large = ('Arial', 16)
        self.font_medium = ('Arial', 14)
        self.font_entry = ('Arial', 14)
        self.font_button = ('Arial', 14, 'bold')

        tab_control = ttk.Notebook(root)
        self.tab_dsv = ttk.Frame(tab_control)
        self.tab_normal = ttk.Frame(tab_control)
        tab_control.add(self.tab_dsv, text='1. Дискретная СВ (ДСВ)')
        tab_control.add(self.tab_normal, text='2. Нормальная СВ')
        tab_control.pack(expand=1, fill="both")
        
        style = ttk.Style()
        style.configure("TNotebook.Tab", font=('Arial', 15, 'bold'), padding=[20, 12])
        style.configure("TLabelframe.Label", font=('Arial', 16, 'bold'))
        style.configure("TLabel", font=('Arial', 14))
        style.configure("TButton", font=self.font_button)
        style.configure("Treeview", font=('Arial', 13), rowheight=35)
        style.configure("Treeview.Heading", font=('Arial', 14, 'bold'))

        self.init_dsv_tab()
        self.init_normal_tab()

    def init_dsv_tab(self):
        frame_input = ttk.LabelFrame(self.tab_dsv, text="Параметры", padding=20)
        frame_input.pack(fill="x", padx=40, pady=20)

        self.prob_entries = []
        self.values = [1, 2, 3, 4, 5]
        defaults = [0.3, 0.2, 0.2, 0.001, ""]
        
        for i in range(5):
            lbl = ttk.Label(frame_input, text=f"Prob {i+1}:", font=self.font_large)
            lbl.grid(row=i, column=0, padx=20, pady=10, sticky="e")
            
            entry = ttk.Entry(frame_input, width=14, font=self.font_entry)
            if defaults[i] != "":
                entry.insert(0, str(defaults[i]))
            entry.grid(row=i, column=1, padx=10, pady=10, ipady=6)
            self.prob_entries.append(entry)

        btn_auto = ttk.Button(frame_input, text="auto", command=self.calc_auto_p5)
        btn_auto.grid(row=4, column=2, padx=15, ipady=5)
        
        lbl_n = ttk.Label(frame_input, text="Number of experiments:", font=self.font_large)
        lbl_n.grid(row=5, column=0, padx=20, pady=20, sticky="e")
        
        self.entry_n = ttk.Entry(frame_input, width=14, font=self.font_entry)
        self.entry_n.insert(0, "10000")
        self.entry_n.grid(row=5, column=1, padx=10, pady=20, ipady=6)

        btn_start = ttk.Button(frame_input, text="Start", command=self.run_dsv)
        btn_start.grid(row=6, column=0, columnspan=3, pady=20, ipady=8)

        frame_table = ttk.LabelFrame(self.tab_dsv, text="Результаты", padding=15)
        frame_table.pack(fill="x", padx=40, pady=20)
        
        cols = ("N", "Mean", "Mean Err %", "Var", "Var Err %", "Chi-Sq", "Chi-Crit", "Result")
        self.tree = ttk.Treeview(frame_table, columns=cols, show="headings", height=5)
        
        col_widths = {"N": 70, "Mean": 110, "Mean Err %": 120, "Var": 110, 
                      "Var Err %": 120, "Chi-Sq": 100, "Chi-Crit": 100, "Result": 130}
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=col_widths[c], anchor="center")
        
        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="x", expand=True)
        scrollbar.pack(side="right", fill="y")

        frame_graph = ttk.LabelFrame(self.tab_dsv, text="Гистограмма (N=10000)", padding=15)
        frame_graph.pack(fill="both", expand=True, padx=40, pady=20)
        
        self.fig, self.ax = plt.subplots(figsize=(13, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame_graph)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        self.ax.tick_params(axis='both', labelsize=14)

    def calc_auto_p5(self):
        try:
            s = sum(float(self.prob_entries[i].get()) for i in range(4))
            p5 = 1.0 - s
            self.prob_entries[4].config(state="normal")
            self.prob_entries[4].delete(0, tk.END)
            self.prob_entries[4].insert(0, f"{p5:.3f}")
            self.prob_entries[4].config(state="readonly")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неверный ввод: {e}")

    def run_dsv(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        try:
            raw_probs = []
            for i in range(4):
                raw_probs.append(float(self.prob_entries[i].get()))
            
            p5_str = self.prob_entries[4].get()
            if p5_str:
                raw_probs.append(float(p5_str))
            else:
                raw_probs.append(1.0 - sum(raw_probs))
            
            total_prob = sum(raw_probs)
            if abs(total_prob - 1.0) > 0.001:
                messagebox.showerror("Ошибка", 
                    f"Сумма вероятностей должна быть равна 1!\n")
                return
            
            N_input = int(self.entry_n.get())
            
            gen = BaseGenerator()
            dv = DiscreteValues(self.values, raw_probs, generator=gen)
            
            calc_theor = Calculate([0]*5, 1, self.values, dv.prob)
            t_mean = calc_theor.mean()
            t_var = calc_theor.var(t_mean)

            last_counts = None
            N_list = [10, 100, 1000, N_input]

            for N in N_list:
                counts = dv.experiment(N)
                calc = Calculate(counts, N, self.values, dv.prob)
                
                e_mean = calc.emp_mean()
                e_var = calc.emp_var(e_mean)
                
                err_m = calc.relative_error(t_mean, e_mean) * 100
                err_v = calc.relative_error(t_var, e_var) * 100
                
                chi = calc.chi_kvadrat()
                chi_crit = 9.488
                res = calc.check_chi(chi)
                
                self.tree.insert("", "end", values=(
                    N, f"{e_mean:.3f}", f"{err_m:.1f}%", f"{e_var:.3f}", 
                    f"{err_v:.1f}%", f"{chi:.2f}", f"{chi_crit:.2f}", res
                ))
                
                if N == N_input:
                    last_counts = counts

            if last_counts:
                self.ax.clear()
                
                x = np.arange(len(self.values))
                width = 0.35
                
                self.ax.bar(x - width/2, dv.prob, width, label='Theoretical', 
                           color='#9370DB', edgecolor='black')
                
                emp_freqs = [c/N_input for c in last_counts]
                self.ax.bar(x + width/2, emp_freqs, width, label=f'Empirical (N={N_input})', 
                           color='#6A5ACD', edgecolor='black')
                
                for i, (xt, xe) in enumerate(zip(x - width/2, x + width/2)):
                    self.ax.annotate(f'{dv.prob[i]:.3f}', xy=(xt, dv.prob[i]), 
                                   ha='center', va='bottom', fontsize=12, fontweight='bold', color='white')
                    self.ax.annotate(f'{emp_freqs[i]:.3f}', xy=(xe, emp_freqs[i]), 
                                   ha='center', va='bottom', fontsize=12, fontweight='bold', color='white')
                
                self.ax.set_xlabel("Values", fontsize=16, fontweight='bold')
                self.ax.set_ylabel("Probability", fontsize=16, fontweight='bold')
                self.ax.set_title(f"Distribution Comparison (N={N_input})", 
                                 fontsize=18, fontweight='bold', pad=20)
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(self.values, fontsize=14)
                self.ax.set_ylim(0, max(max(dv.prob), max(emp_freqs)) * 1.35)
                self.ax.legend(fontsize=14, loc='upper right')
                self.ax.grid(axis='y', alpha=0.3)
                self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def init_normal_tab(self):
        frame_input = ttk.LabelFrame(self.tab_normal, text="Параметры", padding=20)
        frame_input.pack(fill="x", padx=40, pady=20)
        
        ttk.Label(frame_input, text="Mean (μ):", font=self.font_large).grid(row=0, column=0, padx=20, pady=15)
        self.e_mu = ttk.Entry(frame_input, width=14, font=self.font_entry)
        self.e_mu.insert(0, "0")
        self.e_mu.grid(row=0, column=1, padx=10, pady=15, ipady=6)
        
        ttk.Label(frame_input, text="Variance (σ²):", font=self.font_large).grid(row=0, column=2, padx=20, pady=15)
        self.e_var = ttk.Entry(frame_input, width=14, font=self.font_entry)
        self.e_var.insert(0, "1")
        self.e_var.grid(row=0, column=3, padx=10, pady=15, ipady=6)
        
        ttk.Label(frame_input, text="Number of experiments:", font=self.font_large).grid(row=0, column=4, padx=20, pady=15)
        self.e_n_norm = ttk.Entry(frame_input, width=14, font=self.font_entry)
        self.e_n_norm.insert(0, "10000")
        self.e_n_norm.grid(row=0, column=5, padx=10, pady=15, ipady=6)
        
        ttk.Button(frame_input, text="Start", command=self.run_norm).grid(row=1, column=0, columnspan=6, pady=20, ipady=8)

        frame_table = ttk.LabelFrame(self.tab_normal, text="Результаты", padding=15)
        frame_table.pack(fill="x", padx=40, pady=20)
        
        cols = ("N", "Mean", "Mean Err %", "Var", "Var Err %", "Chi-Sq", "Chi-Crit", "Result")
        self.tree_norm = ttk.Treeview(frame_table, columns=cols, show="headings", height=5)
        
        col_widths = {"N": 70, "Mean": 110, "Mean Err %": 120, "Var": 110, 
                      "Var Err %": 120, "Chi-Sq": 100, "Chi-Crit": 100, "Result": 130}
        for c in cols:
            self.tree_norm.heading(c, text=c)
            self.tree_norm.column(c, width=col_widths[c], anchor="center")
        
        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree_norm.yview)
        self.tree_norm.configure(yscrollcommand=scrollbar.set)
        self.tree_norm.pack(side="left", fill="x", expand=True)
        scrollbar.pack(side="right", fill="y")

        frame_graph = ttk.LabelFrame(self.tab_normal, text="Гистограмма + теоретическая кривая (N=10000)", padding=15)
        frame_graph.pack(fill="both", expand=True, padx=40, pady=20)
        
        self.fig_n, self.ax_n = plt.subplots(figsize=(13, 7), dpi=100)
        self.canvas_n = FigureCanvasTkAgg(self.fig_n, master=frame_graph)
        self.canvas_n.get_tk_widget().pack(fill="both", expand=True)
        
        self.ax_n.tick_params(axis='both', labelsize=14)

    def run_norm(self):
        for row in self.tree_norm.get_children():
            self.tree_norm.delete(row)
        
        try:
            mu = float(self.e_mu.get())
            var = float(self.e_var.get())
            
            if var <= 0:
                raise ValueError("дисперсия дожна быть > 0")
            
            sigma = var ** 0.5
            t_mean = mu
            t_var = var
            
            N_input = int(self.e_n_norm.get())
            if N_input < 10 or N_input > 1_000_000_000:
                raise ValueError("N должен быть от 10 и до 1,000,000,000")
            
            N_list = [10, 100, 1000, N_input]
            last_samples = None

            for N in N_list:
                gen = BaseGenerator()
                nrv = NormalRandomVariable(mu, sigma, generator=gen)
                samples = nrv.generate_box_muller(N)
                
                e_mean = np.mean(samples)
                e_var = np.var(samples)
                
                err_m = abs(e_mean - t_mean) / abs(t_mean) * 100 if t_mean != 0 else 0
                err_v = abs(e_var - t_var) / abs(t_var) * 100 if t_var != 0 else 0
                
                chi = nrv.chi_kvadrat_continuous(samples, n_bins=10)
                chi_crit = 16.92
                res = "H0 отвергнута" if chi > chi_crit else "H0 принята"
                
                self.tree_norm.insert("", "end", values=(
                    N, f"{e_mean:.3f}", f"{err_m:.1f}%", f"{e_var:.3f}", 
                    f"{err_v:.1f}%", f"{chi:.2f}", f"{chi_crit:.2f}", res
                ))
                
                if N == N_input:
                    last_samples = samples

            if last_samples is not None:
                self.ax_n.clear()
                
                self.ax_n.hist(last_samples, bins=50, density=True, alpha=0.6, 
                              color='green', edgecolor='black', label='Empirical')
                
                x_min, x_max = self.ax_n.get_xlim()
                x = np.linspace(x_min, x_max, 200)
                
                theoretical_pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * \
                                 np.exp(-((x - mu)**2) / (2 * sigma**2))
                
                self.ax_n.plot(x, theoretical_pdf, 'r-', linewidth=2.5, 
                              label=f'Theoretical (μ={mu}, σ²={var})')
                
                self.ax_n.set_title(f"Normal Distribution (N={N_input})\nMean={mu}, Variance={var}", 
                                   fontsize=18, fontweight='bold', pad=20)
                self.ax_n.set_xlabel("Value", fontsize=16, fontweight='bold')
                self.ax_n.set_ylabel("Density", fontsize=16, fontweight='bold')
                self.ax_n.legend(fontsize=14, loc='upper right')
                self.ax_n.grid(axis='y', alpha=0.3)
                self.canvas_n.draw()
            
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()
