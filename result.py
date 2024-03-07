from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector
import tkinter.messagebox as tkmb

class Result:
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
        
        
        title_lbl=Label(bg_img_lbl,text="CHECK RESULT",font=('yu gothic ui',35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1300,height=60)

        frame=Frame(bg_img_lbl,bd=2)
        frame.place(x=0, y=70, width=1300, height=60)

        self.wloc=Label(frame,text="Ward Location:",font=('yu gothic ui',20,"bold"))
        self.wloc.place(x=10)

        self.wloc_entry=Entry(frame,width=20,font=('yu gothic ui',20,"bold"),bg='lightgrey')
        self.wloc_entry.place(x=220,y=5)

        self.wno=Label(frame,text="Ward Number:",font=('yu gothic ui',20,"bold"))
        self.wno.place(x=700)

        self.wno_entry=Entry(frame,width=20,font=('yu gothic ui',20,"bold"),bg='lightgrey')
        self.wno_entry.place(x=910,y=5)

        button_generate = Button(root, text="Get Result",font=('yu gothic ui',15,"bold"),width=15,command=self.table,cursor='hand2')
        button_generate.place(x=550,y=270)

        tree_style = ttk.Style()
        tree_style.configure("Custom.Treeview", rowheight=40)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 20),foreground='blue')
        tree_columns = ("CandidateID", "First Name","Last Name", "PartyID","Party Name","No. of Votes")  # Replace with your column names
        self.tree = ttk.Treeview(root, columns=tree_columns, show="headings",style="Custom.Treeview")

        for col in tree_columns:
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column(col, anchor="center")
        self.tree.heading("#0", text="My Heading")
        self.tree.place_forget()
        tree_style.configure("Custom.Treeview", font=("Arial", 15))
        back=Button(text='Back',bg='#aef',fg='blue',cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.back)
        back.place(x=10,y=630,width=100,height=50)
    def back(self):
        self.root.destroy()
        call(['python','admin_panel.py'])
    def table(self):
        self.wl=self.wloc_entry.get()
        self.wn=self.wno_entry.get()
    
        if self.wl and self.wn:
            res= self.getdata(self.wl,self.wn)
            if res:
                for row in self.tree.get_children():
                    self.tree.delete(row)
                for row in res:
                    self.tree.insert("", "end", values=row)
            else:
                for row in self.tree.get_children():
                    self.tree.delete(row)
                tkmb.showerror('Error', 'No data available')
        else:
            tkmb.showerror('Error','All fields required')
    def getdata(self,v1,v2):
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='Sonu@234',database='voter')
            cur=conn.cursor()

            query="SELECT candidate.Cid, candidate.FName, candidate.LName, party.Pid, party.Pname, vote.count FROM candidate INNER JOIN party ON candidate.Pid = party.Pid INNER JOIN vote ON candidate.Cid = vote.Cid AND candidate.Pid = vote.Pid WHERE candidate.Loc =%s AND candidate.Ward =%s ORDER BY vote.count DESC"

            cur.execute(query,[v1,v2])

            res=cur.fetchall()
            if len(res)<3 and len(res)!=0:
                self.tree.place(x=0,y=350,width= 1300, height=160)
                p=res[0][3]
                q="SELECT Cid,FName,LName,Pid,PName FROM candidate NATURAL JOIN party WHERE Loc=%s and Ward=%s and Pid!=%s"
                cur.execute(q,[v1,v2,p])
                data=cur.fetchall()
                data_new=[(tup + ('0',)) for tup in data]
                cur.close()
                conn.close()
                return res+data_new
            else:
                cur.close()
                conn.close()
                return res
        except Exception as e:
            tkmb.showerror('Error','due to:'+str(e))
root=Tk()
obj=Result(root)
root.mainloop()