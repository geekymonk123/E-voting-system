from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import voterid
import tkinter.messagebox as tkmb
from subprocess import call

class Voter_Details:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1166x718')
        self.root.title("voter details")
        self.root.resizable(0, 0)
        self.root.state('zoomed')


        self.res=self.details()
       #label background image
        
        #image 1
        img = Image.open("images/banner.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #image 2
        img1 = Image.open("images/banner1.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #image 3
        img2 = Image.open("images/face-off-banner.jpg")
        img2=img2.resize((600,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)

        #background image
                
        img3 = Image.open("images/bg3.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img_lbl=Label(self.root,image=self.photoimg3)
        bg_img_lbl.place(x=0,y=130,width=1300,height=600)
        
        
        title_lbl=Label(bg_img_lbl,text="Voter Details",font=('yu gothic ui',35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        
        #frame

        main_frame=Frame(bg_img_lbl,bd=2)
        main_frame.place(x=100, y=50, width=1000, height=415)

        #image frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=FLAT)
        Left_frame.place(x=15, y=10, width=400, height=415)

        img_left = Image.open("images/hyy.png")
        img_left=img_left.resize((300,200),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=80,y=0,width=250,height=400)




        #Right frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=SUNKEN,text="Details",font=("times new roman",20,"bold"),fg="darkblue")
        Right_frame.place(x=380, y=10, width=620, height=415)

        voterId_label=Label(Right_frame,text="Voter Id:",font=("times new roman",16,"bold"))
        voterId_label.place(x=10,y=5)
        voterid_entry=ttk.Label(Right_frame,relief=SUNKEN,text=f'{self.res[1]}',width=50,font=("times new roman",13,"bold"),foreground="blue")
        voterid_entry.place(x=125,y=5,height=30)

        aadharId_label=Label(Right_frame,text="Aadhaar Id:",font=("times new roman",16,"bold"))
        aadharId_label.place(x=10,y=50)
        aadharId_entry=ttk.Label(Right_frame,width=50,relief=SUNKEN,text=f'{self.res[2]}',font=("times new roman",13,"bold"),foreground="blue")
        aadharId_entry.place(x=125,y=50,height=30)

        firstname_label=Label(Right_frame,text="First Name:",font=("times new roman",16,"bold"))
        firstname_label.place(x=10,y=100)
        firstname_entry=ttk.Label(Right_frame,width=50,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.res[3]}',foreground="blue")
        firstname_entry.place(x=125,y=100,height=30)

        lastname_label=Label(Right_frame,text="Last Name:",font=("times new roman",16,"bold"))
        lastname_label.place(x=10,y=150)
        lastname_entry=ttk.Label(Right_frame,width=50,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.res[4]}',foreground="blue")
        lastname_entry.place(x=125,y=150,height=30)

        date_of_birth_label=Label(Right_frame,text="Date of Birth:",font=("times new roman",16,"bold"))
        date_of_birth_label.place(x=10,y=200)
        date_of_birth_entry=ttk.Label(Right_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.res[5]}',foreground="blue")
        date_of_birth_entry.place(x=150,y=200,height=30)

        sex_label=Label(Right_frame,text="Sex:",font=("times new roman",16,"bold"))
        sex_label.place(x=350,y=200)
        sex_entry=ttk.Label(Right_frame,width=14,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.res[6]}',foreground="blue")
        sex_entry.place(x=420,y=200,height=30)

        address_label=Label(Right_frame,text="Address:",font=("times new roman",16,"bold"))
        address_label.place(x=10,y=250)
        address_entry=ttk.Label(Right_frame,width=50,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.res[7]}',foreground="blue")
        address_entry.place(x=125,y=250,height=30)

        ward_no_label=Label(Right_frame,text="Ward No:",font=("times new roman",16,"bold"))
        ward_no_label.place(x=10,y=300)
        ward_no_entry=ttk.Label(Right_frame,width=10,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.res[8]}',foreground="blue")
        ward_no_entry.place(x=125,y=300,height=30)

       
        mobile_no_label=Label(Right_frame,text="Mobile No:",font=("times new roman",16,"bold"))
        mobile_no_label.place(x=245,y=300)
        mobile_no_entry=ttk.Label(Right_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'+91{self.res[9]}',foreground="blue")
        mobile_no_entry.place(x=355,y=300,height=30)
        back=Button(text='Back',bg='#aef',fg='blue',cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.back)
        back.place(x=101,y=598,width=100,height=50)
    def details(self):
        try:
            with open("stored_value.txt","r") as file:
                lines=file.readlines()
                lines_new=[line.replace("\n","") for line in lines]
            return lines_new
        except Exception as e:
            tkmb.showerror('Error','Due to:'+str(e))
    def back(self):
        self.root.destroy()
        call(['python','voter_page.py'])

root=Tk()
obj=Voter_Details(root)
root.mainloop()
