namespace WindowsFormsApp2
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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea4 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend4 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series4 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.label1 = new System.Windows.Forms.Label();
            this.inputDelta = new System.Windows.Forms.NumericUpDown();
            this.label2 = new System.Windows.Forms.Label();
            this.inputStep = new System.Windows.Forms.NumericUpDown();
            this.label3 = new System.Windows.Forms.Label();
            this.inputStartTemp = new System.Windows.Forms.NumericUpDown();
            this.label4 = new System.Windows.Forms.Label();
            this.inputLeft = new System.Windows.Forms.NumericUpDown();
            this.label5 = new System.Windows.Forms.Label();
            this.inputRight = new System.Windows.Forms.NumericUpDown();
            this.label6 = new System.Windows.Forms.Label();
            this.inputWidth = new System.Windows.Forms.NumericUpDown();
            this.label7 = new System.Windows.Forms.Label();
            this.inputTime = new System.Windows.Forms.NumericUpDown();
            this.label8 = new System.Windows.Forms.Label();
            this.inputPlot = new System.Windows.Forms.NumericUpDown();
            this.label9 = new System.Windows.Forms.Label();
            this.inputHeat = new System.Windows.Forms.NumericUpDown();
            this.label10 = new System.Windows.Forms.Label();
            this.inputLambda = new System.Windows.Forms.NumericUpDown();
            this.btnStart = new System.Windows.Forms.Button();
            this.btnClear = new System.Windows.Forms.Button();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.dataGridResults = new System.Windows.Forms.DataGridView();
            this.colSpaceStep = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colTimeStep = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colTempCenter = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colExecTime = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.inputDelta)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputStep)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputStartTemp)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputLeft)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputRight)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputWidth)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputTime)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputPlot)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputHeat)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputLambda)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridResults)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(186, 25);
            this.label1.TabIndex = 0;
            this.label1.Text = "Шаг по времени, с:";
            // 
            // inputDelta
            // 
            this.inputDelta.DecimalPlaces = 4;
            this.inputDelta.Increment = new decimal(new int[] {
            1,
            0,
            0,
            196608});
            this.inputDelta.Location = new System.Drawing.Point(300, 13);
            this.inputDelta.Name = "inputDelta";
            this.inputDelta.Size = new System.Drawing.Size(120, 29);
            this.inputDelta.TabIndex = 1;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(13, 52);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(239, 25);
            this.label2.TabIndex = 2;
            this.label2.Text = "Шаг по пространству, м:";
            // 
            // inputStep
            // 
            this.inputStep.DecimalPlaces = 4;
            this.inputStep.Increment = new decimal(new int[] {
            1,
            0,
            0,
            196608});
            this.inputStep.Location = new System.Drawing.Point(300, 48);
            this.inputStep.Name = "inputStep";
            this.inputStep.Size = new System.Drawing.Size(120, 29);
            this.inputStep.TabIndex = 3;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(13, 84);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(273, 25);
            this.label3.TabIndex = 4;
            this.label3.Text = "Начальная температура, °C";
            // 
            // inputStartTemp
            // 
            this.inputStartTemp.Location = new System.Drawing.Point(300, 84);
            this.inputStartTemp.Maximum = new decimal(new int[] {
            5000,
            0,
            0,
            0});
            this.inputStartTemp.Minimum = new decimal(new int[] {
            5000,
            0,
            0,
            -2147483648});
            this.inputStartTemp.Name = "inputStartTemp";
            this.inputStartTemp.Size = new System.Drawing.Size(120, 29);
            this.inputStartTemp.TabIndex = 5;
            this.inputStartTemp.Value = new decimal(new int[] {
            20,
            0,
            0,
            0});
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(13, 119);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(234, 25);
            this.label4.TabIndex = 6;
            this.label4.Text = "Температура слева, °C:";
            // 
            // inputLeft
            // 
            this.inputLeft.Location = new System.Drawing.Point(300, 119);
            this.inputLeft.Maximum = new decimal(new int[] {
            5000,
            0,
            0,
            0});
            this.inputLeft.Minimum = new decimal(new int[] {
            5000,
            0,
            0,
            -2147483648});
            this.inputLeft.Name = "inputLeft";
            this.inputLeft.Size = new System.Drawing.Size(120, 29);
            this.inputLeft.TabIndex = 7;
            this.inputLeft.Value = new decimal(new int[] {
            100,
            0,
            0,
            -2147483648});
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(13, 155);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(243, 25);
            this.label5.TabIndex = 8;
            this.label5.Text = "Температура справа, °C:";
            // 
            // inputRight
            // 
            this.inputRight.Location = new System.Drawing.Point(300, 155);
            this.inputRight.Maximum = new decimal(new int[] {
            5000,
            0,
            0,
            0});
            this.inputRight.Minimum = new decimal(new int[] {
            5000,
            0,
            0,
            -2147483648});
            this.inputRight.Name = "inputRight";
            this.inputRight.Size = new System.Drawing.Size(120, 29);
            this.inputRight.TabIndex = 9;
            this.inputRight.Value = new decimal(new int[] {
            70,
            0,
            0,
            0});
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 190);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(225, 25);
            this.label6.TabIndex = 10;
            this.label6.Text = "Толщина пластины, м:";
            // 
            // inputWidth
            // 
            this.inputWidth.DecimalPlaces = 3;
            this.inputWidth.Location = new System.Drawing.Point(300, 190);
            this.inputWidth.Name = "inputWidth";
            this.inputWidth.Size = new System.Drawing.Size(120, 29);
            this.inputWidth.TabIndex = 11;
            this.inputWidth.Value = new decimal(new int[] {
            1,
            0,
            0,
            65536});
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(13, 225);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(254, 25);
            this.label7.TabIndex = 12;
            this.label7.Text = "Время моделирования, с:";
            // 
            // inputTime
            // 
            this.inputTime.Location = new System.Drawing.Point(300, 225);
            this.inputTime.Name = "inputTime";
            this.inputTime.Size = new System.Drawing.Size(120, 29);
            this.inputTime.TabIndex = 13;
            this.inputTime.Value = new decimal(new int[] {
            10,
            0,
            0,
            0});
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(13, 260);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(179, 25);
            this.label8.TabIndex = 14;
            this.label8.Text = "Плотность, кг/м³:";
            // 
            // inputPlot
            // 
            this.inputPlot.Location = new System.Drawing.Point(300, 260);
            this.inputPlot.Maximum = new decimal(new int[] {
            10000000,
            0,
            0,
            0});
            this.inputPlot.Name = "inputPlot";
            this.inputPlot.Size = new System.Drawing.Size(120, 29);
            this.inputPlot.TabIndex = 15;
            this.inputPlot.Value = new decimal(new int[] {
            7800,
            0,
            0,
            0});
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(13, 297);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(266, 25);
            this.label9.TabIndex = 16;
            this.label9.Text = "Теплоемкость, Дж/(кг·°C):";
            // 
            // inputHeat
            // 
            this.inputHeat.Location = new System.Drawing.Point(300, 295);
            this.inputHeat.Maximum = new decimal(new int[] {
            10000000,
            0,
            0,
            0});
            this.inputHeat.Name = "inputHeat";
            this.inputHeat.Size = new System.Drawing.Size(120, 29);
            this.inputHeat.TabIndex = 17;
            this.inputHeat.Value = new decimal(new int[] {
            460,
            0,
            0,
            0});
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(13, 338);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(294, 25);
            this.label10.TabIndex = 18;
            this.label10.Text = "Теплопроводность, Вт/(м·°C):";
            // 
            // inputLambda
            // 
            this.inputLambda.Location = new System.Drawing.Point(300, 334);
            this.inputLambda.Maximum = new decimal(new int[] {
            10000,
            0,
            0,
            0});
            this.inputLambda.Name = "inputLambda";
            this.inputLambda.Size = new System.Drawing.Size(120, 29);
            this.inputLambda.TabIndex = 0;
            this.inputLambda.Value = new decimal(new int[] {
            46,
            0,
            0,
            0});
            // 
            // btnStart
            // 
            this.btnStart.Location = new System.Drawing.Point(480, 17);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(174, 92);
            this.btnStart.TabIndex = 19;
            this.btnStart.Text = "Запуск";
            this.btnStart.UseVisualStyleBackColor = true;
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
            // 
            // btnClear
            // 
            this.btnClear.Location = new System.Drawing.Point(749, 13);
            this.btnClear.Name = "btnClear";
            this.btnClear.Size = new System.Drawing.Size(168, 96);
            this.btnClear.TabIndex = 20;
            this.btnClear.Text = "Очистка";
            this.btnClear.UseVisualStyleBackColor = true;
            this.btnClear.Click += new System.EventHandler(this.btnClear_Click);
            // 
            // chart1
            // 
            chartArea4.AxisX.Title = "Координата x, м";
            chartArea4.AxisY.Title = "Температура T, °C";
            chartArea4.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea4);
            legend4.Name = "Legend1";
            this.chart1.Legends.Add(legend4);
            this.chart1.Location = new System.Drawing.Point(18, 450);
            this.chart1.Name = "chart1";
            series4.ChartArea = "ChartArea1";
            series4.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series4.Legend = "Legend1";
            series4.Name = "Series1";
            this.chart1.Series.Add(series4);
            this.chart1.Size = new System.Drawing.Size(1261, 767);
            this.chart1.TabIndex = 21;
            this.chart1.Text = "chart1";
            // 
            // dataGridResults
            // 
            this.dataGridResults.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridResults.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.colSpaceStep,
            this.colTimeStep,
            this.colTempCenter,
            this.colExecTime});
            this.dataGridResults.Location = new System.Drawing.Point(481, 119);
            this.dataGridResults.Name = "dataGridResults";
            this.dataGridResults.RowHeadersWidth = 72;
            this.dataGridResults.RowTemplate.Height = 31;
            this.dataGridResults.Size = new System.Drawing.Size(1302, 316);
            this.dataGridResults.TabIndex = 22;
            // 
            // colSpaceStep
            // 
            this.colSpaceStep.HeaderText = "Шаг по пространству";
            this.colSpaceStep.MinimumWidth = 9;
            this.colSpaceStep.Name = "colSpaceStep";
            this.colSpaceStep.Width = 175;
            // 
            // colTimeStep
            // 
            this.colTimeStep.HeaderText = "Шаг по времени";
            this.colTimeStep.MinimumWidth = 9;
            this.colTimeStep.Name = "colTimeStep";
            this.colTimeStep.Width = 175;
            // 
            // colTempCenter
            // 
            this.colTempCenter.HeaderText = "Температура в центральной точке";
            this.colTempCenter.MinimumWidth = 9;
            this.colTempCenter.Name = "colTempCenter";
            this.colTempCenter.Width = 175;
            // 
            // colExecTime
            // 
            this.colExecTime.HeaderText = "Время выполнения, с";
            this.colExecTime.MinimumWidth = 9;
            this.colExecTime.Name = "colExecTime";
            this.colExecTime.Width = 175;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(11F, 24F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1812, 1323);
            this.Controls.Add(this.dataGridResults);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.btnClear);
            this.Controls.Add(this.btnStart);
            this.Controls.Add(this.inputLambda);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.inputHeat);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.inputPlot);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.inputTime);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.inputWidth);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.inputRight);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.inputLeft);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.inputStartTemp);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.inputStep);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.inputDelta);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.inputDelta)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputStep)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputStartTemp)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputLeft)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputRight)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputWidth)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputTime)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputPlot)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputHeat)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputLambda)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridResults)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.NumericUpDown inputDelta;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.NumericUpDown inputStep;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.NumericUpDown inputStartTemp;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.NumericUpDown inputLeft;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.NumericUpDown inputRight;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.NumericUpDown inputWidth;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.NumericUpDown inputTime;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.NumericUpDown inputPlot;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.NumericUpDown inputHeat;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.NumericUpDown inputLambda;
        private System.Windows.Forms.Button btnStart;
        private System.Windows.Forms.Button btnClear;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.DataGridView dataGridResults;
        private System.Windows.Forms.DataGridViewTextBoxColumn colSpaceStep;
        private System.Windows.Forms.DataGridViewTextBoxColumn colTimeStep;
        private System.Windows.Forms.DataGridViewTextBoxColumn colTempCenter;
        private System.Windows.Forms.DataGridViewTextBoxColumn colExecTime;
    }
}

