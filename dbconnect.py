from tkinter import *
from tkinter import ttk
import psycopg2
from tkinter import messagebox as msg


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("PostgreSQL Database Connection")
        self.minsize(500, 400)
        self.wm_iconbitmap('D:\Store Management Software\Source Code\icon.ico')

        self.label_frame = ttk.LabelFrame(self, text="Database Connection")
        self.label_frame.grid(column=0, row=0, padx=20, pady=20)

        self.create_widget()

    def create_widget(self):
        label = Label(self.label_frame, text="Enter Your Name:")
        label.grid(column=0, row=0)

        self.text_edit = Entry(self.label_frame, width=25)
        self.text_edit.grid(column=1, row=0)

        label2 = Label(self.label_frame, text="Enter Your Password:")
        label2.grid(column=0, row=1)

        self.text_edit2 = Entry(self.label_frame, width=25)
        self.text_edit2.grid(column=1, row=1)

        button = ttk.Button(self.label_frame, text="Insert Data", command=self.db_connect)
        button.grid(column=1, row=2)

    def db_connect(self):
        con = psycopg2.connect('localhost', 'postgres', '', 'gui')
        cur = con.cursor()
        cur.execute("INSERT INTO data(name, password)"
                    "VALUES('%s', '%s')" % (''.join(self.text_edit.get()),
                                            ''.join(self.text_edit2.get())))

        msg.showinfo("Inserting Data", "Data Inserted Successfully")

window = Window()
window.mainloop()