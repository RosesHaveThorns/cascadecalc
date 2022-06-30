import tkinter as tk
import tkinter.ttk as ttk

class Cascade():

    NUM_MODULES_PER_YEAR = 12

    def __init__(self):
        ## tkinter window setup
        self.window = tk.Tk()

        # top bar
        self.w_frm_topbar = ttk.Frame(master=self.window)
        self.w_frm_topbar.pack(fill=tk.X, side=tk.TOP)

        self.w_lbl_title = ttk.Label(master=self.w_frm_topbar, text="CASCADE CALCULATOR")
        self.w_lbl_title.config(font=("Courier", 25))
        self.w_lbl_title.pack()

        self.w_lbl_subtitle = ttk.Label(master=self.w_frm_topbar, text="Leave module rows blank if you did less than 12 modules")
        self.w_lbl_subtitle.config(font=("Arial", 10))
        self.w_lbl_subtitle.pack()


        # result years titles
        self.w_frm_titlebar = ttk.Frame(master=self.window)
        self.w_frm_titlebar.pack(fill=tk.X, side=tk.TOP)

        self.w_lbl_yr2 = ttk.Label(master=self.w_frm_titlebar, text="Year 2")
        self.w_lbl_yr2.config(font=("Arial", 10))
        self.w_lbl_yr2.grid(row=0, column=0)

        self.w_lbl_yr3 = ttk.Label(master=self.w_frm_titlebar, text="Year 3")
        self.w_lbl_yr3.config(font=("Arial", 10))
        self.w_lbl_yr3.grid(row=0, column=1)

        self.w_lbl_yr4 = ttk.Label(master=self.w_frm_titlebar, text="Year 4")
        self.w_lbl_yr4.config(font=("Arial", 10))
        self.w_lbl_yr4.grid(row=0, column=2)

        self.w_frm_titlebar.grid_columnconfigure(0, weight=1)
        self.w_frm_titlebar.grid_columnconfigure(1, weight=1)
        self.w_frm_titlebar.grid_columnconfigure(2, weight=1)

        # yr 2 results
        self.w_frm_year2 = ttk.Frame(master=self.window, width=100)
        self.w_frm_year2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.w_lbl_yr2creds = ttk.Label(master=self.w_frm_year2, text="Credits")
        self.w_lbl_yr2creds.config(font=("Arial", 10))
        self.w_lbl_yr2creds.grid(row=0, column=1)

        self.w_lbl_yr2res = ttk.Label(master=self.w_frm_year2, text="Result")
        self.w_lbl_yr2res.config(font=("Arial", 10))
        self.w_lbl_yr2res.grid(row=0, column=2)

        self.w_ent_yr2arr = []
        for y in range(1, self.NUM_MODULES_PER_YEAR):

            w_ent_entry1 = ttk.Entry(master=self.w_frm_year2, width=4)
            w_ent_entry1.grid(row=y, column=1)

            w_ent_entry2 = ttk.Entry(master=self.w_frm_year2, width=4)
            w_ent_entry2.grid(row=y, column=2)

            self.w_ent_yr2arr.append((w_ent_entry1, w_ent_entry2))

        self.w_frm_year2.grid_columnconfigure(0, weight=1)
        self.w_frm_year2.grid_columnconfigure(3, weight=1)

        # yr 3 results
        self.w_frm_year3 = ttk.Frame(master=self.window, width=100)
        self.w_frm_year3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.w_lbl_yr3creds = ttk.Label(master=self.w_frm_year3, text="Credits")
        self.w_lbl_yr3creds.config(font=("Arial", 10))
        self.w_lbl_yr3creds.grid(row=0, column=1)

        self.w_lbl_yr3res = ttk.Label(master=self.w_frm_year3, text="Result")
        self.w_lbl_yr3res.config(font=("Arial", 10))
        self.w_lbl_yr3res.grid(row=0, column=2)

        self.w_ent_yr3arr = []
        for y in range(1, self.NUM_MODULES_PER_YEAR):
            
            w_ent_entry1 = ttk.Entry(master=self.w_frm_year3, width=4)
            w_ent_entry1.grid(row=y, column=1)

            w_ent_entry2 = ttk.Entry(master=self.w_frm_year3, width=4)
            w_ent_entry2.grid(row=y, column=2)

            self.w_ent_yr3arr.append((w_ent_entry1, w_ent_entry2))

        self.w_frm_year3.grid_columnconfigure(0, weight=1)
        self.w_frm_year3.grid_columnconfigure(3, weight=1)

        # yr 4/masters yr results
        self.w_frm_year4 = ttk.Frame(master=self.window, width=100)
        self.w_frm_year4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.w_lbl_yr4creds = ttk.Label(master=self.w_frm_year4, text="Credits")
        self.w_lbl_yr4creds.config(font=("Arial", 10))
        self.w_lbl_yr4creds.grid(row=0, column=1)

        self.w_lbl_yr4res = ttk.Label(master=self.w_frm_year4, text="Result")
        self.w_lbl_yr4res.config(font=("Arial", 10))
        self.w_lbl_yr4res.grid(row=0, column=2)

        self.w_ent_yr4arr = []
        for y in range(1, self.NUM_MODULES_PER_YEAR):
            
            w_ent_entry1 = ttk.Entry(master=self.w_frm_year4, width=4)
            w_ent_entry1.grid(row=y, column=1)

            w_ent_entry2 = ttk.Entry(master=self.w_frm_year4, width=4)
            w_ent_entry2.grid(row=y, column=2)

            self.w_ent_yr3arr.append((w_ent_entry1, w_ent_entry2))

        self.w_frm_year4.grid_columnconfigure(0, weight=1)
        self.w_frm_year4.grid_columnconfigure(3, weight=1)

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    casc = Cascade()
    casc.start()