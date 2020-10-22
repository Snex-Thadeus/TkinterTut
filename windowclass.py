from tkinter import *


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tkinter OOP Window & Label")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.createLabel()

    def createLabel(self):
        labelFont = ('times', 40, 'bold')
        label = Label(self, text="Tkinter Label creation")
        label.config(font=labelFont, bg='black', fg='yellow')
        label.grid(column=0, row=0)



window = Window()
window.mainloop()