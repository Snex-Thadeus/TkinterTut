from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tkinter Text Entry")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.text_entry()

    def click_me(self):
        self.label.configure(text="Hello" + self.name.get())

    def text_entry(self):
        self.name = StringVar()

        self.label = ttk.Label(self, text="Enter Your Name:")
        self.label.grid(column=0, row=0)

        self.textbox = ttk.Entry(self, width=20, textvariable=self.name)
        self.textbox.focus()
        self.textbox.grid(column=0, row=1)

        self.button = ttk.Button(self, text="Click Me", command=self.click_me)
        self.button.grid(column=0, row=2)

        self.button.configure(state="disabled")


window = Window()
window.mainloop()