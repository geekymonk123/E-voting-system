from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from subprocess import call

class AdminPanel:
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
        
        
        img3 = Image.open("images/bg3.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img_lbl=Label(self.root,image=self.photoimg3)
        bg_img_lbl.place(x=0,y=130,width=1300,height=630)
        
        
        title_lbl=Label(bg_img_lbl,text="SMART E-VOTING SYSTEM WITH FACE RECOGNITION",font=('yu gothic ui',35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1300,height=60)
        
        #insert candidate button
        
        img4= Image.open("images/log.jpg")
        img4=img4.resize((240,300),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img_lbl,image=self.photoimg4,bg='#040405',cursor="hand2",command=self.cinsert)
        b1.place(x=80,y=150,width=220,height=220)
        
        b1_1=Button(bg_img_lbl,text="Insert Candidate",bg='lightgray',fg="darkblue",cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.cinsert)
        b1_1.place(x=80,y=350,width=220,height=40)
        
        
        #delete candidate button
        
        img5= Image.open("images/download.png")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b2=Button(bg_img_lbl,image=self.photoimg5,bg='#040405',cursor="hand2",command=self.cdelete)
        b2.place(x=380,y=150,width=220,height=220)
        
        b2_1=Button(bg_img_lbl,text="Delete Candidate",bg='lightgray',fg="darkblue",cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.cdelete)
        b2_1.place(x=380,y=350,width=220,height=40)
        
        
        
        
        #insert voter button
        
        img6= Image.open("images/d_voter.png")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b3=Button(bg_img_lbl,image=self.photoimg6,bg='#040405',cursor="hand2",command=self.vinsert)
        b3.place(x=680,y=150,width=220,height=220)
        
        b3_1=Button(bg_img_lbl,text="Insert Voter",bg='lightgray',fg="darkblue",cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.vinsert)
        b3_1.place(x=680,y=350,width=220,height=40)
        
        
        
         #delete voter button
        
        img7= Image.open("images/voter.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b4=Button(bg_img_lbl,image=self.photoimg7,bg='#040405',cursor="hand2",command=self.vdelete)
        b4.place(x=980,y=150,width=220,height=220)
        
        b4_1=Button(bg_img_lbl,text="Delete Voter",bg='lightgray',fg="darkblue",cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.vdelete)
        b4_1.place(x=980,y=350,width=220,height=40)

        exit=Button(text='Exit',bg='#aef',fg='blue',cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.exit)
        exit.place(x=100,y=600,width=100,height=50)
        
        sr=Button(text='Show Result',bg='#aef',fg='blue',cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.result)
        sr.place(x=1000,y=600,width=200,height=50)

    def cinsert(self):
        self.root.destroy()
        call(['python','candidate_register.py'])
    def cdelete(self):
        self.root.destroy()
        call(['python','candidate_delete.py'])
    def vinsert(self):
        self.root.destroy()
        call(['python','voter_register.py'])
    def vdelete(self):
        self.root.destroy()
        call(['python','voter_delete.py'])
    def exit(self):
        self.root.destroy()
        call(['python','landing_page.py'])

    def result(self):
        self.root.destroy()
        call(['python','result.py'])

root=Tk()
obj=AdminPanel(root)
root.mainloop()