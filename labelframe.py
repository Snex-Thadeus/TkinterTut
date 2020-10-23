from tkinter import *
import tkinter as tk
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Labelframe In Tkinter")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.labelFrame = ttk.LabelFrame(self, text="Tkinter Label")
        self.labelFrame.grid(column=0, row=7, padx=20, pady=40)

        self.create_labels()

    def create_labels(self):
        ttk.Label(self.labelFrame, text="Label One").grid(column=0, row=0)
        ttk.Label(self.labelFrame, text="Label Two").grid(column=0, row=1)
        ttk.Label(self.labelFrame, text="Label Three").grid(column=0, row=2)




window = Window()
window.mainloop()