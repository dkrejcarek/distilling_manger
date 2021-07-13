import tkinter as tk
from functools import partial

HEIGHT = 500
WIDTH = 600


class App:

    def __init__(self, master):
        self.master = master
        self.master.title("Distilling manager")
        self.master.config(bg='white')
        self.master.geometry(str(HEIGHT) + 'x' + str(WIDTH))

        self.title_frame = tk.Frame(self.master)
        self.title_frame.grid(row=0, column=0, sticky='news')
        self.button_frame = tk.Frame(self.master)
        self.button_frame.grid(row=1, column=0, sticky='news')
        self.ui_frame = tk.Frame(self.master)
        self.ui_frame.grid(row=2, column=0, sticky='news')
        self.title_label = tk.Label(self.title_frame,
                                    text='Distilling Batch Manager')
        self.title_label.grid(row=0, column=0)

        self.new_batch_btn = tk.Button(self.button_frame, text='New Batch',
                                       command=self.new_batch)
        self.new_batch_btn.grid(row=0, column=0)

        self.close_button = tk.Button(self.button_frame,
                                      text="Close",
                                      command=master.quit)
        self.close_button.grid(row=2, column=0)

    def new_batch(self):
        new_batch_label = tk.Label(self.ui_frame,
                                   text='Please enter New Batch info')
        new_batch_label.grid(row=0, column=0)

        date_label = tk.Label(self.ui_frame,
                              text='Date: ')
        date_label.grid(row=1, column=0)
        date_input = tk.Entry(self.ui_frame)
        date_input.grid(row=1, column=1)

        type_label = tk.Label(self.ui_frame,
                              text='Type: ')
        type_label.grid(row=1, column=2)
        type_input = tk.Entry(self.ui_frame)
        type_input.grid(row=1, column=3)

        original_gravity_label = tk.Label(self.ui_frame,
                                          text="OG: ")
        original_gravity_label.grid(row=1, column=4)
        original_gravity_input = tk.Entry(self.ui_frame,
                                          insert='1.xxx')
        original_gravity_input.grid(row=1, column=5)

        enter_button = tk.Button(self.ui_frame,
                                 text='Enter',
                                 command=lambda: self.save_data(date_input.get(),
                                                                type_input.get(),
                                                                original_gravity_input.get()))
        enter_button.grid(row=2, column=0)

    def save_data(self, date, batch_type, original_gravity):
        print('Data Saved')
        print(date, batch_type, original_gravity)

        for widget in self.ui_frame.winfo_children():
            widget.destroy()
