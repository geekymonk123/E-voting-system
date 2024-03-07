from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter.messagebox as tkmb
import cv2
import os
import numpy as np
from subprocess import call

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("evoting system")
        
        
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
        bg_img_lbl.place(x=0,y=100,width=1530,height=710)
        
        
        title_lbl=Label(bg_img_lbl,text="Welcome To Face Recognition Pannel",font=('yu gothic ui',35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=62)
        
        #insert candidate button
        
        img4= Image.open("images/facial-recognition-banner.jpg.jpg")
        img4=img4.resize((500,350),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img_lbl,image=self.photoimg4,command=self.face_recog,bg='white',cursor="hand2")
        b1.place(x=600,y=200,width=500,height=350)
        
#         b1_1=Button(bg_img_lbl,text="Face Detector",bg='white',fg="darkblue",cursor="hand2",font=('tahoma',15,"bold"))
#         b1_1.place(x=600,y=430,width=180,height=45)
        
    
    def face_recog(self):
        #try:
            def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)

                coord=[]
                for(x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))
                    conn=mysql.connector.connect(host="localhost",user="root",password="Sujoy@2212",database="voter")
                    my_cursor=conn.cursor()

                    my_cursor.execute("select First_Name from voters where Id="+str(id))
                    i=my_cursor.fetchone()
                    i="+".join(i)

                    my_cursor.execute("select AadhaarID from voters where Id="+str(id))
                    self.j=my_cursor.fetchone()
                    self.j="+".join(self.j)

                    if confidence>77:
                        cv2.putText(img,f"Name:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Aaddhar_no:{self.j}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.j=None
                    coord=[x,y,w,h]
                return coord
            def recognize(img,clf,faceCascade):
                coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
                return img

            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            self.video_cap=cv2.VideoCapture(0)

            while True:
                ret,img=self.video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome to voting system",img)

                if cv2.waitKey(1)==13:
                    self.video_cap.release()
                    cv2.destroyAllWindows()
                    break
            if self.j=='327642376473':
                self.face_match()   
#         except Exception as es:
#                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def face_match(self):
        
        result=tkmb.askyesno("Face Match", "Face matched! Do you want to move to the next page?")
        if result:
            call(['python','voter_page.py'])

root=Tk()
obj=Face_Recognition(root)
root.mainloop()