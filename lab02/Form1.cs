using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnStart_Click(object sender, EventArgs e)
        {
            double dt, T0, TL, TR, L, time, rho, c, lambda, dx;
            Stopwatch sw = new Stopwatch();

            dt = (double)inputDelta.Value;
            dx = (double)inputStep.Value;

            T0 = (double)inputStartTemp.Value;
            TL = (double)inputLeft.Value;
            TR = (double)inputRight.Value;
            L = (double)inputWidth.Value;
            time = (double)inputTime.Value;
            rho = (double)inputPlot.Value;
            c = (double)inputHeat.Value;
            lambda = (double)inputLambda.Value;

            if (dx <= 0 || dt <= 0)
            {
                MessageBox.Show("Шаги должны быть больше 0!", "Ошибка",
                               MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            int N = (int)(L / dx) + 1;
            int M = (int)(time / dt);

            if (N > 10000 || M > 1000000)
            {
                    MessageBox.Show($"Слишком мелкие шаги!\nN={N}, M={M}\nУвеличьте шаги.",
                                   "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }

                double[] T = new double[N];
            double[] alpha = new double[N];
            double[] beta = new double[N];

            double A, B, C, F;

            A = C = lambda / (dx * dx);
            B = 2 * lambda / (dx * dx) + rho * c / dt;

            for (int i = 0; i < N; i++)
            {
                T[i] = T0;
            }

            T[0] = TL;
            T[T.Length - 1] = TR;

            sw.Start();
            for (int step = 0; step < M; step++)
            {
                alpha[0] = 0.0;
                beta[0] = TL;

                for (int i = 1; i < N; i++)
                {
                    alpha[i] = A / (B - C * alpha[i - 1]);
                    F = -rho * c * T[i] / dt;
                    beta[i] = (C * beta[i - 1] - F) / (B - C * alpha[i - 1]);
                }

                for (int i = N - 2; i > 0; i--)
                {
                    T[i] = alpha[i] * T[i + 1] + beta[i];
                }

                if (step % 100 == 0 || step == M - 1)
                {
                    chart1.Series[0].Points.Clear();
                    for (int i = 0; i < N; i++)
                    {
                        chart1.Series[0].Points.AddXY(i * dx, T[i]);
                    }
                    chart1.ChartAreas[0].AxisX.Minimum = 0;
                    chart1.ChartAreas[0].AxisX.Maximum = L;
                    chart1.ChartAreas[0].AxisX.Title = "Координата x, м";
                    chart1.ChartAreas[0].AxisY.Title = "Температура T, °C";
                    Application.DoEvents();
                }
            }
            sw.Stop();

            int centerIndex = N / 2;
            double TCenter = T[centerIndex];
            double realTime = sw.Elapsed.TotalSeconds;
            dataGridResults.Rows.Add(dx, dt, TCenter, realTime);
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            dataGridResults.Rows.Clear();
        }
    }
    }