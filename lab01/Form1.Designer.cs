namespace WindowsFormsApp1
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.btLaunch = new System.Windows.Forms.Button();
            this.inputHeight = new System.Windows.Forms.NumericUpDown();
            this.inputAngle = new System.Windows.Forms.NumericUpDown();
            this.inputSpeed = new System.Windows.Forms.NumericUpDown();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.inputStep = new System.Windows.Forms.NumericUpDown();
            this.btClear = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.lblMaxHeight = new System.Windows.Forms.Label();
            this.lblDistance = new System.Windows.Forms.Label();
            this.lblFinalSpeed = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.inputWeight = new System.Windows.Forms.NumericUpDown();
            this.inputSize = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.inputHeight)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputAngle)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputSpeed)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputStep)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputWeight)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputSize)).BeginInit();
            this.SuspendLayout();
            // 
            // btLaunch
            // 
            this.btLaunch.BackColor = System.Drawing.Color.DarkKhaki;
            this.btLaunch.FlatAppearance.BorderColor = System.Drawing.Color.OliveDrab;
            this.btLaunch.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btLaunch.Font = new System.Drawing.Font("Verdana", 8.142858F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.btLaunch.Location = new System.Drawing.Point(534, 78);
            this.btLaunch.Name = "btLaunch";
            this.btLaunch.Size = new System.Drawing.Size(131, 38);
            this.btLaunch.TabIndex = 0;
            this.btLaunch.Text = "Launch";
            this.btLaunch.UseVisualStyleBackColor = false;
            this.btLaunch.Click += new System.EventHandler(this.btLaunch_Click);
            // 
            // inputHeight
            // 
            this.inputHeight.Location = new System.Drawing.Point(138, 19);
            this.inputHeight.Name = "inputHeight";
            this.inputHeight.Size = new System.Drawing.Size(120, 29);
            this.inputHeight.TabIndex = 1;
            // 
            // inputAngle
            // 
            this.inputAngle.Location = new System.Drawing.Point(138, 52);
            this.inputAngle.Name = "inputAngle";
            this.inputAngle.Size = new System.Drawing.Size(120, 29);
            this.inputAngle.TabIndex = 2;
            // 
            // inputSpeed
            // 
            this.inputSpeed.Location = new System.Drawing.Point(138, 87);
            this.inputSpeed.Name = "inputSpeed";
            this.inputSpeed.Size = new System.Drawing.Size(120, 29);
            this.inputSpeed.TabIndex = 3;
            // 
            // chart1
            // 
            chartArea1.AxisX.LabelStyle.Format = "0";
            chartArea1.AxisY.LabelStyle.Format = "0";
            chartArea1.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chart1.Legends.Add(legend1);
            this.chart1.Location = new System.Drawing.Point(12, 136);
            this.chart1.Name = "chart1";
            series1.ChartArea = "ChartArea1";
            series1.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series1.Legend = "Legend1";
            series1.LegendText = "trajectory";
            series1.Name = "Series1";
            this.chart1.Series.Add(series1);
            this.chart1.Size = new System.Drawing.Size(974, 566);
            this.chart1.TabIndex = 5;
            this.chart1.Text = "chart1";
            // 
            // inputStep
            // 
            this.inputStep.DecimalPlaces = 4;
            this.inputStep.Location = new System.Drawing.Point(370, 85);
            this.inputStep.Name = "inputStep";
            this.inputStep.Size = new System.Drawing.Size(120, 29);
            this.inputStep.TabIndex = 7;
            // 
            // btClear
            // 
            this.btClear.BackColor = System.Drawing.Color.RosyBrown;
            this.btClear.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(192)))));
            this.btClear.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.btClear.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btClear.Font = new System.Drawing.Font("Verdana", 8.142858F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.btClear.Location = new System.Drawing.Point(858, 78);
            this.btClear.Name = "btClear";
            this.btClear.Size = new System.Drawing.Size(128, 38);
            this.btClear.TabIndex = 8;
            this.btClear.Text = "Clear";
            this.btClear.UseVisualStyleBackColor = false;
            this.btClear.Click += new System.EventHandler(this.btClear_Click);
            // 
            // timer1
            // 
            this.timer1.Interval = 20;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(49, 21);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(68, 25);
            this.label1.TabIndex = 9;
            this.label1.Text = "Height";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(49, 56);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(63, 25);
            this.label2.TabIndex = 10;
            this.label2.Text = "Angle";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(49, 89);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(70, 25);
            this.label3.TabIndex = 11;
            this.label3.Text = "Speed";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(290, 89);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(53, 25);
            this.label6.TabIndex = 14;
            this.label6.Text = "Step";
            // 
            // lblMaxHeight
            // 
            this.lblMaxHeight.AutoSize = true;
            this.lblMaxHeight.Location = new System.Drawing.Point(766, 412);
            this.lblMaxHeight.Name = "lblMaxHeight";
            this.lblMaxHeight.Size = new System.Drawing.Size(111, 25);
            this.lblMaxHeight.TabIndex = 15;
            this.lblMaxHeight.Text = "Max Height";
            // 
            // lblDistance
            // 
            this.lblDistance.AutoSize = true;
            this.lblDistance.Location = new System.Drawing.Point(766, 451);
            this.lblDistance.Name = "lblDistance";
            this.lblDistance.Size = new System.Drawing.Size(88, 25);
            this.lblDistance.TabIndex = 16;
            this.lblDistance.Text = "Distance";
            // 
            // lblFinalSpeed
            // 
            this.lblFinalSpeed.AutoSize = true;
            this.lblFinalSpeed.Location = new System.Drawing.Point(766, 492);
            this.lblFinalSpeed.Name = "lblFinalSpeed";
            this.lblFinalSpeed.Size = new System.Drawing.Size(117, 25);
            this.lblFinalSpeed.TabIndex = 17;
            this.lblFinalSpeed.Text = "Final Speed";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(290, 21);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(74, 25);
            this.label4.TabIndex = 18;
            this.label4.Text = "Weight";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(290, 54);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(51, 25);
            this.label5.TabIndex = 19;
            this.label5.Text = "Size";
            // 
            // inputWeight
            // 
            this.inputWeight.Location = new System.Drawing.Point(370, 17);
            this.inputWeight.Name = "inputWeight";
            this.inputWeight.Size = new System.Drawing.Size(120, 29);
            this.inputWeight.TabIndex = 20;
            // 
            // inputSize
            // 
            this.inputSize.DecimalPlaces = 4;
            this.inputSize.Location = new System.Drawing.Point(370, 52);
            this.inputSize.Name = "inputSize";
            this.inputSize.Size = new System.Drawing.Size(120, 29);
            this.inputSize.TabIndex = 21;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(11F, 24F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1018, 738);
            this.Controls.Add(this.inputSize);
            this.Controls.Add(this.inputWeight);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.lblFinalSpeed);
            this.Controls.Add(this.lblDistance);
            this.Controls.Add(this.lblMaxHeight);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btClear);
            this.Controls.Add(this.inputStep);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.inputSpeed);
            this.Controls.Add(this.inputAngle);
            this.Controls.Add(this.inputHeight);
            this.Controls.Add(this.btLaunch);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.inputHeight)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputAngle)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputSpeed)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputStep)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputWeight)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputSize)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btLaunch;
        private System.Windows.Forms.NumericUpDown inputHeight;
        private System.Windows.Forms.NumericUpDown inputAngle;
        private System.Windows.Forms.NumericUpDown inputSpeed;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.NumericUpDown inputStep;
        private System.Windows.Forms.Button btClear;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label lblMaxHeight;
        private System.Windows.Forms.Label lblDistance;
        private System.Windows.Forms.Label lblFinalSpeed;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.NumericUpDown inputWeight;
        private System.Windows.Forms.NumericUpDown inputSize;
    }
}

