import tkinter as tk
from batch import Batch
import db as db

HEIGHT = 500
WIDTH = 1000


class App:
    current_batch = ''
    DATABASE = 'batches'
    FONT_TITLE_1 = 24
    FONT_TITLE_2 = 16

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
                                    font=self.FONT_TITLE_1)
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
        self.close_button.grid(row=0, column=2)

    def new_batch(self):
        self.close_frame(self.ui_frame)
        new_batch_label = tk.Label(self.ui_frame,
                                   text='Please enter New Batch info',
                                   bg='white',
                                   font=self.FONT_TITLE_2)
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

        # final_gravity_label = tk.Label(self.ui_frame,
        #                                text="FG: ",
        #                                bg='white')
        # final_gravity_label.grid(row=4, column=0, sticky='ns')
        # final_gravity_input = tk.Entry(self.ui_frame)
        # final_gravity_input.grid(row=4, column=1, sticky='ns')

        volume_label = tk.Label(self.ui_frame,
                                text='Vol (L)', bg='white')
        volume_label.grid(row=5, column=0, sticky='ns')
        volume_input = tk.Entry(self.ui_frame)
        volume_input.grid(row=5, column=1, sticky='ns')

        enter_button = tk.Button(self.ui_frame,
                                 text='Enter',
                                 command=lambda: self.save_data(date_input.get(),
                                                                style_input.get(),
                                                                original_gravity_input.get(),
                                                                volume_input.get()),
                                 padx=30, pady=5)
        enter_button.grid(row=6, column=0, columnspan=2,
                          padx=10, pady=10)
        close_btn = tk.Button(self.ui_frame,
                              text="Close",
                              command=lambda: self.close_frame(self.ui_frame))
        close_btn.grid(row=6, column=1)

    def save_data(self, date, style, og, vol):
        batch = Batch(style, date, float(og), float(vol))
        batch.save_data(self.DATABASE)
        print(batch)

        self.close_frame(self.ui_frame)

    def open_batch(self):
        self.close_frame(self.ui_frame)
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

    def show_selected(self, selection: str):
        self.close_frame(self.ui_frame)

        batch = db.get_batch(self.DATABASE, selection)
        open_label = tk.Label(self.ui_frame, text=batch)
        open_label.grid(row=0, column=0, columnspan=3)
        update_btn = tk.Button(self.ui_frame,
                               text='Update',
                               command=lambda: self.get_batch_update(batch))
        update_btn.grid(row=1, column=0)
        start_run_btn = tk.Button(self.ui_frame,
                                  text='Start Run',
                                  command=lambda: self.start_run(batch))
        start_run_btn.grid(row=1, column=1)
        close_btn = tk.Button(self.ui_frame,
                              text="Close",
                              command=lambda: self.close_frame(self.ui_frame))
        close_btn.grid(row=1, column=2)

    def get_batch_update(self, batch):
        self.close_frame(self.ui_frame)
        update_label = tk.Label(self.ui_frame,
                                text='Update Batch Info',
                                bg='white',
                                padx=10,
                                pady=10,
                                font=self.FONT_TITLE_2)
        update_label.grid(row=0, column=0, sticky='news')

        date_label = tk.Label(self.ui_frame,
                              text='Date: ',
                              bg='white')
        date_label.grid(row=1, column=0, sticky='ns')
        date_input = tk.Entry(self.ui_frame)
        date_input.grid(row=1, column=1, sticky='ns')
        date_input.insert(0, batch.date)

        style_label = tk.Label(self.ui_frame,
                               text='Type: ',
                               bg='white')
        style_label.grid(row=2, column=0, sticky='ns')
        style_input = tk.Entry(self.ui_frame)
        style_input.grid(row=2, column=1, sticky='ns')
        style_input.insert(0, batch.style)

        original_gravity_label = tk.Label(self.ui_frame,
                                          text="OG: ",
                                          bg='white')
        original_gravity_label.grid(row=3, column=0, sticky='ns')
        original_gravity_input = tk.Entry(self.ui_frame)
        original_gravity_input.grid(row=3, column=1, sticky='ns')
        original_gravity_input.insert(0, batch.original_gravity)

        final_gravity_label = tk.Label(self.ui_frame,
                                       text="FG: ",
                                       bg='white')
        final_gravity_label.grid(row=4, column=0, sticky='ns')
        final_gravity_input = tk.Entry(self.ui_frame)
        final_gravity_input.grid(row=4, column=1, sticky='ns')
        final_gravity_input.insert(0, batch.final_gravity)

        volume_label = tk.Label(self.ui_frame,
                                text='Vol (L)', bg='white')
        volume_label.grid(row=5, column=0, sticky='ns')
        volume_input = tk.Entry(self.ui_frame)
        volume_input.grid(row=5, column=1, sticky='ns')
        volume_input.insert(0, batch.volume)

        enter_button = tk.Button(self.ui_frame,
                                 text='Enter',
                                 command=lambda: self.update_batch(batch,
                                                                   date_input.get(),
                                                                   style_input.get(),
                                                                   original_gravity_input.get(),
                                                                   final_gravity_input.get(),
                                                                   volume_input.get()),
                                 padx=30, pady=5)
        enter_button.grid(row=6, column=0,
                          padx=10, pady=10)
        close_btn = tk.Button(self.ui_frame,
                              text="Close",
                              command=lambda: self.close_frame(self.ui_frame))
        close_btn.grid(row=6, column=1)

    def close_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def update_batch(self, batch, date, style,
                     original_gravity, final_gravity, volume):
        self.close_frame(self.ui_frame)

        label = tk.Label(self.ui_frame, text=batch)
        label.grid(row=0, column=0)

        changes = {
            'date': date,
            'style': style,
            'og': float(original_gravity),
            'fg': float(final_gravity),
            'volume': float(volume)
            }
        label_2 = tk.Label(self.ui_frame, text=changes)
        label_2.grid(row=1, column=0)
        batch.update_info(self.DATABASE, changes)

        self.show_selected(batch.name)

    def start_run(self, batch):
        self.close_frame(self.ui_frame)

        head_frame = tk.Frame(self.ui_frame, bg='white')
        head_frame.grid(row=0, column=0, sticky='news')
        run_info_frame = tk.Frame(self.ui_frame, bg='white')
        run_info_frame.grid(row=1, column=0, sticky='news')

        entry_frame = tk.Frame(self.ui_frame, bg='white')
        entry_frame.grid(row=2, column=0, sticky='news')
        # Configure columns to take of fill width of parent
        for i in range(6):
            run_info_frame.columnconfigure(i, weight=1)
            entry_frame.columnconfigure(i, weight=1)

        run_label = tk.Label(head_frame,
                             text='Add Run Data',
                             bg='white',
                             font=("Arial", self.FONT_TITLE_2))
        run_label.grid(row=0, column=0)
        headers = ("Collected Vol (ml)", "Tralles", "Head Temp",
                   "Total Collected (ml)", "Alcohol (ml)",
                   "Alcohol Remaining (L)",)

        for m in range(len(headers)):
            tk.Label(run_info_frame, text=headers[m], bg='white', width=15).grid(row=0, column=m, sticky='ew')

        # display all the previous runs
        for l in range(len(batch.run)):
            for j in range(3):
                tk.Label(run_info_frame,
                         text=batch.run[l][j],
                         bg='white').grid(row=l + 1, column=j)
            collected = batch.calc_cum_totals(l)
            for k in range(3):
                tk.Label(run_info_frame,
                         text=collected[k],
                         bg='white').grid(row=l + 1, column=k + 3)

        col_vol_input = tk.Entry(entry_frame, width=15)
        col_vol_input.grid(row=0, column=0, sticky='ew')
        tralles_input = tk.Entry(entry_frame, width=15)
        tralles_input.grid(row=0, column=1, sticky='ew')
        head_temp_input = tk.Entry(entry_frame, width=15)
        head_temp_input.grid(row=0, column=2, sticky='ew')
        for n in range(3, 6):
            tk.Label(entry_frame, width=15, bg='white').grid(row=0, column=n, sticky='ew')

        add_info_btn = tk.Button(entry_frame,
                                 text='Add',
                                 command=lambda: self.add_batch(batch,
                                                                col_vol_input.get(),
                                                                tralles_input.get(),
                                                                head_temp_input.get()))
        add_info_btn.grid(row=1, column=0)
        done_btn = tk.Button(entry_frame,
                             text="Stop Run",
                             command=lambda: self.close_frame(self.ui_frame))
        done_btn.grid(row=1, column=1)

    def add_batch(self, batch, volume, tralles, temp):
        batch.run.append((float(volume), float(tralles), float(temp)))
        batch.save_data(self.DATABASE)
        self.start_run(batch)
