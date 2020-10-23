from tkinter import *


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tkinter OOP Window & Label")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_listbox()

    def create_listbox(self):
        listbox = Listbox(self)
        listbox.insert(1, "Python")
        listbox.insert(2, "C++")
        listbox.insert(3, "Java")
        listbox.insert(4, "C#")
        listbox.insert(5, "Ruby")

        listbox.pack()


window = Window()
window.mainloop()