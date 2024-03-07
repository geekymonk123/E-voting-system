from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as tkmb
import mysql.connector
from subprocess import call

class Voter_Login:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images/background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=1100, height=600)
        self.lgn_frame.place(x=100, y=50)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME TO THE VOTING SYSTEM"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 17, "bold"), bg="#040405",
                             fg='#FF3399',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=450, y=40, width=400, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images/vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=0, y=150)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images/hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=600, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In As Voter", bg="#040405", fg="#FF3399",
                                    font=("yu gothic ui", 15, "bold"))
        self.sign_in_label.place(x=600, y=240)
   
        
        self.vid=StringVar()
        self.aid=StringVar()
        self.flag=0
         
        
        
        
        

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Voter_id", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), show="*",insertbackground = '#6b6a69',textvariable=self.vid)
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========

        self.show_image1 = ImageTk.PhotoImage(file='images/show.png')

        self.hide_image1 = ImageTk.PhotoImage(file='images/hide.png')

        self.show_button1 = Button(self.lgn_frame, image=self.show_image1, command=self.show1, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button1.place(x=860, y=350)

    
   
        
       
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Aadhaar_No", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69',textvariable=self.aid)
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images/btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='#FF3399',command=self.validation)
        self.login.place(x=20, y=10)

        self.show_image = ImageTk.PhotoImage(file='images/show.png')

        self.hide_image = ImageTk.PhotoImage(file='images/hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        back=Button(text='Back',bg='#aef',fg='blue',cursor="hand2",font=('yu gothic ui',20,"bold"),command=self.back)
        back.place(x=100,y=600,width=100,height=50)
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')
       
        
    def show1(self):
        self.hide_button1 = Button(self.lgn_frame, image=self.hide_image1, command=self.hide1, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button1.place(x=860, y=350)
        self.username_entry.config(show='')

    def hide1(self):
        self.show_button1 = Button(self.lgn_frame, image=self.show_image1, command=self.show1, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button1.place(x=860, y=350)
        self.username_entry.config(show='*')
    def validation(self):
        if self.vid.get()=='':
            tkmb.showerror('Invalid','Please Enter your VoterID')
        elif self.aid.get()=='':
            tkmb.showerror('Invalid','Please Enter your Aadhaar Number')
        if len(self.vid.get())!=0 and len(self.aid.get())!=0:
            self.database()
    def database(self):
        try:
            conn=mysql.connector.connect(host='localhost',password='Sonu@234',user='root',database='voter')
            cur=conn.cursor()
            s='Select * from voters where VoterID=%s and AadhaarID=%s'
            data=(self.vid.get().upper(),self.aid.get())
            cur.execute(s,data)
            res=cur.fetchone()
            if cur.rowcount>0:
                tkmb.showinfo('Successful','Welcome {}! Successfully Logged in'.format(res[3]))
                with open("stored_value.txt","w") as file:
                    for i in range(len(res)):
                        file.write(str(res[i])+"\n")
                self.flag=1
            else:
                tkmb.showerror('Error','Invalid VoterID or Aadhaar Number')
            conn.commit()
            cur.close()
            conn.close()
            self.clear()
        except Exception as e:
            tkmb.showerror('Error','Due to:'+str(e))
            
    def clear(self):
        self.username_entry.delete(0,END)
        self.password_entry.delete(0,END)
        if self.flag==1:
            self.window.destroy()
            call(['python','generate_otp.py'])
    def back(self):
        self.window.destroy()
        call(['python','landing_page.py'])
            
window = Tk()
Voter_Login(window)
window.mainloop()




