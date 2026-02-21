using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        Series currentSeries;
        decimal t, x, y, v0, cosa, sina, dt, MaxHeight, S, m, k, vx, vy;
        int stepCounter = 0;
        const decimal g = 9.81M, rho = 1.29M, C = 0.15M;

        public Form1()
        {
            InitializeComponent();
        }

        private void btLaunch_Click(object sender, EventArgs e)
        {
            chart1.ChartAreas[0].AxisY.Minimum = 0;
            if (!timer1.Enabled)
            {
                t = 0;
                x = 0;
                MaxHeight = y;
                stepCounter = 0;

                y = inputHeight.Value;
                v0 = inputSpeed.Value;
                dt = inputStep.Value;

                double a = (double)inputAngle.Value * Math.PI / 180;
                cosa = (decimal)Math.Cos(a);
                sina = (decimal)Math.Sin(a);
                S = inputSize.Value;
                m = inputWeight.Value;

                k = 0.5M * C * rho * S / m;
                vx = v0 * cosa;
                vy = v0 * sina;

                string seriesName = "Step " + dt.ToString() + " #" + (chart1.Series.Count + 1);
                currentSeries = chart1.Series.Add(seriesName);

                currentSeries.ChartType = SeriesChartType.Line;
                currentSeries.BorderWidth = 3;

                currentSeries.Points.AddXY(x, y);
                timer1.Start();
                if (dt == 0.0001M || dt == 1M)
                    timer1.Interval = 20;
                else
                    timer1.Interval = (int)(dt * 1000);
            }
        }

        private void btClear_Click(object sender, EventArgs e)
        {
            chart1.Series.Clear();
            stepCounter = 0;

            lblDistance.Text = "Distance: -";
            lblMaxHeight.Text = "Max height: -";
            lblFinalSpeed.Text = "Final speed: -";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            t += dt;
            decimal v = (decimal)Math.Sqrt((double)(vx * vx + vy * vy));

            vx = vx - k * vx * v * dt;
            vy = vy - (g + k * vy * v) * dt;

            x = x + vx * dt;
            y = y + vy * dt;
            stepCounter++;
            if (dt >= 0.1M)
            {
                currentSeries.Points.AddXY(x, y);
            }
            else
            {
                if (stepCounter % 100 == 0)
                    currentSeries.Points.AddXY(x, y);
            }

            if (y > MaxHeight) MaxHeight = y;
            if (y <= 0)
            {
                timer1.Stop();
                y = 0;

                currentSeries.Points.AddXY(x, y);

                lblDistance.Text = "Distance: " + Math.Round(x, 2).ToString() + " m";
                lblMaxHeight.Text = "Max height: " + Math.Round(MaxHeight, 2).ToString() + " m";
                lblFinalSpeed.Text = "Final speed: " + Math.Round((decimal)v, 2).ToString() + " m/s";
            }

        }
    }
}