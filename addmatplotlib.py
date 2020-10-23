from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tkinter Matplotlib Embed")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.create_matcanvas()

    def create_matcanvas(self):
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_support(111)

        a.plot([1,2,3,4,5,6], [8,3,4,1,2,9])

        canvas = FigureCanvasTkAgg(f, self)

        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)



window = Window()
window.mainloop()