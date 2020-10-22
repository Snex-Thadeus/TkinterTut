from tkinter import *
from tkinter import ttk


COLOR1 = "RED"
COLOR2 = "BLUE"
COLOR3 = "CYAN"


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Check Buttons In Tkinter")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_check()

    def create_check(self):
        self.check1 = ttk.Checkbutton(self, text="Disabled", state="disabled")
        self.check1.grid(column=0, row=0)

        self.check2 = ttk.Checkbutton(self, text="Unchecked")
        self.check2.grid(column=1, row=0)

        self.check3 = ttk.Checkbutton(self, text="Enabled")
        self.check3.grid(column=2, row=0)


window = Window()
window.mainloop()