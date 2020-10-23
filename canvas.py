from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Canvas In Tkinter")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_canvas()

    def create_canvas(self):
        canvas = Canvas(self, bg="blue", height=250, width=300)
        coord = 10, 50, 240, 210

        canvas.pack(expand=YES, fill=BOTH)

        img = Image.open("s.jpg")
        canvas.image = ImageTk.PhotoImage(img)
        canvas.create_image(0,0, image = canvas.image, anchor='nw')
        #
        # arc = canvas.create_arc(coord, start=0, extent=150, fill="red")
        # canvas.pack()


window = Window()
window.mainloop()