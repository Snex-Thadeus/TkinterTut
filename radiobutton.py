from tkinter import *
from tkinter import ttk


COLOR1 = "RED"
COLOR2 = "BLUE"
COLOR3 = "CYAN"


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tkinter OOP Window & Label")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_radio()

    def rad_event(self):
        radSelected = self.radValues.get()

        if radSelected == 1:
            self.configure(background=COLOR1)
        elif radSelected == 2:
            self.configure(background=COLOR2)
        elif radSelected == 3:
            self.configure(background=COLOR3)

    def create_radio(self):
        self.radValues = IntVar()
        self.rad1 = ttk.Radiobutton(self, text=COLOR1, value=1, variable=self.radValues, command=self.rad_event)
        self.rad1.grid(column=0, row=0, sticky=W, columnspan=3)

        self.rad2 = ttk.Radiobutton(self, text=COLOR2, value=2, variable=self.radValues, command=self.rad_event)
        self.rad2.grid(column=0, row=1, sticky=W, columnspan=3)

        self.rad3 = ttk.Radiobutton(self, text=COLOR3, value=3, variable=self.radValues, command=self.rad_event)
        self.rad3.grid(column=0, row=2, sticky=W, columnspan=3)




window = Window()
window.mainloop()