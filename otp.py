from tkinter import *
import tkinter as tk
from twilio.rest import Client
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as tkmb
import random
import mysql.connector
from subprocess import call

class OTP:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1166x718')
        self.root.title("otp verification")
        self.root.resizable(0, 0)
        self.root.state('zoomed')
        #background image
        
        
        img = Image.open("images/banner.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        
        img1 = Image.open("images/banner1.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        img2 = Image.open("images/face-off-banner.jpg")
        img2=img2.resize((600,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)
        
        
        img3 = Image.open("images/bg3.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img_lbl=Label(self.root,image=self.photoimg3)
        bg_img_lbl.place(x=0,y=130,width=1300,height=630)
        
        
        title_lbl=Label(bg_img_lbl,text="Welcome To E-Voting System With Face Recognition",font=('yu gothic ui',35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1300,height=60)

        title_lb2=Label(bg_img_lbl,text="VERIFY OTP",font=('yu gothic ui',35,"bold"),bg="yellow",fg="darkblue")
        title_lb2.place(x=500,y=70,width=300,height=60)
        self.otp=StringVar()
        self.e = Entry(font=('Roboto Mono', 50,),bg="white",justify="center")
        self.e.place(x=450,y=280,width=400,height=70,)
        self.e.bind("<Key>", self.on_key_press)
        self.b = Button(text='SUBMIT', font=("yu gothic ui", 15, "bold"), width=15, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command = self.check)
        self.b.place(x=570, y=400)
        
        self.c=Label(text='',font=('times new roman',16),fg='white',bg='white',borderwidth=0, highlightthickness=0)
        self.c.place(x=570,y=500)
        self.rs = Button(text='RESEND OTP', font=("yu gothic ui", 15, "bold"), width=15, bd=0,
                            bg='#D68910', cursor='hand2', activebackground='#3047ff', fg='white',command =self.resend)
        self.rs.place(x=570, y=500)
        self.n=str(self.OTP())
        self.pno=self.getdata()
        self.client=Client("AC8092f0ea99f4fdab5e1f9bde905f1e34","30639b879a6bea54e69c753f400aa1ac")
        self.client.messages.create(to=f"{self.pno}",
                                    from_="+12342565207",
                                    body=self.n)
    def on_key_press(self,event):
        # Get the current text in the entry
        text = self.e.get()
        
        # Check if the event is a digit and add a space after the digit
        if event.char.isdigit():
            text += " "

        # Update the entry with the modified text
        self.e.delete(0, END)
        self.e.insert(0, text) 
    def OTP(self):
        return random.randrange(100000,1000000)
    
    def getdata(self):
        try:
            with open("stored_value.txt","r") as file:
                lines=file.readlines()
                lines_new=[line.replace("\n","") for line in lines]
            self.mb="+91"+lines_new[9]
            return self.mb
        except Exception as e:
            tkmb.showerror('Error','Due to:'+str(e))

    def check(self):
        try:
            self.otp = self.e.get().replace(" ","")
            if self.otp==self.n:
                tkmb.showinfo('Success','Verification Successful')
                self.e.delete(0,END)
                self.n='done'
                self.root.destroy()
                import face_recognition
            else:
                tkmb.showerror('Invalid','Wrong OTP')
        except Exception as e:
            tkmb.showerror('Error','Due to:'+str(e))

    def resend(self):
        self.e.delete(0,END)
        self.c.config(text="OTP Resent",fg='green')
        self.c.place(x=590,y=550)
        self.n=str(self.OTP())
        self.client=Client("AC8092f0ea99f4fdab5e1f9bde905f1e34","30639b879a6bea54e69c753f400aa1ac")
        self.client.messages.create(to=f"{self.pno}",
                                    from_="+12342565207",
                                    body=self.n)

root=Tk()
obj=OTP(root)
root.mainloop()