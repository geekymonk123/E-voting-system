from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
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
        
        img4= Image.open("images/can.png")
        img4=img4.resize((180,180),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img_lbl,image=self.photoimg4,command=self.train_classifier,bg='white',cursor="hand2")
        b1.place(x=600,y=250,width=180,height=180)
        
        b1_1=Button(bg_img_lbl,text="Train Data",command=self.train_classifier,bg='white',fg="darkblue",cursor="hand2",font=('tahoma',15,"bold"))
        b1_1.place(x=600,y=430,width=180,height=45)
        
        
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
        print(ids)
        
        ####train the classifier #####
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")
        
            
        
        
        
        
        
        
        
        
        
        
if __name__ =="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()