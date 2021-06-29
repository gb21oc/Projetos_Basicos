using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculadora
{
    public partial class Calculadora : Form
    {
        float number, result;
        string operation;
        bool isOperation = false;
        public Calculadora()
        {
            InitializeComponent();
        }

        private void btnApaga_Click(object sender, EventArgs e)
        {
            txtInput.Text = "";
            isOperation = false;
        }
        private void btnZero_Click(object sender, EventArgs e)
        {
            txtInput.Text += btnZero.Text;
        }
        private void btnUm_Click(object sender, EventArgs e)
        {
            txtInput.Text += btnUm.Text;
        }

        private void btnDois_Click(object sender, EventArgs e)
        {
            txtInput.Text += btnDois.Text;
        }

        private void btnTres_Click(object sender, EventArgs e)
        {
            txtInput.Text += btnTres.Text;
        }
        private void btnQuatro_Click(object sender, EventArgs e)
        {
            txtInput.Text += btnQuatro.Text;
        }
        private void btnCinco_Click(object sender, EventArgs e)
        {
            txtInput.Text += btnCinco.Text;
        }
        private void btnSeis_Click(object sender, EventArgs e)
        {
            txtInput.Text += btnSeis.Text;
        }

        private void btnSete_Click(object sender, EventArgs e)
        {
            txtInput.Text += btnSete.Text;
        }
        private void btnOito_Click(object sender, EventArgs e)
        {
            txtInput.Text += btnOito.Text;
        }
        private void btnNove_Click(object sender, EventArgs e)
        {
            txtInput.Text += btnNove.Text;
        }

        private void btnSoma_Click(object sender, EventArgs e)
        {
            operation = btnSoma.Text;
            if (!isOperation)
            {
                number = float.Parse(txtInput.Text);
                txtInput.Clear();
                txtInput.Focus();
                isOperation = true;
            }
        }

        private void btnSubtrai_Click(object sender, EventArgs e)
        {
            operation = btnSubtrai.Text;
            if (!isOperation)
            {
                number = float.Parse(txtInput.Text);
                txtInput.Clear();
                txtInput.Focus();
                isOperation = true;
            }
        }

        private void btnMultiplica_Click(object sender, EventArgs e)
        {
            operation = btnMultiplica.Text;
            if (!isOperation)
            {
                number = float.Parse(txtInput.Text);
                txtInput.Clear();
                txtInput.Focus();
                isOperation = true;
            }
        }

        private void btnDivide_Click(object sender, EventArgs e)
        {
            operation = btnDivide.Text;
            if (!isOperation)
            {
                number = float.Parse(txtInput.Text);
                txtInput.Clear();
                txtInput.Focus();
                isOperation = true;
            }
        }

        private void btnResult_Click(object sender, EventArgs e)
        {
            switch (operation)
            {
                case "+":
                    result = number + float.Parse(txtInput.Text);
                    txtInput.Text = result.ToString();
                    isOperation = false;
                    break;
                case "-":
                    result = number - float.Parse(txtInput.Text);
                    txtInput.Text = result.ToString();
                    isOperation = false;
                    break;
                case "X":
                    result = number * float.Parse(txtInput.Text);
                    txtInput.Text = result.ToString();
                    isOperation = false;
                    break;
                case "/":
                    result = number / float.Parse(txtInput.Text);
                    txtInput.Text = result.ToString();
                    isOperation = false;
                    break;
            }
        }
    }
}
