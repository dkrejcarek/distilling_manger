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
