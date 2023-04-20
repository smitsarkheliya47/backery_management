from tkinter import *
from tkinter import messagebox
import mysql.connector
import smtplib, ssl
import tkinter as tk
import pandas as pd
import qrcode
from PIL import ImageTk,Image
import pandas as pd
from pyqrcode import create
import pyqrcode

root=Tk()
root.geometry("700x450")
root.title("BACKERY MANAGEMENT SYSTEM")

def insert():
    a=s1.get()
    b=s2.get()
    c=s3.get()
    d=s4.get()
    e=s5.get()

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="backery_billing_system"
        )

    mycursor = mydb.cursor()
    sql = "insert into details(cus_id,price,stocks,expiry_date,selling_record) values (%s,%s,%s,%s,%s)"
    val = (a, b, c, d, e)
    mycursor.execute(sql, val)                                                                                                                                                      
    mydb.commit()
    messagebox.showinfo("record...", "insert succesfully...!!!")


def update():

    root2=Tk()
    root2.geometry("700x350")

    def update1():

        a=s1.get()
        b=s2.get()
        c=s3.get()
        d=s4.get()
        e=s5.get()
        
        
        connection = mysql.connector.connect(host='localhost',
                                             database='backery_billing_system',
                                             user='root',
                                             password='')

        cur = connection.cursor()
        
        sql="UPDATE details SET price=%s,stocks=%s,expiry_date=%s,selling_record=%s  WHERE cus_id=%s"
        val=(b,c,d,e,a)
            
        cur.execute(sql,val)
        connection.commit()
        messagebox.showinfo("Record","Updated Successfully....!!")


    w1 = Label(root2, text="..≛≛.. UPDATE YOUR BILLING SYSTEM HERE ..≛≛..",
           font=("arial", 12, "bold"), bg="powder blue", fg="black")
    w1.grid(row=0,column=2)

    q1 = Label(root2, text="CUSTOMER_ID:➾", font=("arial", 12, "bold"))
    q1.grid(row=1, column=1)

    s1 = Entry(root2, font=("arial", 12, "bold"), bd=5, width=24)
    s1.grid(row=1, column=2)

    q2 = Label(root2, text="PRICE:➾", font=("arial", 12, "bold"))
    q2.grid(row=2, column=1)

    s2 = Entry(root2, font=("arial", 12, "bold"), bd=5, width=24)
    s2.grid(row=2, column=2)

    q3 = Label(root2, text="STOCKS:➾", font=("arial", 12, "bold"))
    q3.grid(row=3, column=1)

    s3 = Entry(root2, font=("arial", 12, "bold"), bd=5, width=24)
    s3.grid(row=3, column=2)

    q4 = Label(root2, text="EXPIRY_DATE:➾", font=("arial", 12, "bold"))
    q4.grid(row=4, column=1)

    s4 = Entry(root2, font=("arial", 12, "bold"), bd=5, width=24)
    s4.grid(row=4, column=2)

    q5 = Label(root2, text="SELLING_RECORD:➾", font=("arial", 12, "bold"))
    q5.grid(row=5, column=1)

    s5 = Entry(root2, font=("arial", 12, "bold"), bd=5, width=24)
    s5.grid(row=5, column=2)

    p4 = Button(root2, text="Update", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=update1)
    p4.grid(row=8, column=2)

    root2.mainloop()



def delete():

    root1=Tk()
    root1.geometry("500x400")

    def delete1():

        Id=e1.get()

        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="backery_billing_system"
            )
        mycursor=mydb.cursor()
        sql="DELETE FROM details WHERE cus_id=%s"
        val=(Id)
        mycursor.execute(sql,(val,))
        mydb.commit()
        messagebox.showinfo("Record","delete Successfully...!!")
        mydb.close()


    w1 = Label(root1, text="..≛≛.. ENTER CUS_ID AND DELETE HERE ..≛≛..",
           font=("arial", 12, "bold"), bg="powder blue", fg="black")
    w1.grid(row=0,column=2)

    l1=Label(root1,text="CUS_ID:➾",font=("arial",16,"bold"))
    l1.grid(row=1,column=1)

    e1=Entry(root1,width=20,bd=5)
    e1.grid(row=1,column=2)

    b1=Button(root1,text="Delete", bg="powder blue", fg="black",width=10,bd=5,font=("arial",16,"bold"),command=delete1)
    b1.grid(row=2,column=2)
    
    root1.mainloop()

def qrcodee():
    
    
    global my_image

    l1=Label(Frame1)
    l1.grid(row=10,column=2)
    
    a=s1.get()
    b=s2.get()
    c=s3.get()
    d=s4.get()
    e=s5.get()
    qrdata=pyqrcode.create(f"cus_id:{a}\n price:{b}\n stocks:{c}\n expiry_date:{d}\n selling_record:{e}")
    my1_qr=qrdata.xbm(scale=2)
    my_image=tk.BitmapImage(data=my1_qr)
    l1.config(image=my_image)

Frame1=Frame(root,height=250,width=350,bg="deep sky blue",bd=1,relief=FLAT)    
Frame1.grid(row=13,column=2)

ll1=Label(Frame1,text="Your QR Generate Here...!!",font=("arial,6,bold"),bg="lightblue",fg="black")
ll1.grid(row=11,column=2)


def csvf():
    mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="backery_billing_system"
            )
    mycursor=mydb.cursor()
    sql="select * FROM details "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    all_cus_id=[]
    all_price=[]
    all_stocks=[]
    all_expiry_date=[]
    all_selling_record=[]
    for cus_id,price,stock,expiry_date,selling_record in myresult:
        all_cus_id.append(cus_id)
        all_price.append(price)
        all_stocks.append(stock)
        all_expiry_date.append(expiry_date)
        all_selling_record.append(selling_record)
    

    dic={'cus_id':all_cus_id,'price':all_price,'stocks':all_stocks,'expiry_date':all_expiry_date, 'selling_record':all_selling_record}
    df=pd.DataFrame(dic)
    df_csv=df.to_csv('C:/A_python_db.csv',index=False)
        

    mydb.commit()
    messagebox.showinfo("Record","CSV FILE Generate Successfully...!!")
    mydb.close()

def email():
    sender_email = "sender@xyz.com"
    receiver_email = "receiver@xyz.com"
    message = """\
    Subject: It Worked!

    Simple Text email from your Python Script."""

    port = 465  
    app_password = input("Enter Password: ")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("sender@xyz.com", app_password)
        server.sendmail(sender_email, receiver_email, message)




s1=IntVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()

w1 = Label(root, text="..≛≛.. BACKERY MANAGEMENT SYSTEM ..≛≛..",
           font=("arial", 12, "bold"), bg="powder blue", fg="black")
w1.grid(row=0, column=2)

q1 = Label(root, text="CUSTOMER_ID:➾", font=("arial", 12, "bold"))
q1.grid(row=1, column=1)

s1 = Entry(root, font=("arial", 12, "bold"), bd=5, width=24)
s1.grid(row=1, column=2)

q2 = Label(root, text="PRICE:➾", font=("arial", 12, "bold"))
q2.grid(row=2, column=1)

s2 = Entry(root, font=("arial", 12, "bold"), bd=5, width=24)
s2.grid(row=2, column=2)

q3 = Label(root, text="STOCKS:➾", font=("arial", 12, "bold"))
q3.grid(row=3, column=1)

s3 = Entry(root, font=("arial", 12, "bold"), bd=5, width=24)
s3.grid(row=3, column=2)

q4 = Label(root, text="EXPIRY_DATE:➾", font=("arial", 12, "bold"))
q4.grid(row=4, column=1)

s4 = Entry(root, font=("arial", 12, "bold"), bd=5, width=24)
s4.grid(row=4, column=2)

q5 = Label(root, text="SELLING_RECORD:➾", font=("arial", 12, "bold"))
q5.grid(row=5, column=1)

s5 = Entry(root, font=("arial", 12, "bold"), bd=5, width=24)
s5.grid(row=5, column=2)

p1 = Button(root, text="Insert", font=("arial",12,"bold"), bd=5, width=5,
            bg="powder blue", fg="black", command=insert)
p1.grid(row=6,column=1)

p3 = Button(root, text="Delet", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=delete)
p3.grid(row=8, column=1)

p4 = Button(root, text="Update", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=update)
p4.grid(row=8, column=2)

p5 = Button(root, text="Csv", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=csvf)
p5.grid(row=9,column=1)

p6 = Button(root, text="Email", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=email)
p6.grid(row=9,column=2)

p8 = Button(root, text="QR code", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=10, command=qrcodee)
p8.grid(row=9,column=3)

root.mainloop()
