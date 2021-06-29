
namespace Calculadora
{
    partial class Calculadora
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.txtInput = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.btnZero = new System.Windows.Forms.Button();
            this.btnTres = new System.Windows.Forms.Button();
            this.btnDois = new System.Windows.Forms.Button();
            this.btnUm = new System.Windows.Forms.Button();
            this.btnSeis = new System.Windows.Forms.Button();
            this.btnCinco = new System.Windows.Forms.Button();
            this.btnQuatro = new System.Windows.Forms.Button();
            this.btnResult = new System.Windows.Forms.Button();
            this.btnSoma = new System.Windows.Forms.Button();
            this.btnSubtrai = new System.Windows.Forms.Button();
            this.btnMultiplica = new System.Windows.Forms.Button();
            this.btnNove = new System.Windows.Forms.Button();
            this.btnOito = new System.Windows.Forms.Button();
            this.btnSete = new System.Windows.Forms.Button();
            this.btnDivide = new System.Windows.Forms.Button();
            this.btnApaga = new System.Windows.Forms.Button();
            this.linkLabel1 = new System.Windows.Forms.LinkLabel();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // txtInput
            // 
            this.txtInput.Enabled = false;
            this.txtInput.Location = new System.Drawing.Point(12, 29);
            this.txtInput.MaxLength = 7;
            this.txtInput.Name = "txtInput";
            this.txtInput.Size = new System.Drawing.Size(248, 23);
            this.txtInput.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(101, 11);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(70, 15);
            this.label1.TabIndex = 1;
            this.label1.Text = "Calculadora";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.btnZero);
            this.groupBox1.Controls.Add(this.btnTres);
            this.groupBox1.Controls.Add(this.btnDois);
            this.groupBox1.Controls.Add(this.btnUm);
            this.groupBox1.Controls.Add(this.btnSeis);
            this.groupBox1.Controls.Add(this.btnCinco);
            this.groupBox1.Controls.Add(this.btnQuatro);
            this.groupBox1.Controls.Add(this.btnResult);
            this.groupBox1.Controls.Add(this.btnSoma);
            this.groupBox1.Controls.Add(this.btnSubtrai);
            this.groupBox1.Controls.Add(this.btnMultiplica);
            this.groupBox1.Controls.Add(this.btnNove);
            this.groupBox1.Controls.Add(this.btnOito);
            this.groupBox1.Controls.Add(this.btnSete);
            this.groupBox1.Controls.Add(this.btnDivide);
            this.groupBox1.Controls.Add(this.btnApaga);
            this.groupBox1.Location = new System.Drawing.Point(12, 58);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(248, 186);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Ferramentas";
            // 
            // btnZero
            // 
            this.btnZero.Location = new System.Drawing.Point(6, 138);
            this.btnZero.Name = "btnZero";
            this.btnZero.Size = new System.Drawing.Size(175, 23);
            this.btnZero.TabIndex = 18;
            this.btnZero.Text = "0";
            this.btnZero.UseVisualStyleBackColor = true;
            this.btnZero.Click += new System.EventHandler(this.btnZero_Click);
            // 
            // btnTres
            // 
            this.btnTres.Location = new System.Drawing.Point(126, 109);
            this.btnTres.Name = "btnTres";
            this.btnTres.Size = new System.Drawing.Size(58, 23);
            this.btnTres.TabIndex = 17;
            this.btnTres.Text = "3";
            this.btnTres.UseVisualStyleBackColor = true;
            this.btnTres.Click += new System.EventHandler(this.btnTres_Click);
            // 
            // btnDois
            // 
            this.btnDois.Location = new System.Drawing.Point(66, 109);
            this.btnDois.Name = "btnDois";
            this.btnDois.Size = new System.Drawing.Size(58, 23);
            this.btnDois.TabIndex = 16;
            this.btnDois.Text = "2";
            this.btnDois.UseVisualStyleBackColor = true;
            this.btnDois.Click += new System.EventHandler(this.btnDois_Click);
            // 
            // btnUm
            // 
            this.btnUm.Location = new System.Drawing.Point(6, 109);
            this.btnUm.Name = "btnUm";
            this.btnUm.Size = new System.Drawing.Size(58, 23);
            this.btnUm.TabIndex = 15;
            this.btnUm.Text = "1";
            this.btnUm.UseVisualStyleBackColor = true;
            this.btnUm.Click += new System.EventHandler(this.btnUm_Click);
            // 
            // btnSeis
            // 
            this.btnSeis.Location = new System.Drawing.Point(126, 80);
            this.btnSeis.Name = "btnSeis";
            this.btnSeis.Size = new System.Drawing.Size(58, 23);
            this.btnSeis.TabIndex = 14;
            this.btnSeis.Text = "6";
            this.btnSeis.UseVisualStyleBackColor = true;
            this.btnSeis.Click += new System.EventHandler(this.btnSeis_Click);
            // 
            // btnCinco
            // 
            this.btnCinco.Location = new System.Drawing.Point(66, 80);
            this.btnCinco.Name = "btnCinco";
            this.btnCinco.Size = new System.Drawing.Size(58, 23);
            this.btnCinco.TabIndex = 13;
            this.btnCinco.Text = "5";
            this.btnCinco.UseVisualStyleBackColor = true;
            this.btnCinco.Click += new System.EventHandler(this.btnCinco_Click);
            // 
            // btnQuatro
            // 
            this.btnQuatro.Location = new System.Drawing.Point(6, 80);
            this.btnQuatro.Name = "btnQuatro";
            this.btnQuatro.Size = new System.Drawing.Size(58, 23);
            this.btnQuatro.TabIndex = 12;
            this.btnQuatro.Text = "4";
            this.btnQuatro.UseVisualStyleBackColor = true;
            this.btnQuatro.Click += new System.EventHandler(this.btnQuatro_Click);
            // 
            // btnResult
            // 
            this.btnResult.Location = new System.Drawing.Point(187, 138);
            this.btnResult.Name = "btnResult";
            this.btnResult.Size = new System.Drawing.Size(58, 23);
            this.btnResult.TabIndex = 11;
            this.btnResult.Text = "=";
            this.btnResult.UseVisualStyleBackColor = true;
            this.btnResult.Click += new System.EventHandler(this.btnResult_Click);
            // 
            // btnSoma
            // 
            this.btnSoma.Location = new System.Drawing.Point(187, 109);
            this.btnSoma.Name = "btnSoma";
            this.btnSoma.Size = new System.Drawing.Size(58, 23);
            this.btnSoma.TabIndex = 10;
            this.btnSoma.Text = "+";
            this.btnSoma.UseVisualStyleBackColor = true;
            this.btnSoma.Click += new System.EventHandler(this.btnSoma_Click);
            // 
            // btnSubtrai
            // 
            this.btnSubtrai.Location = new System.Drawing.Point(187, 80);
            this.btnSubtrai.Name = "btnSubtrai";
            this.btnSubtrai.Size = new System.Drawing.Size(58, 23);
            this.btnSubtrai.TabIndex = 9;
            this.btnSubtrai.Text = "-";
            this.btnSubtrai.UseVisualStyleBackColor = true;
            this.btnSubtrai.Click += new System.EventHandler(this.btnSubtrai_Click);
            // 
            // btnMultiplica
            // 
            this.btnMultiplica.Location = new System.Drawing.Point(187, 51);
            this.btnMultiplica.Name = "btnMultiplica";
            this.btnMultiplica.Size = new System.Drawing.Size(58, 23);
            this.btnMultiplica.TabIndex = 8;
            this.btnMultiplica.Text = "X";
            this.btnMultiplica.UseVisualStyleBackColor = true;
            this.btnMultiplica.Click += new System.EventHandler(this.btnMultiplica_Click);
            // 
            // btnNove
            // 
            this.btnNove.Location = new System.Drawing.Point(126, 51);
            this.btnNove.Name = "btnNove";
            this.btnNove.Size = new System.Drawing.Size(58, 23);
            this.btnNove.TabIndex = 7;
            this.btnNove.Text = "9";
            this.btnNove.UseVisualStyleBackColor = true;
            this.btnNove.Click += new System.EventHandler(this.btnNove_Click);
            // 
            // btnOito
            // 
            this.btnOito.Location = new System.Drawing.Point(66, 51);
            this.btnOito.Name = "btnOito";
            this.btnOito.Size = new System.Drawing.Size(58, 23);
            this.btnOito.TabIndex = 6;
            this.btnOito.Text = "8";
            this.btnOito.UseVisualStyleBackColor = true;
            this.btnOito.Click += new System.EventHandler(this.btnOito_Click);
            // 
            // btnSete
            // 
            this.btnSete.Location = new System.Drawing.Point(6, 51);
            this.btnSete.Name = "btnSete";
            this.btnSete.Size = new System.Drawing.Size(58, 23);
            this.btnSete.TabIndex = 5;
            this.btnSete.Text = "7";
            this.btnSete.UseVisualStyleBackColor = true;
            this.btnSete.Click += new System.EventHandler(this.btnSete_Click);
            // 
            // btnDivide
            // 
            this.btnDivide.Location = new System.Drawing.Point(187, 22);
            this.btnDivide.Name = "btnDivide";
            this.btnDivide.Size = new System.Drawing.Size(58, 23);
            this.btnDivide.TabIndex = 4;
            this.btnDivide.Text = "/";
            this.btnDivide.UseVisualStyleBackColor = true;
            this.btnDivide.Click += new System.EventHandler(this.btnDivide_Click);
            // 
            // btnApaga
            // 
            this.btnApaga.Location = new System.Drawing.Point(6, 22);
            this.btnApaga.Name = "btnApaga";
            this.btnApaga.Size = new System.Drawing.Size(178, 23);
            this.btnApaga.TabIndex = 3;
            this.btnApaga.Text = "AC";
            this.btnApaga.UseVisualStyleBackColor = true;
            this.btnApaga.Click += new System.EventHandler(this.btnApaga_Click);
            // 
            // linkLabel1
            // 
            this.linkLabel1.AutoSize = true;
            this.linkLabel1.Location = new System.Drawing.Point(53, 256);
            this.linkLabel1.Name = "linkLabel1";
            this.linkLabel1.Size = new System.Drawing.Size(167, 15);
            this.linkLabel1.TabIndex = 3;
            this.linkLabel1.TabStop = true;
            this.linkLabel1.Text = "Desenvolvido por: Gabriel Jose";
            // 
            // Calculadora
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(272, 280);
            this.Controls.Add(this.linkLabel1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txtInput);
            this.Name = "Calculadora";
            this.Text = "Calculadora";
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtInput;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button btnZero;
        private System.Windows.Forms.Button btnTres;
        private System.Windows.Forms.Button btnDois;
        private System.Windows.Forms.Button btnUm;
        private System.Windows.Forms.Button btnSeis;
        private System.Windows.Forms.Button btnCinco;
        private System.Windows.Forms.Button btnQuatro;
        private System.Windows.Forms.Button btnResult;
        private System.Windows.Forms.Button btnSoma;
        private System.Windows.Forms.Button btnSubtrai;
        private System.Windows.Forms.Button btnMultiplica;
        private System.Windows.Forms.Button btnNove;
        private System.Windows.Forms.Button btnOito;
        private System.Windows.Forms.Button btnSete;
        private System.Windows.Forms.Button btnDivide;
        private System.Windows.Forms.Button btnApaga;
        private System.Windows.Forms.LinkLabel linkLabel1;
    }
}

