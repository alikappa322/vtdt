using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FormsChernovik
{
    public partial class Form1 : Form
    {
        int[] massiv;
        public Form1()
        {
            InitializeComponent();
            btn_create.Enabled = false;
            btn_sort.Enabled = false;
            this.MaximizeBox = false;
            txt_N.Select();
            btn_clear.Enabled = false;

        }

        private void btn_create_Click(object sender, EventArgs e)
        {
            btn_sort.Enabled = true;

            list_default.Items.Clear();
            Random rnd = new Random();
            int int_N = Convert.ToInt32(txt_N.Text);
            int[] massiv = new int[int_N];
            for (int i = 0; i < int_N; i++)
            {
                massiv[i] = rnd.Next(1, 50);
                list_default.Items.Add(massiv[i].ToString());
            }
        }

        private void btn_sort_Click(object sender, EventArgs e)
        {
            list_sorted.Items.Clear();
            int int_N = Convert.ToInt32(txt_N.Text);
            int[] newmassiv = new int[int_N];
            for (int i = list_default.Items.Count - 1; i >= 0; i--)
            {
                newmassiv[i] = Convert.ToInt32(list_default.Items[i]);
            }

            for (int k = 0; k < newmassiv.Length; k++)
            {
                int mas_pr = newmassiv[k];
                int ind_lev = k;
                for (int j = k + 1; j < newmassiv.Length; j++)
                {
                    if (mas_pr < newmassiv[j])
                    {
                        ind_lev = j;
                        mas_pr = newmassiv[j];
                    }
                }
                newmassiv[ind_lev] = newmassiv[k];
                newmassiv[k] = mas_pr;
            }


            for (int ans = 0; ans < newmassiv.Length; ans++)
            {
                list_sorted.Items.Add(newmassiv[ans].ToString());
            }
            btn_sort.Enabled = false;
        }

        private void txt_N_TextChanged(object sender, EventArgs e)
        {
            //if ()
            if (txt_N.TextLength > 0)
            {
                btn_create.Enabled = true;
                btn_clear.Enabled = true;
            }
            else
            {
                btn_create.Enabled = false;
                btn_clear.Enabled = false;
            }
        }

        private void list_default_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (list_default.Items.Count > 0 || list_sorted.Items.Count > 0)
            {
                btn_clear.Enabled = true;
            }
            else
            {
                btn_clear.Enabled = false;
            }
        }

        private void btn_clear_Click(object sender, EventArgs e)
        {
            txt_N.Clear();
            list_default.Items.Clear();
            list_sorted.Items.Clear();
            btn_create.Enabled = false;
            btn_sort.Enabled = false;
            btn_clear.Enabled = false;
            txt_N.Focus();

        }

        private void list_sorted_SelectedIndexChanged(object sender, EventArgs e)
        {
            int per = list_sorted.Items.Count;
            if (per > 0)
            {
                btn_clear.Enabled = true;
            }
            else
            {
                btn_clear.Enabled = false;
            }
        }
    }
}
