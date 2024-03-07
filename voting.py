from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import tkinter.messagebox as tkmb
from io import BytesIO
from subprocess import call

class GiveVote:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1166x718')
        self.root.title("voting")
        self.root.resizable(0, 0)
        self.root.state('zoomed')
        self.ward,self.vid=self.getdata()
        self.result=self.database()
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
        bg_img_lbl.place(x=0,y=130,width=1300,height=600)
        
        
        title_lbl=Label(bg_img_lbl,text="Gives Your Vote To A Particular Party",font=('yu gothic ui',35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        #insert candidate button
        self.image1=Image.open(BytesIO(self.result[0][10]))
        self.image1=self.image1.resize((220,220),Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        
        b1=Button(bg_img_lbl,image=self.photo1,bg='#040405',cursor="hand2",command=lambda: self.button_clicked(self.result[0]))
        b1.place(x=150,y=150,width=220,height=220)
        
        b1_1=Button(bg_img_lbl,text=f"{self.result[0][2]} {self.result[0][3]}",bg='lightgray',fg="darkblue",cursor="hand2",font=('yu gothic ui',15,"bold"),command=lambda: self.button_clicked(self.result[0]))
        b1_1.place(x=150,y=365,width=220,height=40)
        
        
        # candidate details button
        
        self.image1=Image.open(BytesIO(self.result[1][10]))
        self.image1=self.image1.resize((220,220),Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(self.image1)
        
        b2=Button(bg_img_lbl,image=self.photo2,cursor="hand2",command=lambda: self.button_clicked(self.result[1]))
        b2.place(x=550,y=150,width=220,height=220)
        
        b2_1=Button(bg_img_lbl,text=f"{self.result[1][2]} {self.result[1][3]}",bg='lightgray',fg="darkblue",cursor="hand2",font=('yu gothic ui',15,"bold"),command=lambda: self.button_clicked(self.result[1]))
        b2_1.place(x=550,y=365,width=220,height=40)
        
        
        
        
        
         #votes
        
        self.image1=Image.open(BytesIO(self.result[2][10]))
        self.image1=self.image1.resize((220,220),Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(self.image1)
        
        b4=Button(bg_img_lbl,image=self.photo3,bg='#040405',cursor="hand2",command=lambda: self.button_clicked(self.result[2]))
        b4.place(x=950,y=150,width=220,height=220)
        
        b4_1=Button(bg_img_lbl,text=f"{self.result[2][2]} {self.result[2][3]}",bg='lightgray',fg="darkblue",cursor="hand2",font=('yu gothic ui',15,"bold"),command=lambda: self.button_clicked(self.result[2]))
        b4_1.place(x=950,y=365,width=220,height=40)

        exit=Button(text='Exit',bg='#aef',fg='blue',cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.exit)
        exit.place(x=600,y=600,width=100,height=50)

    def exit(self):
        self.root.destroy()
        call(['python','voter_page.py'])

    def getdata(self):
        try:
            with open("stored_value.txt","r") as file:
                lines=file.readlines()
                lines_new=[line.replace("\n","") for line in lines]
            self.w,self.id=lines_new[8],lines_new[1]
            return self.w,self.id
        except Exception as e:
            tkmb.showerror('Error','Due to:'+str(e))

    def database(self):
        try:
            self.conn=mysql.connector.connect(host='localhost',password='Sonu@234',user='root',database='voter')
            self.cur=self.conn.cursor()
            s="Select * from candidate natural join party where Ward=%s"
            self.cur.execute(s,[self.ward])
            res=self.cur.fetchall()
            if self.cur.rowcount>0:
               return res 
            else:
                tkmb.showerror('Error','Invalid Details...')
        except Exception as e:
            tkmb.showerror('Error','Due to:'+str(e))

    def button_clicked(self,result):
        name=result[2]+" "+result[3]
        r=tkmb.askyesnocancel('Confirm','You are voting {}\n Click Yes to Confirm'.format(name))
        if r:
            self.update(result[1],result[0])
            self.root.destroy()
            call(['python','exit.py'])

    def update(self,cid,pid):
        try:
            c=None
            q='UPDATE voters SET vote=%s WHERE VoterID=%s'
            self.cur.execute(q,(1,self.vid))
            
            q1='SELECT `count` FROM vote where Cid=%s and Pid=%s'
            self.cur.execute(q1,[cid,pid])
            res=self.cur.fetchone()
            if self.cur.rowcount>0:
                c=res[0]
            else:
                c=0
            c=int(c)
            c+=1
            q2='Insert into vote values(%s,%s,%s) ON DUPLICATE KEY UPDATE count=%s'
            data=(cid,pid,c,c)
            self.cur.execute(q2,data)
            tkmb.showinfo('Info','Congratualation!Voting done...')
            self.conn.commit()
            self.conn.close()
        except Exception as e:
             tkmb.showerror('Error',f'Due to:{str(e)}')
root=Tk()
obj=GiveVote(root)
root.mainloop()