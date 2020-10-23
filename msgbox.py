from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Message Box In Tkinter")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_button()

    def create_button(self):
        self.btn = ttk.Button(self, text="Open Message Box", command=self.error_msg)
        self.btn.grid(column=1, row=1)

    def info_msg(self):
        msg.showinfo("Python Info Message Box", "This GUI is build in Tkinter")

    def warn_msg(self):
        msg.showwarning("Warning Message", "This is a warning!")

    def error_msg(self):
        msg.showerror("This is an Error", "This is an error message")





window = Window()
window.mainloop()