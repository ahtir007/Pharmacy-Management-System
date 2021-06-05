from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import sqlite3
import datetime
import tkinter.ttk as ttk
import pyttsx3
import datetime
import time as tm

import sqlite3
import pandas as pd
from fuzzywuzzy import process



''' NEW'''
conn = sqlite3.connect('medicine.sqlite')
cur = conn.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS Medicines (
     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Name TEXT,
    Salt TEXT ,
    Company,
    Quantity INTEGER,
    Weight INTEGER,
    uses TEXT

);
CREATE TABLE IF NOT EXISTS Uses (
     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
     NameTEXT UNIQUE,
     Uses TEXT UNIQUE
);
''')

class Parent:
    def __init__(self,master):
        self.master=master
        self.master.title("Softex Solutions")
        self.master.geometry("1350x750+0+0")#("1000x700")
        p1=PhotoImage(file='logo.png')
        master.iconphoto(False,p1)



        self.mainframe=Frame(self.master)
        self.mainframe.pack()
    

class Login(Parent):
    def __init__(self,master):
        super().__init__(master)
        engine = pyttsx3.init()
        engine.say('Good morning Welcome to Hassan Shakoor Pharmacy Management System')
       engine.runAndWait()

        
        self.Username=StringVar()
        self.Password=StringVar()
        self.Heading=Label(self.mainframe,font=("arial",40,"bold"),text="Softex Pharmacy Login System")
        self.Heading.grid(row=0,column=0,columnspan=2,pady=25)

        self.lgnFrame=LabelFrame(self.mainframe, width=1000, height=500, relief='ridge', bd=20)
        self.lgnFrame.grid(row=1,column=0)
        
        self.lgnFrame2=LabelFrame(self.mainframe, width=1000, height=500, relief='ridge', bd=20)
        self.lgnFrame2.grid(row=2,column=0)

        self.btnLogin=Button(self.lgnFrame2,text="Login",font=("arial",15,"bold"),width=17,bd=4,command=self.login)
        self.btnLogin.grid(row=2,column=0,pady=20,padx=8)
        self.btnReset=Button(self.lgnFrame2,text="Reset",font=("arial",15,"bold"),width=17,bd=4,command=self.reset)
        self.btnReset.grid(row=2,column=1,pady=20,padx=8)
        self.btnExit=Button(self.lgnFrame2,text="Exit",font=("arial",15,"bold"),width=17,bd=4,command=self.Exit)
        self.btnExit.grid(row=2,column=3,pady=20,padx=8)
        self.btnForgot=Button(self.lgnFrame2,text="Forgot Password",font=("arial",15,"bold"),width=17,bd=4,command=self.forgot_password)
        self.btnForgot.grid(row=2,column=2,pady=20,padx=8)
       
#_____________________________________________________________________________________________
        #Entries in login page
        self.userName=Label(self.lgnFrame,text= "Username" ,font=('arial',20,'bold'),bd=22)
        self.userName.grid(row=0,column=0)
        self.txtuserName=Entry(self.lgnFrame,font=('arial',20,'bold'),textvariable=self.Username)
        self.txtuserName.focus_set()
        self.txtuserName.bind("<Return>",self.nextEntry)
        self.txtuserName.grid(row=0,column=1)
        self.logoFrame=Frame(self.master,bd=10,width=400, height=270,padx=10,relief=RIDGE)
        self.logoFrame.pack(side=BOTTOM)
        my_canvas=Canvas(self.logoFrame, width=400, height=270, bg="white")
        my_canvas.pack(expand=YES, fill=BOTH)
        gif1 = PhotoImage(file='newlogo.png')
        image=my_canvas.create_image(0,0, anchor=NW, image=gif1)

       

        self.password=Label(self.lgnFrame,text= "Password" ,font=('arial',20,'bold'),bd=22)
        self.password.grid(row=1,column=0)
        self.txtpassword=Entry(self.lgnFrame,font=('arial',20,'bold'),show='*',textvariable=self.Password)
        self.txtpassword.bind("<Return>",self.login)
        self.txtpassword.grid(row=1,column=1)

        mainloop()
        

    def nextEntry(self, *args):
        self.txtpassword.focus_set()
        
    def login(self, *args):
        u=(self.Username.get())
        p=self.Password.get()
        if (u==str("softex") and p==str("softex")):
            self.newWindow=Toplevel(self.master)
            self.app=Window1(self.newWindow)
        else:
            self.Username.set('')
            self.Password.set('')
            tkinter.messagebox.showerror(title="Softex Solutions", message="Login Systems, Username or password is wrong")
            self.txtuserName.focus()
    def reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtuserName.focus()
    def forgot_password(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window5(self.newWindow)

    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("Manufacturing System System","confirm if you want to exit")
        if self.Exit>0:
            self.master.destroy()
            return
    def new_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window1(self.newWindow)



        

class Window1(Parent):
    def __init__(self,master):
        super().__init__(master)
        
        self.titleframe=Frame(self.mainframe,width=1350, padx=20, bd=20, relief=RIDGE)
        self.titleframe.pack()

        self.title1=Label(self.titleframe,font=("arial",40,"bold"),text="Softex Pharmacy System")
        self.title1.grid(row=0,column=0,columnspan=2,pady=20)


  
        #image_label=Label(image=p2)
        

        self.dataframe=Frame(self.mainframe,bd=20,width=1300, height=550,padx=20,relief=RIDGE)
        self.dataframe.pack()

        #___________________________________________________________________________________________________________

        '''SELCTING PHOTOS'''

        employeeImg=PhotoImage(file='employee.png')
        reportImg=PhotoImage(file='report2.png')
        selling_mode=PhotoImage(file='sales2.png')
        debt=PhotoImage(file="debt.png")
        stock=PhotoImage(file="stocknew.png")
        customer=PhotoImage(file="rsz_customer.png")

        #____________________________________________________________________________________________________________


        self.sales=Button(self.dataframe,image=selling_mode,command=self.sales,bg="blue").place(x=40,y=30)#(x=660,y=30)
        self.salesLabel=Label(self.dataframe, text="Sales",font=("arial",15,"bold"))
        self.salesLabel.place(x=110,y=200)


        self.employee=Button(self.dataframe,image=employeeImg,bg="blue").place(x=470,y=30)
        self.employeeLabel=Label(self.dataframe, text="Employee",font=("arial",15,"bold"))
        self.employeeLabel.place(x=550,y=200)
        

        


        self.report=Button(self.dataframe,image=reportImg,command=self.add_company,bg="lightblue").place(x=900,y=30)#(x=350,y=30)
        self.reportLabel=Label(self.dataframe, text="Reports",font=("arial",15,"bold"))
        self.reportLabel.place(x=970,y=200)#(x=370,y=200)

        self.debt=Button(self.dataframe,image=debt,command=self.manage_staff,bg="blue").place(x=40,y=300)
        self.debtLabel=Label(self.dataframe, text="Debts",font=("arial",15,"bold"))
        self.debtLabel.place(x=110,y=480)


        self.stock=Button(self.dataframe,image=stock,command=self.manage_stock,bg="blue").place(x=460,y=300)#(x=350,y=300)
        self.labelStock=Label(self.dataframe, text="Stock",font=("arial",15,"bold"))
        self.labelStock.place(x=550,y=480)#(x=370,y=480)


        self.customer=Button(self.dataframe,image=customer,command=self.customer_history,bg="lightblue").place(x=900,y=280)#(x=660,y=300)
        self.labelCustomer=Label(self.dataframe, text="Customer History",font=("arial",15,"bold")).place(x=920,y=480)#(x=680,y=480)

        mainloop()

    def stock(self):
        self.newWindow=Toplevel(self.master)
        self.app=Stock_Management(self.newWindow)
        
    def add_company(self):
        self.newWindow=Toplevel(self.master)
        self.app=Add_Company(self.newWindow)

    def sales(self):
        self.newWindow=Toplevel(self.master)
        self.app=Sales(self.newWindow)


    def manage_staff(self):
        self.newWindow=Toplevel(self.master)
        self.app=Manage_Staff(self.newWindow)


    def manage_stock(self):
        self.newWindow=Toplevel(self.master)
        self.app=Manage_Stock(self.newWindow)


    def customer_history(self):
        self.newWindow=Toplevel(self.master)
        self.app=Customer_History(self.newWindow)

#Adding medicine to stock
class Stock_Management(Parent):
    def __init__(self,master):
        super().__init__(master)

class Add_Company(Parent):
    def __init__(self,master):
        super().__init__(master)


#SELLING MODE CLASS
class Sales(Parent):
    def __init__(self,master):
        super().__init__(master)

      

        self.medicine=StringVar()
        self.Quantity=DoubleVar()
        self.customername=StringVar()
        self.Date=StringVar()
        self.Time=StringVar()
        self.search=StringVar()
        self.Amount=DoubleVar()
        self.rateper=""
        self.med=""
        self.tempamount=0
        self.tempquantity=0




        self.titleframe=Frame(self.mainframe,width=1350, padx=20, bd=20, relief=RIDGE)
        self.titleframe.pack()


        self.title1=Label(self.titleframe,font=("arial",40,"bold"),text="Softex Pharmacy System")
        self.title1.grid(row=0,column=0,columnspan=2,pady=20)
        #DATA FRAME


        self.dataframe1=Frame(self.mainframe,bd=10,width=250, height=110,padx=10,relief=RIDGE)
        self.dataframe1.pack()




        #INSIDE DATAFRAME 1 BOX
        # SEARCH ENTRY
        self.searchLabel=Label(self.dataframe1,font=("arial",15,"bold"),text="Search:",padx=10,pady=10)
        self.searchLabel.grid(row=0,column=2)
        self.Search=Entry(self.dataframe1,font=("arial",15,"bold"),width=20,textvariable=self.search)
        self.Search.bind("<Return>",self.entries)
        
        self.Search.grid(row=0,column=3)

        self.OK=Button(self.dataframe1,text="Ok",font=("arial",10,"bold"),width=10,bd=4,bg="pink",command=self.ok_button,padx=10,pady=10)
        self.OK.grid(row=0,column=4)


        self.back=Button(self.mainframe,text="Back",font=("arial",10,"bold"),height=2,width=15,bd=3,bg="green",command=self.Back)
        self.back.place(x=5,y=5)




        self.dataframe=Frame(self.mainframe,bd=20,width=1300, height=550,padx=20,relief=RIDGE)
        self.dataframe.pack()

        # LEFT FRAME

        self.dataframeLeft=LabelFrame(self.dataframe,bd=10,width=400, height=400,padx=20,relief=RIDGE,font=("arial",12,"bold"))
        self.dataframeLeft.pack(side=LEFT)

        # RIGHT FRAME

        self.dataframeright=LabelFrame(self.dataframe,bd=10,width=450, height=300,padx=20,relief=RIDGE,font=("arial",12,"bold"),text="Categories:  ")
        self.dataframeright.pack(side=RIGHT)



        self.dataframeRight=Listbox(self.dataframeright,width=200,height=150,font=("arial",12,"bold"))

        self.dataframeRight.bind("<<ListboxSelect>>",self.Select)
        self.dataframeRight.grid(row=0,column=0,padx=8)

        #INSIDE LEFT BOX
        # MEDICINE ENTRY


        self.medicineLabel=Label(self.dataframeLeft,font=("arial",15,"bold"),text="Medicine: ",padx=10,pady=10)
        self.medicineLabel.grid(row=0,column=0,sticky=W)

        self.Medicine=Entry(self.dataframeLeft,font=("arial",15,"bold"),width=15,textvariable=self.medicine)
        self.Medicine.focus_set()

        self.Medicine.bind("<Return>",self.next1)
        #self.medicine.bind("<Return>",self.nextEntry2)
        self.Medicine.grid(row=0,column=1)

        self.AddButton=Button(self.dataframeLeft,text="Add",font=("arial",10,"bold"),height=2,width=10,bd=4,bg="yellow").grid(row=0,column=2)


        

        #QUANTITY ENTRY
        self.quantityLabel=Label(self.dataframeLeft,font=("arial",15,"bold"),text="Quantity: ",padx=10,pady=10)
        self.quantityLabel.grid(row=1,column=0,sticky=W)

        self.quantity=Entry(self.dataframeLeft,font=("arial",15,"bold"),width=15,textvariable=self.Quantity)
        self.quantity.focus_set()
        self.quantity.bind("<Return>",self.next2)
        self.quantity.grid(row=1,column=1)

        #CUSTOMER NAME ENTRY
        self.nameLabel=Label(self.dataframeLeft,font=("arial",15,"bold"),text="Name: ",padx=10,pady=10)
        self.nameLabel.grid(row=2,column=0,sticky=W)

        self.name=Entry(self.dataframeLeft,font=("arial",15,"bold"),width=15,textvariable=self.customername)
        self.name.focus_set()
        self.name.bind("<Return>",self.next3)
        self.name.grid(row=2,column=1)

        #DATE ENTRY

        self.dateLabel=Label(self.dataframeLeft,font=("arial",15,"bold"),text="Date: ",padx=10,pady=10)
        self.dateLabel.grid(row=3,column=0,sticky=W)

        self.date=Entry(self.dataframeLeft,font=("arial",15,"bold"),width=15,textvariable=self.Date)
        self.date.grid(row=3,column=1)
        self.date.bind("<Return>",self.next4)
        now = datetime.date.today()
        now=str(now)
        self.date.insert(0,now)

        #TIME

        self.timeLabel=Label(self.dataframeLeft,font=("arial",15,"bold"),text="Time: ",padx=10,pady=10)
        self.timeLabel.grid(row=4,column=0,sticky=W)

        self.time=Entry(self.dataframeLeft,font=("arial",15,"bold"),width=15,textvariable=self.Time)
        self.time.grid(row=4,column=1)
        now = tm.strftime('%H:%M')
        now=str(now)
        self.time.insert(0,now)

        
        self.amountLabel=Label(self.dataframeLeft,font=("arial",15,"bold"),text="Amount: ",padx=10,pady=10)
        self.amountLabel.grid(row=5,column=0,sticky=W)

        self.amount=Entry(self.dataframeLeft,font=("arial",15,"bold"),width=15,textvariable=self.Amount)
        self.amount.grid(row=5,column=1)

        # BILL BUTTON
        self.bill=Button(self.mainframe,text="Bill",font=("arial",12,"bold"),height=3,width=25,bd=4,bg="pink",command=self.generate_bill).place(x=70,y=620)
       
        '''NEW'''

        cur.execute('SELECT * FROM Medicines')
        self.row=cur.fetchall()
        self.list1=[]
        for i in self.row:
            self.list1.append(i[1])

    def entries(self,*args):
        self.Medicine.focus_set()

    def Back(self):
        self.master.destroy()#esc binding
        
    def next1(self,*args):
        self.quantity.focus_set()
    def next2(self,*args):

        cur.execute("SELECT Name, Rateper FROM Medicines")
        row2=cur.fetchall()
        self.med=self.Medicine.get()
        # Finding the rate of medicine and then calculate the amount by multiplying the rate per tabet and 
        for i in row2:  
            if (str(self.med==i[0])):
                self.rateper=(i[1])

                break
            else:
                print("no")
        
        if self.quantity!=0:

            self.tempquantity=Entry.get(self.quantity)
            self.tempamount=float(self.tempquantity)*self.rateper
        self.med=self.Medicine.get()
        #self.Amount.set(self.tempamount)  
        self.Amount.set("")  
        self.amount.insert(END,self.tempamount)

        self.name.focus_set()

    def next3(self,*args):
        self.date.focus_set()

    
        
    def Select(self,evt):
        self.Medicine.delete(0,END)
        a=""
        x=self.dataframeRight.get(self.dataframeRight.curselection())
   
    
        if len(x)!=0:
            i=0
            while i < len(x):
                if x[i]==" ":
                    i=i+1
                    pass
                
                else:
                    while (i!=len(x) and x[i]!=" "):
                        a=str(a)+str(x[i])
                        i=i+1
                    if i!=len(x):
                        a=str(a)+","
            a.split(",")
            (list(a))
            self.array=[]
            b=" "
            for i in a:
                if i!=",":
                    b=b+i
                elif i==",":
                    if b not in self.array:
                        self.array.append(b)
                        b=" "
                    b=" "
            if len(self.array)!=0:
                self.Medicine.insert(END,self.array[1])# Problem
            else:
                pass

 
        
        
    def next4(self,*args):
        self.time.focus_set()

   
    def generate_bill(self):
        self.medicine.set("")
        self.customername.set("")
        self.Amount.set("")
        self.Quantity.set("")


        date=Entry.get(self.date)
        time=Entry.get(self.time)
        name=Entry.get(self.name)
              
       

        self.dataframeRight.delete(0,END)
        
        string3=str(date)+"                     "+str(time)+str("                      Cashier Name:  Ahtir")

        self.dataframeRight.insert(END,string3)
        
        self.dataframeRight.insert(END,'\n\n')
        
        self.dataframeRight.insert(END,"Customer Name:  "+str(name))
        self.dataframeRight.insert(END,'\n\n')

        string4=str("Sr no  ")+str("    Description     ")+str("             Rate")+str("                   Quantity")+str("             Total")
        self.dataframeRight.insert(END,string4)
        self.dataframeRight.insert(END,'\n\n')
        n=1
        string=str(n)+"               "+str(self.med)+"                           "+str(self.rateper)+"                    "+str(self.tempquantity)+"                        "+str(self.tempamount)
        self.dataframeRight.insert(END,string)

                            #Resetting                   

        '''NEW'''

        
    def ok_button(self):
        self.dataframeRight.delete(0,END)
        
        medicine=Entry.get(self.Search)
        if len(medicine)!=0:
            
            result=process.extract(medicine,self.list1,limit=2)
            self.list=[]
            for i in result:
                a=i[0]
                self.list.append(a)
            string="Serial no         "+str("Medicine            ")+str("Salt                 ")+str("Quantity                ")+str("Weight")
            self.dataframeRight.insert(END,string)
            self.dataframeRight.insert(END,'\n\n')
            
            n=1
            for i in self.list:
                for x in self.row:
                    if i in x:
                        string="\n\n"
                        string1=str(n)+"                     "+str(x[1])+"               "+str(x[2])+"           "+str(x[4])+"                 "+str(x[5])
                        self.dataframeRight.insert(END,string)
                        self.dataframeRight.insert(END,str(string1))

                        n=n+1
                
                    else:
                        pass

            
           
            ''''ADJUST IN BILL WALE ME LATER'''


class Generate_Bill(Parent):
    def __init__(self,master):
        super().__init__(master)



class Manage_Staff(Parent):
    def __init__(self,master):
        super().__init__(master)


class Manage_Stock(Parent):
    def __init__(self,master):
        super().__init__(master)        

class Customer_History(Parent):
    def __init__(self,master):
        super().__init__(master)

      


if __name__=="__main__":
    root=Tk()
    app=Window1(root)
    ttk.Style().theme_use('default')

