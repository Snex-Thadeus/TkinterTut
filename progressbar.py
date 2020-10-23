from tkinter import *
import tkinter as tk
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("ProgressBar In Tkinter")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.label_trame = ttk.LabelFrame(self, text="ProgressBar Example")
        self.label_trame.grid(column=0, row=0)

        self.create_progressbar()

    def create_progressbar(self):
        self.button1 = ttk.Button(self.label_trame, text="Start ProgressBar", command=self.start_progressbar)
        self.button1.grid(column=0, row=0)

        self.button2 = ttk.Button(self.label_trame, text="Stop ProgressBar", command=self.stop_progressbar)
        self.button2.grid(column=0, row=2)

        self.progress_bar = ttk.Progressbar(self, orient='horizontal', length=280, mode='determinate')
        self.progress_bar.grid(column=0, row=3)

    def start_progressbar(self):
        self.progress_bar.start()

    def stop_progressbar(self):
        self.progress_bar.stop()




window = Window()
window.mainloop()