from tkinter import *
import tkinter as tk
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tab Widget In Tkinter")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        tab_control = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tab_control)
        tab_control.add(self.tab1, text="Example One")

        self.tab2 = ttk.Frame(tab_control)
        tab_control.add(self.tab2, text="Example Two")

        tab_control.pack(expand=1, fill="both")

        self.add_widgets()

    def add_widgets(self):
        label_frame = LabelFrame(self.tab1, text="Example One Tab")
        label_frame.grid(column=0, row=0, padx=8, pady=4)

        label = Label(label_frame, text="Enter Your Name:")
        label.grid(column=0, row=0)

        text_edit = Entry(label_frame, width=25)
        text_edit.grid(column=1, row=0)

        label2 = Label(label_frame, text="Enter Your Password:")
        label2.grid(column=0, row=1)

        text_edit2 = Entry(label_frame, width=25)
        text_edit2.grid(column=1, row=1)

        # tab 2
        label_frame2 = LabelFrame(self.tab2, text="Example Two Tab")
        label_frame2.grid(column=0, row=0, padx=8, pady=4)

        label = Label(label_frame2, text="Enter Your Name:")
        label.grid(column=0, row=0)

        text_edit = Entry(label_frame2, width=25)
        text_edit.grid(column=1, row=0)

        label2 = Label(label_frame2, text="Enter Your Password:")
        label2.grid(column=0, row=1)

        text_edit2 = Entry(label_frame2, width=25)
        text_edit2.grid(column=1, row=1)


window = Window()
window.mainloop()