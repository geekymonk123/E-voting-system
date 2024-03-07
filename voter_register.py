from tkinter import *
import tkinter.messagebox as tkmb
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from subprocess import call
import cv2
import os
import numpy as np

class Voter_Register:
    def __init__(self,root):
        self.root =root
        self.root.title("Registration window")
        self.root.geometry('1166x718')
        self.root.resizable(0, 0)
        self.root.state('zoomed')
#         self.root.config(bg="white")
        
        self.bg=ImageTk.PhotoImage(file="images/bg2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
#         self.left=ImageTk.PhotoImage(file="images/vector.png")
#         left=Label(self.root,image=self.left,bg='#040405').place(x=80,y=100,width=400,height=500)
        
        self.fn=StringVar()
        self.ln=StringVar()
        self.db=StringVar()
        self.gender=StringVar()
        self.vid=StringVar()
        self.aid=StringVar()
        self.addr=StringVar()
        self.ward=StringVar()
        self.pno=StringVar()
        self.c=IntVar()
        # register frame  
        
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=50,width=700,height=600)
        
        
        self.left=ImageTk.PhotoImage(file="images/vector.png")
        left=Label(self.root,image=self.left,bg='#040405').place(x=80,y=50,width=400,height=600)
        
        self.h_name = Label(frame1,text="REGISTER AS VOTER",font=('yu gothic ui', 20, "bold"), bg="white",fg='#FF3399').place(x=200,y=10)
        
        self.f_name = Label(frame1,text="First Name",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=50,y=100)
        self.txt_fname = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.fn)
        self.txt_fname.place(x=50,y=130,width=250)
        
        
        self.l_name = Label(frame1,text="Last Name",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=370,y=100)
        self.txt_lname = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.ln)
        self.txt_lname.place(x=370,y=130,width=250)
        
        
        
        self.dob = Label(frame1,text="Date Of Birth",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=50,y=170)
        self.txt_dob = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.db)
        self.txt_dob.place(x=50,y=200,width=250)
           
            
        self.sex = Label(frame1,text="SEX",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=370,y=170)
        self.r1=Radiobutton(frame1,text="Male",variable=self.gender, value="Male",font=('yu gothic ui', 15,),bg="lightgray").place(x=370,y=200)
        self.r2=Radiobutton(frame1,text="Female",variable=self.gender, value="Female",font=('yu gothic ui', 15,),bg="lightgray").place(x=500,y=200)
        self.gender.set('Male')
        
        
        
        self.address = Label(frame1,text="ADDRESS",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=50,y=240)
        self.txt_address = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.addr)
        self.txt_address.place(x=50,y=270,width=250)
        
        self.word_no = Label(frame1,text="WARD_NO",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=370,y=240)
        self.txt_word_no = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.ward)
        self.txt_word_no.place(x=370,y=270,width=250)
        
        
        self.voter_id = Label(frame1,text="VOTER_ID",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=50,y=310)
        self.txt_voter_id = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.vid)
        self.txt_voter_id.place(x=50,y=340,width=250)
        
        self.aadhaar_no = Label(frame1,text="AADHAAR_NO",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=370,y=310)
        self.txt_aadhar_no = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.aid)
        self.txt_aadhar_no.place(x=370,y=340,width=250)
        
       
        self.phno = Label(frame1,text="Phone Number",font=('yu gothic ui', 15, "bold"), bg="white",fg='#FF3399').place(x=50,y=380)
        self.txt_phno = Entry(frame1,font=('yu gothic ui', 15,),bg="lightgray",textvariable=self.pno)
        self.txt_phno.place(x=50,y=410,width=250)
        
      
        check_frame=Frame(frame1,bg='white')
        check_frame.place(x=200,y=450,width=400,height=70)
        
        check_btn=Checkbutton(check_frame,text="Agree Our Terms and Conditions",font=('times new roman',16),bg='white',onvalue=1,offvalue=0,variable=self.c)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)
        
        self.check_lbl=Label(check_frame,text='',font=('times new roman',16),fg='red',bg='white')
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)
        

        self.b1_1=Button(frame1,text="REGISTER",bg='darkblue',fg="#FF3399",cursor="hand2",font=('tahoma',20,"bold"),command=self.validation)
        self.b1_1.place(x=20,y=520,width=300,height=40)
        
        self.b2=Button(frame1,text="TRAINING",bg='darkblue',fg="#FF3399",cursor="hand2",font=('tahoma',20,"bold"),command=self.train_classifier)
        self.b2.place(x=380,y=520,width=300,height=40)

        back=Button(text='Back',bg='#aef',fg='blue',cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.back)
        back.place(x=80,y=600,width=100,height=50)
    def checkphno(self,phno):
        if phno.isdigit():
            return True
        else:
            return False
    def validation(self):
        if self.fn.get()=='':
            tkmb.showerror('Invalid','Please Enter Your First Name',parent=self.root)
        elif self.ln.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Last Name',parent=self.root)
        elif self.db.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Date of Birth',parent=self.root)
        elif self.gender.get()=='':
            tkmb.showerror('Invalid','Please Select Your Gender',parent=self.root)
        elif self.addr.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Address',parent=self.root)
        elif self.ward.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Ward Number',parent=self.root)
        elif self.vid.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Voter Id',parent=self.root)
        elif self.aid.get()=='':
            tkmb.showerror('Invalid','Please Enter Your Aadhaar Number',parent=self.root)
        elif self.pno.get()=='':
            tkmb.showerror('Invalid','Please Enter Mobile Number',parent=self.root)
        elif len(self.aid.get())!=0:
            x=self.checkphno(self.aid.get())
            if(x==False):
                 tkmb.showerror('Invalid','Only Numbers allowed in Aadhaar Number')
            elif len(self.aid.get())!=12:        
                tkmb.showerror('Invalid','Aadhaar Number must be 12 digits',parent=self.root)
        
        if len(self.pno.get())!=0:
            x=self.checkphno(self.pno.get())
            if(x==False):
                tkmb.showerror('Invalid','Only Numbers allowed in Phone Number')
            elif len(self.pno.get())!=10:
                tkmb.showerror('Invalid','Phone Number must be 10 digits',parent=self.root)

        if len(self.vid.get())!=0 and len(self.aid.get())!=0 and len(self.fn.get())!=0 and len(self.ln.get())!=0 and len(self.pno.get())!=0 and len(self.addr.get())!=0 and len(self.db.get())!=0 and len(self.ward.get())!=0 and len(self.gender.get())!=0:
            if self.c.get()==0:
                self.check_lbl.config(text='Please Agree Our Terms and Conditions',fg='red')
            else:
                self.check_lbl.config(text="Checked",fg='green')
                self.generate_dataset()
    def database(self):
        try:
            conn=mysql.connector.connect(host='localhost',password='Sonu@234',user='root',database='voter')
            cur=conn.cursor()
            q='SELECT * FROM voters'
            cur.execute(q)
            myresult=cur.fetchall()
            id=1
            for x in myresult:
                id+=1
            res=tkmb.askokcancel('Confirmation','Opening Camera for image generation....')
            if res:
                self.generate_dataset()
                s='INSERT INTO voters Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                data=(id,self.vid.get().upper(),self.aid.get(),self.fn.get().upper(),self.ln.get().upper(),self.db.get(),self.gender.get(),self.addr.get(),self.ward.get(),self.pno.get(),0)
                cur.execute(s,data)
                conn.commit()
                conn.close()
                tkmb.showinfo(title='Registration' , message="Congratulation!Successfully Signed Up")
                tkmb.showinfo('Generate','Click on training to train dataset')
                
            else:
                tkmb.showerror('Registration','Generate image for registration...')
        except Exception as e:
            tkmb.showerror('Error',f'Due to:{str(e)}')
    def back(self):
        self.root.destroy()
        call(['python','admin_panel.py'])
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_dob.delete(0,END)
        self.txt_address.delete(0,END)
        self.txt_word_no.delete(0,END)
        self.txt_voter_id.delete(0,END)
        self.txt_aadhar_no.delete(0,END)
        self.txt_phno.delete(0,END)
        self.check_lbl.config(text="")
    def generate_dataset(self):
        try:
            conn=mysql.connector.connect(host='localhost',password='Sonu@234',user='root',database='voter')
            cur=conn.cursor()
            q='SELECT * FROM voters'
            cur.execute(q)
            myresult=cur.fetchall()
            id=1
            for x in myresult:
                id+=1
            res=tkmb.askokcancel('Confirmation','Opening Camera for image generation....')
            if res:
                face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face.detectMultiScale(gray,1.3,5)
                    
                    #scaling factor=1.3
                    #mininum neighbour=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face1=cv2.resize(face_cropped(my_frame),(450,450))
                        face1=cv2.cvtColor(face1,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face1)
                        cv2.putText(face1,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face1)
                
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
            
                cap.release()
                cv2.destroyAllWindows()
                tkmb.showinfo("Result","Generating dataset completed successfully")
                s='INSERT INTO voters Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                data=(id,self.vid.get().upper(),self.aid.get(),self.fn.get().upper(),self.ln.get().upper(),self.db.get(),self.gender.get(),self.addr.get(),self.ward.get(),self.pno.get(),0)
                cur.execute(s,data)
                conn.commit()
                conn.close()
                tkmb.showinfo(title='Registration' , message="Congratulation!Successfully Signed Up")
                tkmb.showinfo('Generate','Click on training to train dataset')
                
            else:
                tkmb.showerror('Registration','Generate image for registration...')
            
        except Exception as es:
            tkmb.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')#gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        ####train the classifier #####
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        tkmb.showinfo("Result","Training dataset completed")
        self.c.set(False)
        self.clear()
        
root =Tk()
obj = Voter_Register(root)
root.mainloop()

