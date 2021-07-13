<<<<<<< HEAD
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk  # python 2


class App():
    def __init__(self):
        open_button = tk.Button(text='File Open', command=self.open_events_db)
        print_button = tk.Button(text='Print DB', command=self.print_events_db)

        open_button.pack(fill=tk.X)
        print_button.pack(fill=tk.X)
=======
import tkinter as tk
from batch import Batch

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
        new_batch_label.grid(row=0, column=0, sticky='news')

        date_label = tk.Label(self.ui_frame,
                              text='Date: ')
        date_label.grid(row=1, column=0, sticky='ns')
        date_input = tk.Entry(self.ui_frame)
        date_input.grid(row=1, column=1, sticky='ns')

        style_label = tk.Label(self.ui_frame,
                               text='Type: ')
        style_label.grid(row=2, column=0, sticky='ns')
        style_input = tk.Entry(self.ui_frame)
        style_input.grid(row=2, column=1, sticky='ns')

        original_gravity_label = tk.Label(self.ui_frame,
                                          text="OG: ")
        original_gravity_label.grid(row=3, column=0, sticky='ns')
        original_gravity_input = tk.Entry(self.ui_frame)
        original_gravity_input.grid(row=3, column=1, sticky='ns')

        volume_label = tk.Label(self.ui_frame,
                                text='Vol (L)')
        volume_label.grid(row=4, column=0, sticky='ns')
        volume_input = tk.Entry(self.ui_frame)
        volume_input.grid(row=4, column=1, sticky='ns')

        enter_button = tk.Button(self.ui_frame,
                                 text='Enter',
                                 command=lambda: self.save_data(date_input.get(),
                                                                style_input.get(),
                                                                original_gravity_input.get(),
                                                                volume_input.get()))
        enter_button.grid(row=5, column=0, columnspan=2, sticky='news')

    def save_data(self, date, style, og, vol):
        batch = Batch(style, date, float(og), float(vol))
        batch.save_data()
        print(batch)

        for widget in self.ui_frame.winfo_children():
            widget.destroy()
>>>>>>> 207bcac9fb30438eca5cab2818b1c36ec4723b2a
