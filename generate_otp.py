from tkinter import *
import os
from twilio.rest import Client
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as tkmb
from subprocess import call

class Generate_OTP:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1166x718')
        self.root.title("OTP GENERATE")
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
        
        
        self.j = Label(text="    OTP Verification", font = "TimesNewRoman 50 bold",bg= "#4682B4", fg="white").place(x= 0, y= 120,width=1300, height=80)
        self.a = Label(text="OTP is valid for 10 minutes.", font = "TimesNewRoman 14",bg= "#4682B4", fg="white").place(x= 0, y= 300,width=1300,height=60)
        self.b = Label(text="Click on button to generate OTP on your Registered Mobile Number", font = "TimesNewRoman 14", bg= '#4682B4', fg="white").place(x=0, y= 360,width=1300,height=60)
        self.GenerateOTP=PhotoImage(file = "images/Generate_OTP.png")
        self.generatebutton = Button(image=self.GenerateOTP, border = 0,cursor='hand2', command=self.open)
        self.generatebutton.place(x = 560 ,y = 450)
    def open(self):
        self.root.destroy()
        import otp
        
root=Tk()
obj=Generate_OTP(root)
root.mainloop()