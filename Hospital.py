from tkinter import *
from datetime import date
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import time
import datetime
from datetime import datetime
from datetime import timedelta
import smtplib
import mysql.connector
import pyttsx3
import os
import webbrowser
import datetime
import speech_recognition as sr
root = Tk()
root.title("Blood bank management system")
root.iconbitmap("aa.ico")
root.geometry("900x500+300+150")
root.resizable(0, 0)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Welcome to our Blood bank management system. This is our final year project for BCA. This project is made by Munish Kumar , Shashank Shekhar , Pratap Mukherjee and  Bharat Yadav  ") 
class maincode:
     def takeCommand1(self):
         import speech_recognition as sr
         r = sr.Recognizer()
         mic = sr.Microphone(device_index=1)
         with mic as source:
             r.adjust_for_ambient_noise(source, duration=1)
             audio = r.listen(source, timeout=5)
         try:
             SQ2 = r.recognize_google(audio, language='English')
         except:
             messagebox.showerror('Blood bank management system', 'Sorry! Not able to uderstand')
             pass
         return SQ2





     def login(self):

         self.var1 = self.e1.get()
         self.var2 = self.e2.get()
         import mysql.connector
         mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
         cursor=mydb.cursor()
         cursor.execute("SELECT * FROM patient WHERE Patient_ID='"+self.var1+"' and Password='"+self.var2+"'") 
         self.ab = cursor.fetchone()
         if self.ab!=None:
               
             self.under_fm=Frame(root,height=500,width=900,bg='#fff')
             self.under_fm.place(x=0,y=0)
             self.fm2=Frame(root,bg='#0f624c',height=80,width=900)
             self.fm2.place(x=0,y=0)

            

             self.lbb=Label(self.fm2,bg='#0f624c')
             self.lbb.place(x=15,y=5)
             self.ig=PhotoImage(file='hospital.png')
             self.lbb.config(image=self.ig)
             self.lb3=Label(self.fm2,text='WELCOME TO OUR HOSPITAL',fg='White',bg='#0f624c',font=('Arial',30,'bold'))
             self.lb3.place(x=180,y=17)
             self.lbb5=Label(self.fm2,bg='#0f624c')
             self.lbb5.place(x=800,y=5)
             self.ig3=PhotoImage(file='hospital.png')
             self.lbb5.config(image=self.ig3)


            

             self.name=Label(root,text="Name : ",bg='#fff',fg="black",font=('Arial',10,'bold'))
             self.name.place(x=5,y=83)
             self.name1=Label(root,text=self.ab[1],fg='black',bg='#fff',font=('Arial',10,'bold'))
             self.name1.place(x=60,y=83)

          

             self.today=date.today()
             self.dat=Label(root,text='Date : ',bg='#fff',fg='black',font=('Arial',10,'bold'))
             self.dat.place(x=740,y=83)
             self.dat2 = Label(root, text=self.today, bg='#fff', fg='black', font=('Arial', 10, 'bold'))
             self.dat2.place(x=790, y=83)

             self.cur()

         else:
               messagebox.showerror('Blood bank management system', 'Your ID or Password is not Valid')
            
     def cur(self):
             self.fm3=Frame(root,bg='#fff',width=900,height=390)
             self.fm3.place(x=0,y=110)

        

             def clock():
                 h = str(time.strftime("%H"))
                 m = str(time.strftime("%M"))
                 s = str(time.strftime("%S"))

                 if int(h) >=12 and int(m) >=0:
                       self.lb7_hr.config(text="PM")

                 
                 self.lb1_hr.config(text=h)
                 self.lb3_hr.config(text=m)
                 self.lb5_hr.config(text=s)

                 self.lb1_hr.after(200, clock)

             self.lb1_hr = Label(self.fm3, text='12', font=('times new roman', 20, 'bold'), bg='#fc1c1c', fg='white')
             self.lb1_hr.place(x=560, y=0, width=60, height=30)


             self.lb3_hr = Label(self.fm3, text='05', font=('times new roman', 20, 'bold'), bg='#0ee38b', fg='white')
             self.lb3_hr.place(x=630, y=0, width=60, height=30)


             self.lb5_hr = Label(self.fm3, text='37', font=('times new roman', 20, 'bold'), bg='#2b1dff', fg='white')
             self.lb5_hr.place(x=700, y=0, width=60, height=30)


             self.lb7_hr = Label(self.fm3, text='AM', font=('times new roman', 17, 'bold'), bg='#2b1dff', fg='white')
             self.lb7_hr.place(x=770, y=0, width=60, height=30)


             clock()

            


             self.canvas8 = Canvas(self.fm3, bg='black', width=400, height=300)
             self.canvas8.place(x=475, y=37)
             self.photo9=PhotoImage(file="bb.png")
             self.canvas8.create_image(0,0,image=self.photo9,anchor=NW)

             self.develop=Label(self.fm3,text='Developed By - Munish Kumar , Shashank Shekhar , Pratap Mukherjee and  Bharat Yadav',bg='#fff',fg='blue',
                               font=('Cursive',12,'italic','bold'))
             self.develop.place(x=50,y=350)

            

             self.bt1=Button(self.fm3,text='Add Patient deatils',fg='#fff',bg='#ff0076',font=('Arial',15,'bold'),width=200,
                          height=-3,bd=10,relief='flat',command=self.addp,cursor='hand2')
             self.bt1.place(x=10,y=40)
             self.logo = PhotoImage(file='bt1.png')
             self.bt1.config(image=self.logo, compound=LEFT)
             self.small_logo = self.logo.subsample(1,1)
             self.bt1.config(image=self.small_logo)

            

             self.bt2 = Button(self.fm3, text='  Appointment', fg='#fff', bg='#ff0076', font=('Arial', 15, 'bold'),
                            width=200,height=-3, bd=10,relief='flat',command=self.appoint,cursor='hand2')
             self.bt2.place(x=250, y=40)
             self.log = PhotoImage(file='bt2.png')
             self.bt2.config(image=self.log, compound=LEFT)
             self.small_log = self.log.subsample(1, 1)
             self.bt2.config(image=self.small_log)

            

             self.bt3 = Button(self.fm3, text=' Edit Patient deatils', fg='#fff', bg='#ff0076', font=('Arial', 15, 'bold'),
                           width=200,height=-3,bd=10,relief='flat',cursor='hand2',command=self.edit)
             self.bt3.place(x=10, y=120)
             self.logb = PhotoImage(file='bt3.png')
             self.bt3.config(image=self.logb, compound=LEFT)
             self.small_logb = self.logb.subsample(1, 1)
             self.bt3.config(image=self.small_logb)

            

             self.bt4 = Button(self.fm3, text='  Blood Enquiry', fg='#fff', bg='#ff0076', font=('Arial', 15, 'bold'),
                          width=200,height=-3,bd=7,relief='flat',cursor='hand2',command=self.email)
             self.bt4.place(x=250, y=120)
             self.log4 = PhotoImage(file='bt4.png')
             self.bt4.config(image=self.log4, compound=LEFT)
             self.small_log4 = self.log4.subsample(1, 1)
             self.bt4.config(image=self.small_log4)

            

             self.bt5 = Button(self.fm3, text=' Delete Patient detail', fg='#fff', bg='#ff0076', font=('Arial', 15, 'bold'),
                          width=200,height=-3,bd=7,relief='flat',cursor='hand2',command=self.delete)
             self.bt5.place(x=10, y=200)
             self.log5 = PhotoImage(file='bt5.png')
             self.bt5.config(image=self.log5, compound=LEFT)
             self.small_log5 = self.log5.subsample(1, 1)
             self.bt5.config(image=self.small_log5)

           

             self.bt6 = Button(self.fm3, text='Blood Available', fg='#fff', bg='#ff0076', font=('Arial', 15, 'bold'),
                           width=200,height=-3,bd=7, relief='flat',cursor='hand2',command=self.show)
             self.bt6.place(x=250, y=200)
             self.log6 = PhotoImage(file='bt6.png')
             self.bt6.config(image=self.log6, compound=LEFT)
             self.small_log6 = self.log6.subsample(1, 1)
             self.bt6.config(image=self.small_log6)

            

             self.bt7 = Button(self.fm3, text=' Search Doctors', fg='#fff', bg='#ff0076', font=('Arial', 15, 'bold'),
                          width=200,height=0,bd=7, relief='flat',cursor='hand2',command=self.search)
             self.bt7.place(x=10, y=280)
             self.log7 = PhotoImage(file='bt7.png')
             self.bt7.config(image=self.log7, compound=LEFT)
             self.small_log7 = self.log7.subsample(1, 1)
             self.bt7.config(image=self.small_log7)

             
             try:

                self.bt8 = Button(self.fm3, text='  log Out', fg='#fff', bg='#ff0076', font=('Arial', 15, 'bold'),
                               width=200,
                          height=-3, bd=7, relief='flat',cursor='hand2',command=self.code)
                self.bt8.place(x=250, y=280)
                self.log8 = PhotoImage(file='bt8.png')
                self.bt8.config(image=self.log8, compound=LEFT)
                self.small_log8 = self.log8.subsample(1, 1)
                self.bt8.config(image=self.small_log8)

             except:

               self.bt9 = ttk.Button(self.fm3, text="ram", bg='#11d09a', font=('Arial', 15, 'bold'), width=150,
                                     height=0)
               self.bt9.place(x=10, y=350)
               self.log9 = PhotoImage(file='bt8.png')
               self.bt9.config(image=self.log9, compound=LEFT)
               self.small_log9 = self.log9.subsample(3, 3)
               self.bt9.config(image=self.small_log9)






     def mainclear(self):
         self.e1.delete(0,END)
         self.e2.delete(0,END)


    

     def addp(self):
         class temp(maincode):

             def pa(self):

                 self.fm=Frame(root,bg='#a7ecd9',width=900,height=390)
                 self.fm.place(x=0,y=110)
                 self.fm1=Frame(self.fm,bg='#fff',width=500,height=360,bd=5,relief='flat')
                 self.fm1.place(x=200,y=15)
                 self.backbt = Button(self.fm, width=60, bg='#a7ecd9',activebackground='#a7ecd9', bd=0, relief='flat',\
                                                                                                 command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log0 = self.log.subsample(1, 1)
                 self.backbt.config(image=self.small_log0)

                 
                 self.f=Frame(self.fm1,bg='#0f624c',width=490,height=35)
                 self.f.place(x=0,y=0)
                 self.ll=Label(self.f,text='ADD PATIENT DETAILS',fg='#fff',bg='#0f624c',font=('Arial',12,'bold'))
                 self.ll.place(x=150,y=6)
                 self.lb=Label(self.fm1,text='Patient ID',fg='black',bg='#fff',font=('Arial',10,'bold'))
                 self.lb.place(x=20,y=90)
                 self.lb2 = Label(self.fm1, text='Patient Name', fg='black', bg='#fff', font=('Arial', 10, 'bold'))
                 self.lb2.place(x=20, y=130)
                 self.lb3 = Label(self.fm1, text='Blood Group', fg='black', bg='#fff', font=('Arial', 10, 'bold'))
                 self.lb3.place(x=20, y=170)
                 self.lb4= Label(self.fm1, text='Wants to donate blood', fg='black', bg='#fff', font=('Arial', 10, 'bold'))
                 self.lb4.place(x=20, y=210)
                 self.lb5 = Label(self.fm1, text='Blood related disease', fg='black', bg='#fff', font=('Arial', 10, 'bold'))
                 self.lb5.place(x=20, y=250)

               

                 self.ee1=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee1.place(x=180,y=90)
                 self.ee2=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee2.place(x=180,y=130)
                 self.ee3=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee3.place(x=180,y=170)
                 self.ee4=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee4.place(x=180,y=210)
                 self.ee5=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee5.place(x=180,y=250)

                 self.bt=Button(self.fm1,text='Submit',width=41,bg='red',fg='#fff',font=('Arial',10,'bold'),bd=5,
                          relief='flat',command=self.submit1)
                 self.bt.place(x=70,y=290)
                 

                 self.mike1 = Button(self.fm1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.ee1.insert(END, self.takeCommand()))
                 self.mike1.place(x=420, y=90)
                 self.log = PhotoImage(file='mike.png')
                 self.mike1.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(1, 1)
                 self.mike1.config(image=self.small_log)



                 self.mike1 = Button(self.fm1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.ee2.insert(END, self.takeCommand()))
                 self.mike1.place(x=420, y=130)
                 self.log = PhotoImage(file='mike.png')
                 self.mike1.config(image=self.log, compound=LEFT)
                 self.small_log1 = self.log.subsample(1, 1)
                 self.mike1.config(image=self.small_log1)


                 self.mike2 = Button(self.fm1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.ee3.insert(END, self.takeCommand()))
                 self.mike2.place(x=420, y=170)
                 self.log = PhotoImage(file='mike.png')
                 self.mike2.config(image=self.log, compound=LEFT)
                 self.small_log2 = self.log.subsample(1, 1)
                 self.mike2.config(image=self.small_log2)


                 self.mike3 = Button(self.fm1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.ee4.insert(END, self.takeCommand()))
                 self.mike3.place(x=420, y=210)
                 self.log = PhotoImage(file='mike.png')
                 self.mike3.config(image=self.log, compound=LEFT)
                 self.small_log3 = self.log.subsample(1, 1)
                 self.mike3.config(image=self.small_log3)
                 

                 self.mike4 = Button(self.fm1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.ee5.insert(END, self.takeCommand()))
                 self.mike4.place(x=420, y=250)
                 self.log = PhotoImage(file='mike.png')
                 self.mike4.config(image=self.log, compound=LEFT)
                 self.small_log4 = self.log.subsample(1, 1)
                 self.mike4.config(image=self.small_log4)



             def takeCommand(self):
                 import speech_recognition as sr
                 r = sr.Recognizer()
                 mic = sr.Microphone(device_index=1)
                 with mic as source:
                     r.adjust_for_ambient_noise(source, duration=1)
                     audio = r.listen(source, timeout=5)
                 try:
                     SQ1 = r.recognize_google(audio, language='English')
                     
                 except:
                     messagebox.showerror('Blood bank management system', 'Sorry! Not able to uderstand')
                     pass
                 return SQ1






              




             def submit1(self):

                 self.id=self.ee1.get()
                 self.ttl=self.ee2.get()
                 self.aut=self.ee3.get()
                 self.edi=self.ee4.get()
                 self.pri=self.ee5.get()
                 import mysql.connector
                 mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
                 cursor=mydb.cursor()
                 s="INSERT INTO details (SNO,patient_name,blood_group,donate,disease) VALUES(%s,%s,%s,%s,%s)"
                 b1=(self.id,self.ttl,self.aut,self.edi,self.pri)
                 cursor.execute(s,b1)
                 mydb.commit()
                 self.clear()

             def clear(self):
                 self.ee1.delete(0,END)
                 self.ee2.delete(0,END)
                 self.ee3.delete(0,END)
                 self.ee4.delete(0,END)
                 self.ee5.delete(0,END)

         obj=temp()
         obj.pa()


      
     def appoint(self):
         class test(maincode):
              def issue(self):
                  self.f = Frame(root, bg='#a7ecd9', width=900, height=390)
                  self.f.place(x=0, y=110)

                  self.fmi=Canvas(self.f,bg='#fff',width=900,height=390,bd=0,relief='flat')
                  self.fmi.place(x=0,y=0)


                  self.fc=Frame(self.fmi,bg='#fff',width=330,height=230,bd=4,relief='flat')
                  self.fc.place(x=70,y=20)

                  self.ffb=Frame(self.fc,bg='#0f624c',bd=2,relief='flat',width=330,height=35)
                  self.ffb.place(x=0,y=0)

                  self.lc=Label(self.ffb,text='Doctor  Appointment',bg='#0f624c',fg='#fff',font=('Arial',12,'bold'))
                  self.lc.place(x=55,y=5)

                  self.lb=Label(self.fc,text='Doctor-ID',bg='#fff',fg='black',font=('Arial',10,'bold'))
                  self.lb.place(x=15,y=60)
                  self.ob=Label(self.fc,text='or',bg='#fff',fg='black',font=('cursive',12,'bold'))
                  self.ob.place(x=180,y=90)
                  self.em = Entry(self.fc, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                  self.em.place(x=105, y=60)
                  self.lb = Label(self.fc, text='Doctor-Name', bg='#fff', fg='black', font=('Arial', 10, 'bold'))
                  self.lb.place(x=15, y=120)
                  self.em2 = Entry(self.fc, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                  self.em2.place(x=105, y=120)
                  self.bt = Button(self.fc, text='Submit', width=14, bg='red', fg='#fff', font=('Arial', 10, 'bold'),
                                 bd=5,relief='flat',command=self.check)
                  self.bt.place(x=15,y=180)

                  self.bt3=Button(self.fc,text='Clear',width=14,bg='blue',fg='#fff',font=('arial',10,'bold'),bd=5,
                            relief='flat',command=self.clr)
                  self.bt3.place(x=165,y=180)

                  self.backbt = Button(self.fmi,width=60, bg='#fff',activebackground='#fff',bd=0, relief='flat',
                                       command=self.cur)
                  self.backbt.place(x=5, y=5)
                  self.log = PhotoImage(file='back.png')
                  self.backbt.config(image=self.log, compound=LEFT)
                  self.small_log = self.log.subsample(1, 1)
                  self.backbt.config(image=self.small_log)



                  
                  self.mike1 = Button(self.fc, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.em.insert(END, self.takeCommand()))
                  self.mike1.place(x=300, y=60)
                  self.log = PhotoImage(file='mike.png')
                  self.mike1.config(image=self.log, compound=LEFT)
                  self.small_log1 = self.log.subsample(1, 1)
                  self.mike1.config(image=self.small_log1)



                  

                  self.mike2 = Button(self.fc, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.em2.insert(END, self.takeCommand()))
                  self.mike2.place(x=300, y=120)
                  self.log = PhotoImage(file='mike.png')
                  self.mike2.config(image=self.log, compound=LEFT)
                  self.small_log2 = self.log.subsample(1, 1)
                  self.mike2.config(image=self.small_log2)


              def takeCommand(self):
                  import speech_recognition as sr
                  r = sr.Recognizer()
                  mic = sr.Microphone(device_index=1)
                  with mic as source:
                      r.adjust_for_ambient_noise(source, duration=1)
                      audio = r.listen(source, timeout=5)
                  try:
                      SQ1 = r.recognize_google(audio, language='English')
                  except:
                      messagebox.showerror('Blood bank management system', 'Sorry! Not able to uderstand')
                      pass
                  return SQ1





              def check(self):
                  self.ai=self.em.get()
                  self.b2=self.em2.get()
                  import mysql.connector
                  mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
                  cursor=mydb.cursor()
                  cursor.execute("SELECT * FROM doctor WHERE D_ID='"+self.ai+"' or D_name='"+self.b2+"'")
                  self.var=cursor.fetchone()
                  if self.var!=None:
                        self.lb1=Label(self.fmi,text='Name :',fg='black',font=('Arial',10,'bold'))
                        self.lb1.place(x=60,y=255)
                        self.lb2 = Label(self.fmi, text=self.var[1], fg='black', font=('Arial', 10, 'bold'))
                        self.lb2.place(x=150, y=255)
                        self.lb3 = Label(self.fmi, text='Cabin :',fg='black', font=('Arial', 10, 'bold'))
                        self.lb3.place(x=60, y=275)
                        self.lb4 = Label(self.fmi, text=self.var[2],fg='black', font=('Arial', 10, 'bold'))
                        self.lb4.place(x=150, y=275)
                        self.lb5 = Label(self.fmi, text='Department:', fg='black', font=('Arial', 10, 'bold'))
                        self.lb5.place(x=60, y=295)
                        self.lb6 = Label(self.fmi, text=self.var[3], fg='black', font=('Arial', 10, 'bold'))
                        self.lb6.place(x=150, y=295)
                        self.lb7 = Label(self.fmi, text='Contact :', fg='black', font=('Arial', 10, 'bold'))
                        self.lb7.place(x=60, y=315)
                        self.lb8 = Label(self.fmi, text=self.var[4],fg='black', font=('Arial', 10, 'bold'))
                        self.lb8.place(x=150, y=315)
                        self.lb9 = Label(self.fmi, text='Qualification :', fg='black', font=('Arial', 10, 'bold'))
                        self.lb9.place(x=60, y=335)
                        self.lb10 = Label(self.fmi, text=self.var[5],fg='black', font=('Arial', 10, 'bold'))
                        self.lb10.place(x=152, y=335)


                        self.fr=Frame(self.fmi,bg='#fff',bd=5,relief='flat',width=450,height=320)
                        self.fr.place(x=420,y=20)
                        self.ff=Frame(self.fr,bg='#0f624c',bd=2,relief='flat',width=450,height=35)
                        self.ff.place(x=0,y=0)
                        self.lb=Label(self.ff,text='Patient Detail',bg='#0f624c',fg='#fff',font=('Arial',12,'bold'))
                        self.lb.place(x=165,y=5)
                        self.tt=Label(self.fr,text='Patient-ID',bg='#fff',fg='black',font=('arial',10,'bold'))
                        self.tt.place(x=50,y=60)
                        self.e1 = Entry(self.fr, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                        self.e1.place(x=160, y=60)
                        self.ttp = Label(self.fr, text='Patient-Name', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                        self.ttp.place(x=50, y=110)
                        self.e2 = Entry(self.fr, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                        self.e2.place(x=160, y=110)
                        self.bt1 = Button(self.fr, text='Submit', width=35, bg='#0f624c', fg='#fff', font=('Arial', 10,
                                                                    'bold'),bd=5,relief='flat',command=self.data)
                        self.bt1.place(x=60, y=160)

                        self.bt1 = Button(self.fr, text='Submit', width=35, bg='#0f624c', fg='#fff', font=('Arial', 10,
                                                        'bold'), bd=5,relief='flat',command=self.data, state=ACTIVE)
                        self.bt1.place(x=60, y=160)


                        self.mike10 = Button(self.fr, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.e1.insert(END, self.takeCommand()))
                        self.mike10.place(x=350, y=60)
                        self.log = PhotoImage(file='mike.png')
                        self.mike10.config(image=self.log, compound=LEFT)
                        self.small_log10 = self.log.subsample(1, 1)
                        self.mike10.config(image=self.small_log10)



                  

                        self.mike11 = Button(self.fr, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.e2.insert(END, self.takeCommand()))
                        self.mike11.place(x=350, y=110)
                        self.log = PhotoImage(file='mike.png')
                        self.mike11.config(image=self.log, compound=LEFT)
                        self.small_log11 = self.log.subsample(1, 1)
                        self.mike2.config(image=self.small_log11)




              def clr(self):
                  self.em.delete(0, END)
                  self.em2.delete(0, END)
          

              def data(self):
                   self.vva=self.e1.get()
                   self.vvb=self.e2.get()
                   import mysql.connector
                   mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
                   cursor=mydb.cursor()
                   s="INSERT INTO  p_details (P_ID,P_NAME) VALUES(%s,%s)"
                   b1=(self.vva,self.vvb)
                   cursor.execute(s,b1)
                   mydb.commit()
                   self.boot=Tk()
                   self.boot.title("Select the date")
                   self.boot.iconbitmap("aa.ico")
                   self.boot.configure(bg='#fff')
                   self.boot.geometry("300x500+1202+50")
                   self.boot.resizable(0,0)
                    
                   self.x = date.today()
                   self.cal = Calendar(self.boot, selectmode="day", bg='black',year=2020,month=9,day=6)
                   self.cal.place(x=20,y=200)
                   btn1 = Button(self.boot, text="Confirm Date",command=self.get_data,  bg='#ff0076',
                                      font=('arial', 10, 'bold'),
                                      fg='#fff', relief='flat')
                   btn1.place(x=90,y=400)
                   self.boot.mainloop()
              def get_data(self):
                   self.datecon=self.cal.selection_get()
                   self.vva=self.e1.get()
                   self.vvb=self.e2.get()
                   import mysql.connector
                   mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
                   cursor=mydb.cursor()
                   s2="INSERT INTO  p_appointment (P_ID,P_NAME,appointment_date) VALUES(%s,%s,%s)"
                   b2=(self.vva,self.vvb,self.datecon)
                   cursor.execute(s2,b2)
                   mydb.commit()
                   messagebox.showinfo("Blood management system","You successfully get an Appointment !")

         obk=test()
         obk.issue()



     def edit(self):
         class editing(maincode):
               def edbooks(self):


                     self.ffm=Frame(root,bg='#a7ecd9',width=900,height=390)
                     self.ffm.place(x=0,y=110)
                     self.fm1 = Frame(self.ffm, bg='#fff', width=500, height=200, bd=5, relief='flat')
                     self.fm1.place(x=200, y=15)
                     self.ed = Frame(self.fm1, bg='#0f624c', bd=0, relief='flat', width=490, height=35)
                     self.ed.place(x=0,y=0)
                     self.lab = Label(self.ed, text='EDIT PATIENT DETAILS', bg='#0f624c', fg='#fff', font=('Arial', 12,
                                                                                                    'bold'))
                     self.lab.place(x=165, y=5)
                     self.label3=Label(self.fm1,text='Patient-ID',bg='#fff',fg='black',font=('arial',10,'bold'))
                     self.label3.place(x=85,y=65)
                     self.entry=Entry(self.fm1,width=30,bd=4,relief='groove',font=('arial',8,'bold'))
                     self.entry.place(x=188,y=65)
                     self.button7 = Button(self.fm1, text='Search', bg='#0f624c', fg='#fff', width=24, height=0,
                                  font=('Arial', 10, 'bold'),command=self.search)
                     self.button7.place(x=140,y=120)

                     self.backbt = Button(self.ffm, width=60, bg='#a7ecd9',activebackground='#a7ecd9',
                                          bd=0, relief='flat', command=self.cur)
                     self.backbt.place(x=0, y=0)
                     self.log = PhotoImage(file='back.png')
                     self.backbt.config(image=self.log, compound=LEFT)
                     self.small_log = self.log.subsample(1, 1)
                     self.backbt.config(image=self.small_log)




                     self.mike1 = Button(self.fm1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.entry.insert(END, self.takeCommand()))
                     self.mike1.place(x=380, y=62)
                     self.log = PhotoImage(file='mike.png')
                     self.mike1.config(image=self.log, compound=LEFT)
                     self.small_log1 = self.log.subsample(1, 1)
                     self.mike1.config(image=self.small_log1)
               def takeCommand(self):
                   import speech_recognition as sr
                   r = sr.Recognizer()
                   mic = sr.Microphone(device_index=1)
                   with mic as source:
                       r.adjust_for_ambient_noise(source, duration=1)
                       audio = r.listen(source, timeout=5)
                   try:
                       SQ1 = r.recognize_google(audio, language='English')
                   except:
                       messagebox.showerror('Blood bank management system', 'Sorry! Not able to uderstand')
                       pass
                   return SQ1


                


               def search(self):
                     self.datas=self.entry.get()
                     import mysql.connector
                     mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
                     cursor=mydb.cursor()
                     cursor.execute("SELECT * FROM details WHERE SNO='"+self.datas+"'")
                     self.val=cursor.fetchone()
                     if self.val!=None:

                          self.edcat=Tk()
                          self.edcat.title("BLOOD BANK MANAGEMENT SYSTEM")
                          self.edcat.geometry("300x320+590+320")
                          self.edcat.configure(bg='#fff')
                          self.edcat.iconbitmap("aa.ico")


                          self.fc=Frame(self.edcat,bg='#0f624c',width=300,height=30)
                          self.fc.place(x=0,y=0)
                          self.lab=Label(self.fc,bg='#0f624c',fg='#fff',text='EDIT DETAILS',font=('arial',10,'bold'))
                          self.lab.place(x=112,y=5)
                          self.labid = Label(self.edcat, bg='#fff', fg='black', text='Patient-ID', font=('arial', 10,
                                                                                                    'bold'))
                          self.labid.place(x=10, y=45)
                          self.labti = Label(self.edcat, bg='#fff', fg='black', text='Patient-Name', font=('arial', 10,
                                                                                                    'bold'))
                          self.labti.place(x=10, y=90)
                          self.labaut = Label(self.edcat, bg='#fff', fg='black', text='Blood-group', font=('arial', 10,
                                                                                                    'bold'))
                          self.labaut.place(x=10, y=135)
                          self.labed = Label(self.edcat, bg='#fff', fg='black', text='Donate blood', font=('arial', 10,
                                                                                                    'bold'))
                          self.labed.place(x=10, y=180)
                          self.labpr = Label(self.edcat, bg='#fff', fg='black', text='Disease', font=('arial', 10,
                                                                                                    'bold'))
                          self.labpr.place(x=10, y=225)

                        


                          self.en1=Entry(self.edcat,width=25,bd=4,relief='groove',font=('arial',8,'bold'))
                          self.en1.place(x=100,y=45)
                          self.en2 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en2.place(x=100, y=90)
                          self.en3 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en3.place(x=100, y=135)
                          self.en4 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en4.place(x=100, y=180)
                          self.en5 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en5.place(x=100, y=225)
                          self.butt = Button(self.edcat, text='Submit', bg='#0f624c', fg='#fff', width=20, height=0,
                                      font=('Arial', 10, 'bold'),command=self.savedit)
                          self.butt.place(x=67, y=270)

                         

                          self.en1.insert(0, self.val[0])
                          self.en2.insert(0, self.val[1])
                          self.en3.insert(0, self.val[2])
                          self.en4.insert(0, self.val[3])
                          self.en5.insert(0, self.val[4])

                          self.edcat.mainloop()

                     else:
                          messagebox.showerror('BLOOD BANK MANAGEMENT SYSTEM','PLEASE! ENTER THE CORRECT Patient-ID')

                


               def savedit(self):
                     self.id = self.en1.get()
                     self.ti = self.en2.get()
                     self.au = self.en3.get()
                     self.ed = self.en4.get()
                     self.pi = self.en5.get()
                     import mysql.connector
                     mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
                     cursor=mydb.cursor()
                     cursor.execute("UPDATE  details SET  SNO='"+self.id+"', patient_name='"+self.ti+"',blood_group='"+self.au+"',donate='"+self.ed+"',disease='"+self.pi+"' WHERE SNO='"+self.datas+"'")
                     mydb.commit()
                     messagebox.showinfo('BLOOD BANK MANAGEMENT SYSTEM','YOUR DATA IS UPDATED!')

         obj=editing()
         obj.edbooks()

         


         
     def email(self):
         class retu(maincode):

             def __init__(self):
                 self.frame=Frame(root,bd=0,relief='flat',bg='#a7ecd9',width=900,height=390)
                 self.frame.place(x=0,y=110)
                 self.f1 = Frame(self.frame, bg='#fff', width=500, height=370, bd=5, relief='flat')
                 self.f1.place(x=200, y=15)
                 self.ed = Frame(self.f1, bg='#0f624c', bd=0, relief='flat', width=490, height=35)
                 self.ed.place(x=0, y=0)
                 self.lac = Label(self.ed, text='BLOOD ENQUIRY ', bg='#0f624c', fg='#fff', font=('Arial', 12, 'bold'))
                 self.lac.place(x=175, y=5)
                 self.label8 = Label(self.f1, text='PATIENT-ID:', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label8.place(x=100, y=65)
                 self.entry4 = Entry(self.f1, width=30,bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entry4.place(x=188, y=65)
                 

                 self.label9 = Label(self.f1, text='NAME:', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label9.place(x=100, y=105)
                 self.entry5 = Entry(self.f1, width=30,bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entry5.place(x=188, y=105)

                 self.label10 = Label(self.f1, text='SUBJECT:', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label10.place(x=100, y=145)
                 self.entry6 = Entry(self.f1, width=30,bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entry6.place(x=188, y=145)

                 self.label11 = Label(self.f1, text='MESSAGE:', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label11.place(x=100, y=185)

                 self.entry7 = Text(self.f1, width=30,height=5,bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entry7.place(x=188, y=185)
                 self.button9 = Button(self.f1, text='SUBMIT', bg='#0f624c', fg='#fff', width=24, height=0,
                                       font=('Arial', 10, 'bold'),command=self.mail)
                 self.button9.place(x=140, y=290)



                 self.backbt = Button(self.frame, width=60, bg='#a7ecd9', activebackground='#a7ecd9',
                                      bd=0, relief='flat', command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(1, 1)
                 self.backbt.config(image=self.small_log)



                 self.mike1 = Button(self.f1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.entry4.insert(END, self.takeCommand()))
                 self.mike1.place(x=380, y=65)
                 self.log = PhotoImage(file='mike.png')
                 self.mike1.config(image=self.log, compound=LEFT)
                 self.small_log1 = self.log.subsample(1, 1)
                 self.mike1.config(image=self.small_log1)



                 self.mike2 = Button(self.f1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.entry5.insert(END, self.takeCommand()))
                 self.mike2.place(x=380, y=105)
                 self.log = PhotoImage(file='mike.png')
                 self.mike2.config(image=self.log, compound=LEFT)
                 self.small_log2 = self.log.subsample(1, 1)
                 self.mike2.config(image=self.small_log1)

                 self.mike3 = Button(self.f1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.entry6.insert(END, self.takeCommand()))
                 self.mike3.place(x=380, y=145)
                 self.log = PhotoImage(file='mike.png')
                 self.mike3.config(image=self.log, compound=LEFT)
                 self.small_log3 = self.log.subsample(1, 1)
                 self.mike3.config(image=self.small_log1)


                 self.mike4 = Button(self.f1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.entry7.insert(END, self.takeCommand()))
                 self.mike4.place(x=380, y=185)
                 self.log = PhotoImage(file='mike.png')
                 self.mike4.config(image=self.log, compound=LEFT)
                 self.small_log4 = self.log.subsample(1, 1)
                 self.mike4.config(image=self.small_log4)





             def takeCommand(self):
                  import speech_recognition as sr
                  r = sr.Recognizer()
                  mic = sr.Microphone(device_index=1)
                  with mic as source:
                      r.adjust_for_ambient_noise(source, duration=1)
                      audio = r.listen(source, timeout=5)
                  try:
                      SQ1 = r.recognize_google(audio, language='English')
                  except:
                       messagebox.showerror('Blood bank management system', 'Sorry! Not able to uderstand')
                       pass
                  return SQ1




             def mail(self):

                 self.id=self.entry4.get()
                 self.ttl=self.entry5.get()
                 self.aut=self.entry6.get()
                 self.edi=self.entry7.get("1.0",END)
                 
                 import mysql.connector
                 mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
                 cursor=mydb.cursor()
                 s="INSERT INTO inquiry (p_id,p_name,subject,message) VALUES(%s,%s,%s,%s)"
                 b1=(self.id,self.ttl,self.aut,self.edi)
                 cursor.execute(s,b1)
                 mydb.commit()
                 self.clear()

             def clear(self):
                 self.entry4.delete(0,END)
                 self.entry5.delete(0,END)
                 self.entry6.delete(0,END)
                 self.entry7.delete("1.0",END)


         object=retu()

     


    

     def delete(self):
         class dele(maincode):
               def deleteee(self):
                     self.ff = Frame(root, bg='#a7ecd9', width=900, height=390)
                     self.ff.place(x=0, y=110)
                     self.f1 = Frame(self.ff, bg='#fff', width=500, height=200, bd=5, relief='flat')
                     self.f1.place(x=200, y=15)
                     self.ed = Frame(self.f1, bg='#0f624c', bd=0, relief='flat', width=490, height=35)
                     self.ed.place(x=0, y=0)
                     self.lac = Label(self.ed, text='DELETE PATIENT DETAILS ', bg='#0f624c', fg='#fff', font=('Arial', 12,'bold'))
                     self.lac.place(x=175, y=5)
                     self.label8 = Label(self.f1, text='Patient_ID', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                     self.label8.place(x=85, y=65)
                     self.entry14 = Entry(self.f1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                     self.entry14.place(x=188, y=65)
                     self.button9 = Button(self.f1, text='Delete', bg='#0f624c', fg='#fff', width=24, height=0,
                                  font=('Arial', 10, 'bold'),command=self.deldata)
                     self.button9.place(x=140, y=120)

                     self.backbt = Button(self.ff,width=60, bg='#a7ecd9',activebackground='#a7ecd9',
                                          bd=0, relief='flat', command=self.cur)
                     self.backbt.place(x=0, y=0)
                     self.log = PhotoImage(file='back.png')
                     self.backbt.config(image=self.log, compound=LEFT)
                     self.small_log = self.log.subsample(1, 1)
                     self.backbt.config(image=self.small_log)

                     self.mike4 = Button(self.f1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.entry14.insert(END, self.takeCommand()))
                     self.mike4.place(x=380, y=65)
                     self.log = PhotoImage(file='mike.png')
                     self.mike4.config(image=self.log, compound=LEFT)
                     self.small_log4 = self.log.subsample(1, 1)
                     self.mike4.config(image=self.small_log4)
               def takeCommand(self):
                   import speech_recognition as sr
                   r = sr.Recognizer()
                   mic = sr.Microphone(device_index=1)
                   with mic as source:
                        r.adjust_for_ambient_noise(source, duration=1)
                        audio = r.listen(source, timeout=5)
                   try:
                       SQ1 = r.recognize_google(audio, language='English')
                   except:
                       messagebox.showerror('Blood bank management system', 'Sorry! Not able to uderstand')
                       pass
                   return SQ1


               def deldata(self):
                     self.a=self.entry14.get()
                     import mysql.connector
                     mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
                     cursor=mydb.cursor()
                     cursor.execute("select * from details WHERE SNO='"+self.a+"'")
                     self.da=cursor.fetchone()
                     if self.da!=None:
                         cursor.execute("DELETE FROM details WHERE SNO='"+self.a+"'")
                         mydb.commit()
                         messagebox.showinfo('Library System','YOUR DATA IS DELETED !')
                     else:
                          messagebox.showerror('Library System','YOUR DATA IS NOT FOUND !')

         occ=dele()
         occ.deleteee()

    


    

     def search(self):
         class demt(maincode):
             def delmdata(self):

                 self.fc = Frame(root, bg='#a7ecd9', width=900, height=390)
                 self.fc.place(x=0, y=110)
                 self.fc1 = Frame(self.fc, bg='#fff', width=500, height=200, bd=5, relief='flat')
                 self.fc1.place(x=200, y=15)
                 self.edm = Frame(self.fc1, bg='#0f624c', bd=0, relief='flat', width=490, height=35)
                 self.edm.place(x=0, y=0)
                 self.lac = Label(self.edm, text='SEARCH DOCTOR ', bg='#0f624c', fg='#fff', font=('Arial', 12, 'bold'))
                 self.lac.place(x=175, y=5)
                 self.label8 = Label(self.fc1, text='Doctor Name', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label8.place(x=85, y=65)
                 self.entryl= Entry(self.fc1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entryl.place(x=188, y=65)
                 self.butto = Button(self.fc1, text='Search', bg='#0f624c', fg='#fff', width=24, height=0,
                                       font=('Arial', 10, 'bold'),command=self.srch)
                 self.butto.place(x=140, y=120)

                 self.backbt = Button(self.fc,width=60, bg='#a7ecd9',activebackground='#a7ecd9',bd=0, relief='flat', command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(1, 1)
                 self.backbt.config(image=self.small_log)

                 self.mike4 = Button(self.fc1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.entryl.insert(END, self.takeCommand()))
                 self.mike4.place(x=380, y=65)
                 self.log = PhotoImage(file='mike.png')
                 self.mike4.config(image=self.log, compound=LEFT)
                 self.small_log4 = self.log.subsample(1, 1)
                 self.mike4.config(image=self.small_log4)
             def takeCommand(self):
                 import speech_recognition as sr
                 r = sr.Recognizer()
                 mic = sr.Microphone(device_index=1)
                 with mic as source:
                     r.adjust_for_ambient_noise(source, duration=1)
                     audio = r.listen(source, timeout=5)
                 try:
                     SQ1 = r.recognize_google(audio, language='English')
                 except:
                     messagebox.showerror('Blood bank management system', 'Sorry! Not able to uderstand')
                     pass
                 return SQ1


             def srch(self):
                 self.emp=self.entryl.get()
                 import mysql.connector
                 mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
                 cursor=mydb.cursor()
                 cursor.execute("SELECT * from doctor  WHERE D_name='"+self.emp+"'")
                 self.srval=cursor.fetchone()
                 if self.srval!=None:

                     self.top=Tk()
                     self.top.title("BLOOD BANK MANGEMENT SYSTEM")
                     self.top.iconbitmap("aa.ico")
                     self.top.geometry("600x600+600+300")
                     self.top.resizable(0, 0)
                     self.top.configure(bg='black')

                     self.frm=Frame(self.top,bg='#0f624c',width=300,height=35)
                     self.frm.place(x=0,y=0)

                     self.mnlb=Label(self.frm,bg='#0f624c',fg='#fff',text="Avaliable",font=('arial',11,'bold'))
                     self.mnlb.place(x=120,y=5)

                     self.lb1 = Label(self.top, text='Doctor-ID', bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb1.place(x=40,y=80)
                     self.lb2=Label(self.top,text=self.srval[0],bg='black',fg='blue',font=('arial',12,'bold'))
                     self.lb2.place(x=150,y=80)

                     self.lb3 = Label(self.top, text='Doctor-Name', bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb3.place(x=40, y=160)
                     self.lb4 = Label(self.top, text=self.srval[1], bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb4.place(x=150, y=160)

                     self.lb5 = Label(self.top, text='Doctor-Cabin', bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb5.place(x=40, y=240)
                     self.lb6 = Label(self.top, text=self.srval[2], bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb6.place(x=150, y=240)

                     self.lb7 = Label(self.top, text='Department', bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb7.place(x=40, y=320)
                     self.lb8 = Label(self.top, text=self.srval[3], bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb8.place(x=150, y=320)

                     self.lb9 = Label(self.top, text='Contact', bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb9.place(x=40, y=400)
                     self.lb10 = Label(self.top, text=self.srval[4], bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb10.place(x=150, y=400)

                     self.lb11 = Label(self.top, text='qualification', bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb11.place(x=40, y=480)
                     self.lb12 = Label(self.top, text=self.srval[5], bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb12.place(x=150, y=480)

                 else:
                     messagebox.showwarning('Library System','YOUR DATA IS NOT AVAILABLE !')

         object=demt()
         object.delmdata()

     


   

     def show(self):
         class tst(maincode):
             def __init__(self):
                 self.fc = Frame(root, bg='#a7ecd9', width=900, height=390)
                 self.fc.place(x=0, y=110)
                 self.popframe=Frame(self.fc,width=900,height=30,bg='#0f624c')
                 self.popframe.place(x=0,y=0)
                 self.lbn=Label(self.popframe,bg='#0f624c',text='Blood Available',fg='#fff',font=('arial',10,
                                                                                                      'bold'))
                 self.lbn.place(x=380,y=5)

                 self.backbt = Button(self.popframe,width=30, bg='#0f624c',activebackground='#0f624c',
                                      bd=0, relief='flat', command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(2, 2)
                 self.backbt.config(image=self.small_log)


                 self.table_frame=Frame(self.fc,bg='#fff',bd=1,relief='flat')
                 self.table_frame.place(x=0,y=30,width=900,height=360)

                 self.scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
                 self.scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
                 self.book_table=ttk.Treeview(self.table_frame,columns=("P_ID","P_name","Address","Email",
                                                                           "contact","Blood grp"),
                                      xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                 self.scroll_x.pack(side=BOTTOM,fill=X)
                 self.scroll_y.pack(side=RIGHT, fill=Y)
                 self.scroll_x.config(command=self.book_table.xview)
                 self.scroll_y.config(command=self.book_table.yview)

                 self.book_table.heading("P_ID",text="P_ID")
                 self.book_table.heading("P_name", text="P_name")
                 self.book_table.heading("Address", text="Address")
                 self.book_table.heading("Email", text="Email")
                 self.book_table.heading("contact", text="contact")
                 self.book_table.heading("Blood grp", text="Blood grp")
                 self.book_table['show']='headings'
                 self.book_table.column("P_ID",width=10)
                 self.book_table.column("P_name", width=10)
                 self.book_table.column("Address", width=10)
                 self.book_table.column("Email", width=10)
                 self.book_table.column("contact", width=10)
                 self.book_table.column("Blood grp", width=10)
                 self.book_table.pack(fill=BOTH,expand=1)
                 self.fetch_data()

             def fetch_data(self):
                 import mysql.connector
                 mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
                 cursor=mydb.cursor()
                 cursor.execute("SELECT * FROM doctor")
                 self.rows=cursor.fetchall()
                 if len(self.rows)!=0:
                      for self.row in self.rows:
                           self.book_table.insert('',END,values=self.row)
                 mydb.commit()


         oc=tst()

     

     def code(self):

         self.fm=Frame(root,height=500,width=900,bg='white')
         self.fm.place(x=0,y=0)

         self.canvas=Canvas(self.fm,height=500,width=900,bg='#22224b')
         self.canvas.place(x=0,y=0)

         self.photo=PhotoImage(file="images (17).png")
         self.canvas.create_image(-148,-337,image=self.photo,anchor=NW)

         self.fm1=Frame(self.canvas,height=260,width=300,bg='white',bd=3,relief='ridge')
         self.fm1.place(x=300,y=200)

         self.b1=Label(self.fm1,text='Patient ID',bg='white',font=('Arial',10,'bold'))
         self.b1.place(x=20,y=42)

         self.e1=Entry(self.fm1,width=22,font=('arial',9,'bold'),bd=4,relief='groove')
         self.e1.place(x=100,y=40)

         self.lb2=Label(self.fm1,text='Password',bg='white',font=('Arial',10,'bold'))
         self.lb2.place(x=20,y=102)

         self.e2=Entry(self.fm1,width=22,show='*',font=('arial',9,'bold'),bd=4,relief='groove')
         self.e2.place(x=100,y=100)


         self.btn1=Button(self.fm1,text='  login',fg='white',bg='red',width=100,font=('Arial',11,'bold'),
                 activebackground='white',activeforeground='black',command=self.login,bd=3,relief='flat',cursor='hand2')
         self.btn1.place(x=25,y=160)
         self.logo = PhotoImage(file='user.png')
         self.btn1.config(image=self.logo, compound=LEFT)
         self.small_logo = self.logo.subsample(1, 1)
         self.btn1.config(image=self.small_logo)



         self.btn2=Button(self.fm1,text='Clear',fg='white',bg='blue',width=100,font=('Arial',11,'bold'),
                 activebackground='white',activeforeground='black',bd=3,relief='flat',cursor='hand2',
                          command=self.mainclear)
         self.btn2.place(x=155,y=160)
         self.log = PhotoImage(file='cart.png')
         self.btn2.config(image=self.log, compound=LEFT)
         self.small_log = self.log.subsample(1, 1)
         self.btn2.config(image=self.small_log)

         

         self.forgot=Label(self.fm1,text='Sign up',fg='red',bg='#fff',bd=3,activeforeground='black',
                           font=('cursive',9,'bold'))
         self.forgot.place(x=120,y=220)
         self.forgot.bind("<Button>",self.mouseClick)



         self.mike70 = Button(self.fm1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.e1.insert(END, self.takeCommand1()))
         self.mike70.place(x=255, y=38)
         self.log = PhotoImage(file='mike.png')
         self.mike70.config(image=self.log, compound=LEFT)
         self.small_log70 = self.log.subsample(1, 1)
         self.mike70.config(image=self.small_log70)

         self.mike25 = Button(self.fm1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.e2.insert(END,self.takeCommand1()))
         self.mike25.place(x=255, y=98)
         self.log = PhotoImage(file='mike.png')
         self.mike25.config(image=self.log, compound=LEFT)
         self.small_log25 = self.log.subsample(1, 1)
         self.mike25.config(image=self.small_log25)
         
         root.mainloop()

     def mouseClick(self,event):
         self.rog=Tk()
         self.rog.title("Sign up")
         self.rog.geometry("400x300+530+280")
         self.rog.iconbitmap("aa.ico")
         self.rog.resizable(0,0)
         self.rog.configure(bg='#fff')

         self.label=Label(self.rog,text="Add your deatils",bg='#fff',fg='red',font=("cursive",20,'bold'))
         self.label.place(x=105,y=15)

         self.user=Label(self.rog,text='Patient ID :',bg='#fff',fg='black',font=("cursive",10,'bold'))
         self.user.place(x=40,y=95)

         self.user=Label(self.rog,text='Patient Name :',bg='#fff',fg='black',font=("cursive",10,'bold'))
         self.user.place(x=40,y=135)

         self.user = Label(self.rog, text='password :', bg='#fff', fg='black', font=("cursive", 10, 'bold'))
         self.user.place(x=40, y=180)


         self.e1 = Entry(self.rog, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
         self.e1.place(x=170, y=95)

         self.e2 = Entry(self.rog, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
         self.e2.place(x=170, y=135)

         self.e3 = Entry(self.rog, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
         self.e3.place(x=170, y=175)

         self.btn1 = Button(self.rog, text='Submit', fg='white', bg='#5500ff', width=20, font=('Arial', 13, 'bold'),
                            activebackground='white', activeforeground='black',bd=3, relief='flat',
                            cursor='hand2',command=self.sign_up)
         self.btn1.place(x=100, y=240)


     def sign_up(self):
         self.a=self.e1.get()
         self.b=self.e2.get()
         self.c=self.e3.get()
         mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='hospital')
         cursor=mydb.cursor()
         cursor.execute("SELECT Patient_ID FROM patient WHERE Patient_ID='"+self.a+"'" ) 
         self.data=cursor.fetchone()
         if self.data==None:
             s="INSERT INTO patient (Patient_ID,Patient_name,Password) VALUES(%s,%s,%s)"
             b1=(self.a,self.b,self.c)
             cursor.execute(s,b1)
             mydb.commit()
             messagebox.showinfo("Blood management system","You are successfully registered !")
         else:
             messagebox.showinfo("Blood management system","You are Already registered !")
             
         self.rog.mainloop()
wishMe()
ob=maincode()
ob.code()
