from tkinter import *


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tkinter Layout Management")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_Place()

    def create_Pack(self):
        Label(self, text="Pack Layout Example").pack()
        Button(self, text="Button").pack()
        Button(self, text="Button").pack(expand=1)
        Button(self, text="Button").pack(fill=X, expand=1)

        Button(self, text="LEFT").pack(side=LEFT)
        # Button(self, text="CENTER").pack(side=CENTER)
        # Button(self, text="RIGHT").pack(side=RIGHT)

    def create_Grid(self):
        Label(self, text="GridLayout Example").grid(column=0, row=0)
        Button(self, text="Button").grid(column=1, row=1)

    def create_Place(self):
        Button(self, text="Absolute Positioning").place(x=20, y=20)
        Button(self, text="Relative Positioning").place(relx=0.6, rely=0.9, relwidth=10, anchor=NE)




window = Window()
window.mainloop()