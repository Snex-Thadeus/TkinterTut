from tkinter import *
from tkinter import colorchooser
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tkinter OOP Window & Label")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_button()

    def create_button(self):
        btn = ttk.Button(self, text="Open Color Chooser", command=self.color_chooser)
        btn.grid(column=0, row=0)

    def color_chooser(self):
        (rgbx, hx) = colorchooser.askcolor()



window = Window()
window.mainloop()