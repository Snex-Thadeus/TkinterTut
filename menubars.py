from tkinter import *
import tkinter as tk
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tkinter Menu")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.labelFrame = ttk.LabelFrame(self, text="Tkinter Label")
        self.labelFrame.grid(column=0, row=7, padx=20, pady=40)

        self.create_menu()

    def window_close(self):
        self.quit()
        self.destroy()
        exit()

    def create_menu(self):
        menuBar = Menu(self)
        self.config(menu=menuBar)

        file_menu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Exit", command=self.window_close)
        file_menu.add_separator()
        file_menu.add_command(label="Open")

        help_menu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About")



window = Window()
window.mainloop()