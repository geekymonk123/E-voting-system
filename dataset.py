import cv2
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import customtkinter
import tkinter.messagebox as tkmb
import mysql.connector
from tkinter import filedialog

class Information:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("evoting system")

        self.pid=StringVar()
        self.pname=StringVar()
        self.image_file_path = None
        self.image_data=None

        self.dob = Label(text="Pid",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=500,y=70)
        self.txt_dob = Entry(font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.pid)
        self.txt_dob.place(x=500,y=100,width=250)
        
        self.dob = Label(text="Pname",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=500,y=170)
        self.txt_dob = Entry(font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.pname)
        self.txt_dob.place(x=500,y=200,width=250)

        self.open_button = Button(text="Upload Image",cursor="hand2",font=('tahoma',20,"bold"),command=self.open)
        self.open_button.place(x=500,y=380,width=200,height=40)

        self.b=Button(text='Submit',command=self.data)
        self.b.place(x=500,y=500)
    def data(self):
        try:
            if self.image_file_path:
                    with open(self.image_file_path, "rb") as f:
                        self.image_data = f.read()
                    conn=mysql.connector.connect(host='localhost',password='Sujoy@2212',user='root',database='voter')
                    cur=conn.cursor()
                    s='INSERT INTO party Values(%s,%s,%s)'
                    data=(self.pid.get().upper(),self.pname.get().upper(),self.image_data)
                    cur.execute(s,data)
                    conn.commit()
                    conn.close()
                    tkmb.showinfo(title='Registration' , message="Done")
        except Exception as e:
             tkmb.showerror('Error',f'Due to:{str(e)}')
    def open(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_file_path = file_path
root=Tk()
obj=Information(root)
root.mainloop()