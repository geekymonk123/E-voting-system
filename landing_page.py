from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from subprocess import call

class Landing_Page:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1166x718')
        self.root.title("evoting system")
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
        
        
        img3 = Image.open("images/l1.png")
        img3=img3.resize((1200,630),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img_lbl=Label(self.root,image=self.photoimg3)
        bg_img_lbl.place(x=0,y=100,width=1300,height=630)
        
        
        title_lbl=Label(bg_img_lbl,text="Welcome To E-Voting System With Face Recognition",font=('yu gothic ui',35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1300,height=60)
        
        #insert candidate button
        
        img4= Image.open("images/dev.jpg")
        img4=img4.resize((300,250),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img_lbl,image=self.photoimg4,bg='white',cursor="hand2",command=self.admin)
        b1.place(x=20,y=200,width=300,height=250)
        
        b1_1=Button(bg_img_lbl,text="Login As Admin",bg='gray',fg="darkblue",cursor="hand2",font=('tahoma',15,"bold"),command=self.admin)
        b1_1.place(x=20,y=420,width=300,height=60)
        
        
        img5= Image.open("images/human.jpg")
        img5=img5.resize((300,250),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img_lbl,image=self.photoimg5,bg='white',cursor="hand2",command=self.voter)
        b1.place(x=950,y=200,width=300,height=250)
        
        b1_1=Button(bg_img_lbl,text="Login As Voter",bg='gray',fg="darkblue",cursor="hand2",font=('tahoma',15,"bold"),command=self.voter)
        b1_1.place(x=950,y=420,width=300,height=60)

        exit=Button(text='Exit',bg='#aef',fg='blue',cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.exit)
        exit.place(x=50,y=620,width=100,height=50)
    
    def exit(self):
        self.root.destroy()
    def admin(self):
        self.root.destroy()
        call(['python','admin_login.py'])
    def voter(self):
        self.root.destroy()
        call(['python','voter_login_final.py'])

root=Tk()
obj=Landing_Page(root)
root.mainloop()
        
        
        
        
        
        
        
        
        
        
        
       