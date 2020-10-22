from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tkinter Text Entry")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_combo()

    def click_me(self):
        self.label.configure(text="Selected :" + self.languages.get())

    def create_combo(self):
        self.languages = StringVar()

        self.combobox = ttk.Combobox(self, width=20, textvariable=self.languages)
        self.combobox['values'] = ("Python", "Java", "C++", "C#", "Ruby")
        self.combobox.grid(column=1, row=0)

        self.label = ttk.Label(self, text="Select Your Language")
        self.label.grid(column=0, row=0)

        self.button = ttk.Button(self, text="Click Me", command=self.click_me)
        self.button.grid(column=2, row=0)


window = Window()
window.mainloop()