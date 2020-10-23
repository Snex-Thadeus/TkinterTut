from tkinter import *
import tkinter as tk
from tkinter import scrolledtext


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("ScrollTextControl In Tkinter")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_scroll()

    def create_scroll(self):
        scroll_w = 30
        scroll_h = 10

        scrollText = scrolledtext.ScrolledText(self, width=scroll_w, height=scroll_h, wrap=tk.WORD)
        scrollText.grid(column=0, columnspan=3)



window = Window()
window.mainloop()