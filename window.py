try:
    import tkinter
except ImportError:
    import Tkinter as tkinter  # python 2

import function as f
import batch as Batch

# setup main window
mainWindow = tkinter.Tk()
mainWindow.title("Distillate Manager")
mainWindow.geometry("640x480")

# Setup the frames for the buttons, and display info
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=0, column=0, sticky="news")
result_frame = tkinter.Frame(mainWindow)
result_frame.grid(row=1, column=0, sticky="news")
user_interaction_frame = tkinter.Frame(mainWindow)
user_interaction_frame.grid(row=1, column=0, sticky='news')

# setup and display the button frame
new_batch_btn = tkinter.Button(button_frame, text='New Batch', command=f.create_new_instance)
new_batch_btn.grid(row=0, column=0)
open_batch_btn = tkinter.Button(button_frame, text='Open Batch', command=f.open_batch)
open_batch_btn.grid(row=0, column=1)

edit_batch_btn = tkinter.Button(button_frame, text='Update Batch')
edit_batch_btn.grid(row=1, column=0)
show_batch_data_btn = tkinter.Button(button_frame, text='Show Batch Data')
show_batch_data_btn.grid(row=1, column=1)
run_data_btn = tkinter.Button(button_frame, text='Start Run Data')
run_data_btn.grid(row=1, column=2)
delete_batch_btn = tkinter.Button(button_frame, text='Delete Batch')
delete_batch_btn.grid(row=1, column=3)
