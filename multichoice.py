from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Multi choice Box In Tkinter")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_button()

    def create_button(self):
        self.btn = ttk.Button(self, text="Open Choice Box", command=self.choice_box)
        self.btn.grid(column=1, row=1)

    def choice_box(self):
        answer = msg.askyesnocancel("Multi Choice Box", "Do You Want To Exit?")

        if answer == True:
            self.quit()


window = Window()
window.mainloop()