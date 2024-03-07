from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as tkmb
import mysql.connector
from io import BytesIO
from subprocess import call

class Candidate_Details:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1166x718')
        self.root.title("candidate")
        self.root.resizable(0, 0)
        self.root.state('zoomed')
        self.ward=self.getdata()
        self.result=self.database()
       #label background image
        
        #image 1
        img = Image.open("images/banner.jpg")
        img=img.resize((500,100),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=100)
        
        #image 2
        img1 = Image.open("images/banner1.jpg")
        img1=img1.resize((500,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=100)
        
        #image 3
        img2 = Image.open("images/face-off-banner.jpg")
        img2=img2.resize((600,100),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=100)
        
        
        
        #background image
                
        img3 = Image.open("images/bg3.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img_lbl=Label(self.root,image=self.photoimg3)
        bg_img_lbl.place(x=0,y=100,width=1300,height=600)
        
        
        title_lbl=Label(bg_img_lbl,text="Candidate Details",font=('yu gothic ui',35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=-2,width=1300,height=40)
        back=Button(bg_img_lbl,text='Back',bg='#aef',fg='blue',cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.back)
        back.place(x=0,y=-2,width=100,height=40)

        #frame
        #Left frame

        main_frame=Frame(bg_img_lbl,bd=2)
        main_frame.place(x=40, y=60, width=350, height=500)

        LEFT_frame=LabelFrame(main_frame,bd=2,relief=SUNKEN,text="Candidate 1",font=("times new roman",15,"bold"),fg="darkblue")
        LEFT_frame.place(x=15, y=5, width=363, height=480)

        #Left frame.photo frame
        self.image1=Image.open(BytesIO(self.result[0][8]))
        self.image1=self.image1.resize((140,140),Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        Photo_frame=Label(LEFT_frame,bd=2,relief=FLAT,image=self.photo1)
        Photo_frame.place(x=170,y=7, width=140, height=140)

        cId_label=Label(LEFT_frame,text="Candidate Id:",font=("times new roman",16,"bold"))
        cId_label.place(x=10,y=7)
        cId_entry=ttk.Label(LEFT_frame,width=15,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[0][0]}',foreground='#3A98B9')
        cId_entry.place(x=10,y=43,height=30)

        firstname_label=Label(LEFT_frame,text="First Name:",font=("times new roman",16,"bold"))
        firstname_label.place(x=10,y=160)
        firstname_entry=ttk.Label(LEFT_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[0][1]}',foreground='#3A98B9')
        firstname_entry.place(x=125,y=160,height=30)

        lastname_label=Label(LEFT_frame,text="Last Name:",font=("times new roman",16,"bold"))
        lastname_label.place(x=10,y=210)
        lastname_entry=ttk.Label(LEFT_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[0][2]}',foreground='#3A98B9')
        lastname_entry.place(x=125,y=210,height=30)

        age_label=Label(LEFT_frame,text="Age:",font=("times new roman",16,"bold"))
        age_label.place(x=10,y=260)
        age_entry=ttk.Label(LEFT_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[0][3]}',foreground='#3A98B9')
        age_entry.place(x=125,y=260,height=30)

        sex_label=Label(LEFT_frame,text="Sex:",font=("times new roman",16,"bold"))
        sex_label.place(x=10,y=310)
        sex_entry=ttk.Label(LEFT_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[0][4]}',foreground='#3A98B9')
        sex_entry.place(x=125,y=310,height=30)

        loc_label=Label(LEFT_frame,text="Location:",font=("times new roman",16,"bold"))
        loc_label.place(x=10,y=360)
        loc_entry=ttk.Label(LEFT_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[0][5]}',foreground='#3A98B9')
        loc_entry.place(x=125,y=360,height=30)

        ward_no_label=Label(LEFT_frame,text="Ward No:",font=("times new roman",16,"bold"))
        ward_no_label.place(x=10,y=410)
        ward_no_entry=ttk.Label(LEFT_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[0][6]}',foreground='#3A98B9')
        ward_no_entry.place(x=125,y=410,height=30)

        pid_label=Label(LEFT_frame,text="Party Id:",font=("times new roman",16,"bold"))
        pid_label.place(x=10,y=80)
        pid_entry=ttk.Label(LEFT_frame,width=15,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[0][7]}',foreground='#3A98B9')
        pid_entry.place(x=10,y=116,height=30)



        #Middle frame

        main_frame1=Frame(bg_img_lbl,bd=2)
        main_frame1.place(x=460, y=60, width=350, height=500)

        Mid_frame=LabelFrame(main_frame1,bd=2,relief=SUNKEN,text="Candidate 2",font=("times new roman",15,"bold"),fg="darkblue")
        Mid_frame.place(x=15, y=5, width=363, height=480)

        #Middle frame.photo frame
        self.image2=Image.open(BytesIO(self.result[1][8]))
        self.image2=self.image2.resize((140,140),Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        Photo_frame1=Label(Mid_frame,bd=2,relief=FLAT,image=self.photo2)
        Photo_frame1.place(x=170,y=7, width=140, height=140)

        # voterId_label=Label(Mid_frame,text="Voter Id:",font=("times new roman",16,"bold"))
        # voterId_label.place(x=10,y=90)
        # voterid_entry=ttk.Label(Mid_frame,relief=SUNKEN,width=30,font=("times new roman",13,"bold"))
        # voterid_entry.place(x=125,y=90,height=30)

        cId_label=Label(Mid_frame,text="Candidate Id:",font=("times new roman",16,"bold"))
        cId_label.place(x=10,y=7)
        cId_entry=ttk.Label(Mid_frame,width=15,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[1][0]}',foreground='#3A98B9')
        cId_entry.place(x=10,y=43,height=30)

        firstname_label=Label(Mid_frame,text="First Name:",font=("times new roman",16,"bold"))
        firstname_label.place(x=10,y=160)
        firstname_entry=ttk.Label(Mid_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[1][1]}',foreground='#3A98B9')
        firstname_entry.place(x=125,y=160,height=30)

        lastname_label=Label(Mid_frame,text="Last Name:",font=("times new roman",16,"bold"))
        lastname_label.place(x=10,y=210)
        lastname_entry=ttk.Label(Mid_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[1][2]}',foreground='#3A98B9')
        lastname_entry.place(x=125,y=210,height=30)

        age_label=Label(Mid_frame,text="Age:",font=("times new roman",16,"bold"))
        age_label.place(x=10,y=260)
        age_entry=ttk.Label(Mid_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[1][3]}',foreground='#3A98B9')
        age_entry.place(x=125,y=260,height=30)

        sex_label=Label(Mid_frame,text="Sex:",font=("times new roman",16,"bold"))
        sex_label.place(x=10,y=310)
        sex_entry=ttk.Label(Mid_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[1][4]}',foreground='#3A98B9')
        sex_entry.place(x=125,y=310,height=30)

        loc_label=Label(Mid_frame,text="Location:",font=("times new roman",16,"bold"))
        loc_label.place(x=10,y=360)
        loc_entry=ttk.Label(Mid_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[1][5]}',foreground='#3A98B9')
        loc_entry.place(x=125,y=360,height=30)

        ward_no_label=Label(Mid_frame,text="Ward No:",font=("times new roman",16,"bold"))
        ward_no_label.place(x=10,y=410)
        ward_no_entry=ttk.Label(Mid_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[1][6]}',foreground='#3A98B9')
        ward_no_entry.place(x=125,y=410,height=30)

        pid_label=Label(Mid_frame,text="Party Id:",font=("times new roman",16,"bold"))
        pid_label.place(x=10,y=80)
        pid_entry=ttk.Label(Mid_frame,width=15,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[1][7]}',foreground='#3A98B9')
        pid_entry.place(x=10,y=116,height=30)


        #Right frame

        main_frame2=Frame(bg_img_lbl,bd=2)
        main_frame2.place(x=880, y=60, width=350, height=500)

        Right_frame=LabelFrame(main_frame2,bd=2,relief=SUNKEN,text="Candidate 3",font=("times new roman",15,"bold"),fg="darkblue")
        Right_frame.place(x=15, y=5, width=363, height=480)

        #Right frame.photo frame
        self.image=Image.open(BytesIO(self.result[2][8]))
        self.image=self.image.resize((140,140),Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        Photo_frame2=Label(Right_frame,bd=2,relief=FLAT,image=self.photo)
        Photo_frame2.place(x=170,y=7, width=140, height=140)


        cId_label=Label(Right_frame,text="Candidate Id:",font=("times new roman",16,"bold"))
        cId_label.place(x=10,y=7)
        cId_entry=ttk.Label(Right_frame,width=15,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[2][0]}',foreground='#3A98B9')
        cId_entry.place(x=10,y=43,height=30)

        firstname_label=Label(Right_frame,text="First Name:",font=("times new roman",16,"bold"))
        firstname_label.place(x=10,y=160)
        firstname_entry=ttk.Label(Right_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[2][1]}',foreground='#3A98B9')
        firstname_entry.place(x=125,y=160,height=30)

        lastname_label=Label(Right_frame,text="Last Name:",font=("times new roman",16,"bold"))
        lastname_label.place(x=10,y=210)
        lastname_entry=ttk.Label(Right_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[2][2]}',foreground='#3A98B9')
        lastname_entry.place(x=125,y=210,height=30)

        age_label=Label(Right_frame,text="Age:",font=("times new roman",16,"bold"))
        age_label.place(x=10,y=260)
        age_entry=ttk.Label(Right_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[2][3]}',foreground='#3A98B9')
        age_entry.place(x=125,y=260,height=30)

        sex_label=Label(Right_frame,text="Sex:",font=("times new roman",16,"bold"))
        sex_label.place(x=10,y=310)
        sex_entry=ttk.Label(Right_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[2][4]}',foreground='#3A98B9')
        sex_entry.place(x=125,y=310,height=30)

        loc_label=Label(Right_frame,text="Location:",font=("times new roman",16,"bold"))
        loc_label.place(x=10,y=360)
        loc_entry=ttk.Label(Right_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[2][5]}',foreground='#3A98B9')
        loc_entry.place(x=125,y=360,height=30)

        ward_no_label=Label(Right_frame,text="Ward No:",font=("times new roman",16,"bold"))
        ward_no_label.place(x=10,y=410)
        ward_no_entry=ttk.Label(Right_frame,width=20,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[2][6]}',foreground='#3A98B9')
        ward_no_entry.place(x=125,y=410,height=30)

        pid_label=Label(Right_frame,text="Party Id:",font=("times new roman",16,"bold"))
        pid_label.place(x=10,y=80)
        pid_entry=ttk.Label(Right_frame,width=15,relief=SUNKEN,font=("times new roman",13,"bold"),text=f'{self.result[2][7]}',foreground='#3A98B9')
        pid_entry.place(x=10,y=116,height=30)

        
    def getdata(self):
        try:
            with open("stored_value.txt","r") as file:
                lines=file.readlines()
                lines_new=[line.replace("\n","") for line in lines]
            self.w=lines_new[8]
            return self.w
        except Exception as e:
            tkmb.showerror('Error','Due to:'+str(e))

    def database(self):
        try:
            conn=mysql.connector.connect(host='localhost',password='Sonu@234',user='root',database='voter')
            cur=conn.cursor()
            s="Select * from candidate where Ward=%s"
            cur.execute(s,[self.ward])
            res=cur.fetchall()
            if cur.rowcount>0:
               return res 
            else:
                tkmb.showerror('Error','Invalid Details...')
            conn.commit()
            conn.close()
        except Exception as e:
            tkmb.showerror('Error','Due to:'+str(e))
    def back(self):
        self.root.destroy()
        call(['python','voter_page.py'])
root=Tk()
obj=Candidate_Details(root)
root.mainloop()