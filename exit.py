from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from subprocess import call


class Exit:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1166x718')
        self.root.title("exit")
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
        
        
        
        #background image
        
        
        img3 = Image.open("images/bg2.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img_lbl=Label(self.root,image=self.photoimg3)
        bg_img_lbl.place(x=0,y=100,width=1300,height=600)
        
        
        title_lbl=Label(bg_img_lbl,text="Thanks For Voting..........",font=('yu gothic ui',35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1300,height=62)
        
        #insert candidate button
        
        img4= Image.open("images/exi.jpg")
        img4=img4.resize((180,180),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img_lbl,image=self.photoimg4,bg='white',cursor="hand2",command=self.exit)
        b1.place(x=550,y=180,width=180,height=180)
        
        b1_1=Button(bg_img_lbl,text="EXIT",bg='white',fg="darkblue",cursor="hand2",font=('tahoma',20,"bold"),command=self.exit)
        b1_1.place(x=550,y=360,width=180,height=45)
    def exit(self):
        self.root.destroy()
        
root=Tk()
obj=Exit(root)
root.mainloop()