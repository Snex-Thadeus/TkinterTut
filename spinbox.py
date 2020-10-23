from tkinter import *
import tkinter as tk
from tkinter import scrolledtext


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Create SpinBox In Tkinter")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.spin_box()

    def spin_callback(self):
        value = self.spin.get()
        self.controlText.insert(INSERT, value)

    def spin_box(self):
        self.spin = Spinbox(self, from_=0, to_=15, command=self.spin_callback)
        self.spin.grid(column=0, row=0)

        scroll_w = 30
        scroll_h = 10

        self.controlText = scrolledtext.ScrolledText(self, width=scroll_w, height=scroll_h, wrap=WORD)
        self.controlText.grid(column=1, row=2)


window = Window()
window.mainloop()