from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import customtkinter
import tkinter.messagebox as tkmb
import mysql.connector
from subprocess import call
from tkinter import filedialog

class Candidate_Register:
    def __init__(self,root):
        self.root =root
        self.root.title("Registration window")
        self.root.geometry('1166x718')
        self.root.resizable(0, 0)
        self.root.state('zoomed')
        
        self.bg=ImageTk.PhotoImage(file="images/bg2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        self.fn=StringVar()
        self.ln=StringVar()
        self.a=StringVar()
        self.gender=StringVar()
        self.wloc=StringVar()
        self.ward=StringVar()
        self.pid=StringVar()
        self.cid=StringVar()
        self.image_file_path = None
        self.image_data=None
        self.flag=0
        # register frame  
        
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=70,width=700,height=500)
        
        
        self.left=ImageTk.PhotoImage(file="images/vector.png")
        left=Label(self.root,image=self.left,bg='#040405').place(x=80,y=70,width=400,height=500)
        

        self.h_name = Label(frame1,text="REGISTER AS CANDIDATE",font=('yu gothic ui', 20, "bold"), bg="white",fg='#FF3399').place(x=200,y=10)
       
        self.f_name = Label(frame1,text="First Name",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=50,y=100)
        self.txt_fname = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.fn)
        self.txt_fname.place(x=50,y=130,width=250)
        
        self.l_name = Label(frame1,text="Last Name",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=370,y=100)
        self.txt_lname = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.ln)
        self.txt_lname.place(x=370,y=130,width=250)
        
        
        
        self.age = Label(frame1,text="Age",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=50,y=170)
        self.txt_age = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.a)
        self.txt_age.place(x=50,y=200,width=250)
       
    
        self.sex = Label(frame1,text="Sex",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=370,y=170)
        self.r1=Radiobutton(frame1,text="Male",variable=self.gender, value="Male",font=('yu gothic ui', 15,),bg="lightgray").place(x=370,y=200)
        self.r2=Radiobutton(frame1,text="Female",variable=self.gender, value="Female",font=('yu gothic ui', 15,),bg="lightgray").place(x=500,y=200)
        self.gender.set('Male')
        
        
        self.word_loc = Label(frame1,text="Ward Location",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=50,y=240)
        self.txt_word_loc = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.wloc)
        self.txt_word_loc.place(x=50,y=270,width=250)
        
        self.ward_no = Label(frame1,text="Ward Number",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=370,y=240)
        self.txt_ward_no = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.ward)
        self.txt_ward_no.place(x=370,y=270,width=250)
        
        
        self.party_id = Label(frame1,text="Party Id",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=50,y=310)
        self.txt_party_id = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.pid)
        self.txt_party_id.place(x=50,y=340,width=250)
        
        self.candidate_id = Label(frame1,text="Candidate Id",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=370,y=310)
        self.txt_candidate_id = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.cid)
        self.txt_candidate_id.place(x=370,y=340,width=250)
        
        self.open_button = Button(frame1,text="Upload Image",cursor="hand2",font=('tahoma',20,"bold"),command=self.open)
        self.open_button.place(x=250,y=380,width=200,height=40)

#         self.btn_img=ImageTk.PhotoImage(file="images/btn1.png")
#         btn=Button(frame1,image=self.btn_img,width=250,bd=0,cursor="hand2",bg='#3047ff', text='LOGIN', font=("yu gothic ui", 13, "bold"),fg='#FF3399').place(x=50,y=420)
        
        b1_1=Button(frame1,text="REGISTER",bg='darkblue',fg="#FF3399",cursor="hand2",font=('tahoma',20,"bold"),command=self.validation)
        b1_1.place(x=180,y=430,width=350,height=40)
       
        back=Button(text='Back',bg='#aef',fg='blue',cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.back)
        back.place(x=50,y=620,width=100,height=50)
    def validation(self):
        if self.fn.get()=='':
            tkmb.showerror('Invalid','Please Enter Your First Name',parent=self.root)
        elif self.ln.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Last Name',parent=self.root)
        elif self.a.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Age',parent=self.root)
        elif self.gender.get()=='':
            tkmb.showerror('Invalid','Please Select Your Gender',parent=self.root)
        elif self.wloc.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Location',parent=self.root)
        elif self.ward.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Ward Number',parent=self.root)
        elif self.pid.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Party Id',parent=self.root)
        elif self.cid.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Candidate Id',parent=self.root)
        if len(self.cid.get())!=0 and len(self.pid.get())!=0 and len(self.fn.get())!=0 and len(self.ln.get())!=0 and len(self.wloc.get())!=0 and len(self.a.get())!=0 and len(self.ward.get())!=0 and len(self.gender.get())!=0:
            try:
                if self.image_file_path:
                    with open(self.image_file_path, "rb") as f:
                        self.image_data = f.read()
                    conn=mysql.connector.connect(host='localhost',password='Sonu@234',user='root',database='voter')
                    cur=conn.cursor()
                    s='INSERT INTO candidate Values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    data=(self.cid.get().upper(),self.fn.get().upper(),self.ln.get().upper(),self.a.get(),self.gender.get(),self.wloc.get(),self.ward.get(),self.pid.get().upper(),self.image_data)
                    cur.execute(s,data)
                    conn.commit()
                    conn.close()
                    tkmb.showinfo(title='Registration' , message="Congratulation!Successfully Signed Up")
                    self.clear()
                else:
                    tkmb.showerror('Invalid','Please Upload Your Image')
            except Exception as e:
                tkmb.showerror('Error',f'Due to:{str(e)}')
    def back(self):
        self.root.destroy()
        call(['python','admin_panel.py'])
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_age.delete(0,END)
        self.txt_ward_no.delete(0,END)
        self.txt_word_loc.delete(0,END)
        self.txt_party_id.delete(0,END)
        self.txt_candidate_id.delete(0,END)
        self.image_file_path = None
        self.open_button.config(text='Upload Image',fg='black')
    def open(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_file_path = file_path
            self.open_button.config(text='Uploaded',fg='green')
            self.flag=1
root =Tk()
obj = Candidate_Register(root)
root.mainloop()