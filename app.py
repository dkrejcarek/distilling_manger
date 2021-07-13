import tkinter as tk
from batch import Batch
import db as db

HEIGHT = 500
WIDTH = 600


class App:
    current_batch = ''
    DATABASE = 'batches.db'

    def __init__(self, master):
        self.master = master
        self.master.title("Distilling manager")
        self.master.config(bg='white')
        self.master.geometry(str(HEIGHT) + 'x' + str(WIDTH))

        self.title_frame = tk.Frame(self.master, bg='white')
        self.title_frame.grid(row=0, column=0, sticky='news')
        self.button_frame = tk.Frame(self.master, bg='white')
        self.button_frame.grid(row=1, column=0, sticky='news')
        self.ui_frame = tk.Frame(self.master, bg='white')
        self.ui_frame.grid(row=2, column=0, sticky='news')
        self.title_label = tk.Label(self.title_frame,
                                    text='Distilling Batch Manager',
                                    bg='white',
                                    font=15)
        self.title_label.grid(row=0, column=0, pady=10)

        self.new_batch_btn = tk.Button(self.button_frame, text='New Batch',
                                       command=self.new_batch)
        self.new_batch_btn.grid(row=0, column=0, padx=5, pady=5)
        self.open_btn = tk.Button(self.button_frame, text='Open Batch',
                                  command=self.open_batch)
        self.open_btn.grid(row=0, column=1, padx=5, pady=5)

        self.close_button = tk.Button(self.button_frame,
                                      text="Exit",
                                      command=master.quit)
        self.close_button.grid(row=2, column=0)

    def new_batch(self):
        new_batch_label = tk.Label(self.ui_frame,
                                   text='Please enter New Batch info',
                                   bg='white')
        new_batch_label.grid(row=0, column=0, sticky='news')

        date_label = tk.Label(self.ui_frame,
                              text='Date: ',
                              bg='white')
        date_label.grid(row=1, column=0, sticky='ns')
        date_input = tk.Entry(self.ui_frame)
        date_input.grid(row=1, column=1, sticky='ns')

        style_label = tk.Label(self.ui_frame,
                               text='Type: ',
                               bg='white')
        style_label.grid(row=2, column=0, sticky='ns')
        style_input = tk.Entry(self.ui_frame)
        style_input.grid(row=2, column=1, sticky='ns')

        original_gravity_label = tk.Label(self.ui_frame,
                                          text="OG: ",
                                          bg='white')
        original_gravity_label.grid(row=3, column=0, sticky='ns')
        original_gravity_input = tk.Entry(self.ui_frame)
        original_gravity_input.grid(row=3, column=1, sticky='ns')

        volume_label = tk.Label(self.ui_frame,
                                text='Vol (L)', bg='white')
        volume_label.grid(row=4, column=0, sticky='ns')
        volume_input = tk.Entry(self.ui_frame)
        volume_input.grid(row=4, column=1, sticky='ns')

        enter_button = tk.Button(self.ui_frame,
                                 text='Enter',
                                 command=lambda: self.save_data(date_input.get(),
                                                                style_input.get(),
                                                                original_gravity_input.get(),
                                                                volume_input.get()),
                                 padx=30, pady=5)
        enter_button.grid(row=5, column=0, columnspan=2,
                          padx=10, pady=10)

    def save_data(self, date, style, og, vol):
        batch = Batch(style, date, float(og), float(vol))
        batch.save_data(self.DATABASE)
        print(batch)

        for widget in self.ui_frame.winfo_children():
            widget.destroy()

    def open_batch(self):
        #  Get Batches from DB
        list_var = tk.StringVar(value=db.load_batches(self.DATABASE))

        # Setup the view Window
        open_label = tk.Label(self.ui_frame,
                              text='Please select Batch to open',
                              bg='white')
        open_label.grid(row=0, column=0, sticky='news')

        batch_listbox = tk.Listbox(self.ui_frame,
                                   listvariable=list_var,
                                   height=6)
        batch_listbox.grid(row=1, column=0)
        select_btn = tk.Button(self.ui_frame,
                               text="Open",
                               command=lambda: self.show_selected(batch_listbox.get(batch_listbox.curselection())))
        select_btn.grid(row=2,
                        column=0)

    def show_selected(self, selection):
        for widget in self.ui_frame.winfo_children():
            widget.destroy()
        batch = db.get_batch(self.DATABASE, selection)
        open_label = tk.Label(self.ui_frame, text=batch)
        open_label.grid(row=0, column=0)
        update_btn = tk.Button(self.ui_frame,
                               text='Update')
        update_btn.grid(row=1, column=0)



