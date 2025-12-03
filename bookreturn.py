from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
from datetime import datetime



# Main window setup
win = Toplevel()
win.title("Library Management System")
win.geometry("1580x1380")
f1 = ("Arial", 15, 'bold')
f2 = ("Arial", 20, 'bold')

path = Image.open(r"C:\Users\panka\OneDrive\Documents\WhatsApp Image 2025-03-01 at 11.10.58_b55a3c0e.jpg")
render = ImageTk.PhotoImage(path)
img = Label(win, image=render)
img.image = render  # Keep a reference
img.place(x=1, y=1)


# Clear fields
def clfield():

    cal1.delete(0, END)
    ch.delete(0, END)
    ch1.delete(0, END)
    t5.delete(0, END)

def fetchrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    cursor = mydb.cursor()
    cursor.execute("select sno from studmast")
    data = cursor.fetchall()
    return data

def callback(event):
    s1 = ch.get()
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms"
    )
    cursor = mydb.cursor()
    cursor.execute("select * from studmast where sno=%s", (s1,))
    data = cursor.fetchone()
    if data:
        t8.delete(0, END)
        t8.insert(0, data[1])

def fetchrec1():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    cursor = mydb.cursor()
    cursor.execute("select bcode from bookmast")
    data1 = cursor.fetchall()
    return data1

def callback_book(event1):
    b1 = ch1.get()
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms"
    )
    cursor = mydb.cursor()
    cursor.execute("select * from bookmast where bcode=%s", (b1,))
    data = cursor.fetchone()
    if data:
        t9.delete(0, END)
        t9.insert(0, data[1])

def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    mycur = mydb.cursor()
    mycur.execute("select * from bookreturn")
    mydata = mycur.fetchall()
    mx = 0
    for i in mydata:
        mx=i[0]
    mx=mx+1
    t1.delete(0,END)
    t1.insert(0,mx)
    clfield()
# Save record
def saverec():
    s1 = t1.get()
    s2 = cal1.get()
    s3 = ch.get()
    s4 = ch1.get()
    s5 = t5.get()
    if s2.strip() == "":
        messagebox.showinfo('Warning...', 'please enter rtno')
        return
    if s3.strip() == "":
        messagebox.showinfo('Warning...', 'please enter sno')
        return
    if s4.strip() == "":
        messagebox.showinfo('Warning...', 'please enter bcode')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'please enter remark')
        return

    mydb = mysql.connector.connect (
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    mycur = mydb.cursor()
    mycur.execute("INSERT INTO bookreturn (rtno, rdate, sno, bcode, remark) VALUES (%s, %s, %s, %s, %s)", (s1, s2, s3, s4, s5))

    mydb.commit()
    messagebox.showinfo('confirm', "Record is save")
    maxrec()

# Search record
def serrec():
    s1 = t1.get()
    clfield()
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms"
    )
    mycur = mydb.cursor()
    mycur.execute("select * from bookreturn where rtno=%s", (s1,))
    mydata = mycur.fetchone()

    if mydata is not None:
        try:
            cal1.set_date(mydata[1])
        except ValueError:
            messagebox.showwarning('Warning', 'Invalid date format in database')
        ch.insert(0, mydata[2])
        ch1.insert(0, mydata[3])
        t5.insert(0, mydata[4])
    else:
        messagebox.showinfo('Confirm', 'Record Is Not Found')

    mycur.close()
    mydb.close()

def uprec():
    s1 = t1.get()
    s2 = cal1.get()
    s3 = ch.get()
    s4 = ch1.get()
    s5 = t5.get()
    if s2.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter rtno')
        return
    if s3.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter sno')
        return
    if s4.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter bcode')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter remark')
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms"
    )
    mycur = mydb.cursor()
    mycur.execute("UPDATE bookreturn SET  sno='"+s3+"', bcode='"+s3+"', remark='"+s5+"'WHERE rtno="+s1)
    mydb.commit()
    messagebox.showinfo('Confirm', "Record Is Updated")
    maxrec()


# Delete record
def delrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    mycur = mydb.cursor()
    ans = messagebox.askyesno('Confirm', 'Are you sure you want to delete?')
    if ans:
        s1 = t1.get()
        mycur.execute("DELETE FROM bookreturn WHERE rtno=" + s1)
        mydb.commit()
        messagebox.showinfo('Confirm', 'Record Is Deleted')
        maxrec()

l1 = Label(win, text=" Book Return ",width=15, font=f2, fg='black', bg='pink')
l1.place(x=600, y=100)

# Return No. Entry
l2 = Label(win, text="Return Is No. ",width=11, font=f1)
l2.place(x=530, y=200)
t1 = Entry(win, bd=2,width=20, font=f1)
t1.place(x=700, y=200)

# Return Date Entry
l3 = Label(win, text="Return Date",width=11, font=f1)
l3.place(x=530, y=270)
cal1 = DateEntry(win, selectmode="day",width=20, font=f1, date_pattern="yyyy-mm-dd")
cal1.place(x=700, y=270)


L7=Label(win,text="----------------",font=f1,width=15)
L7.place(x=-700,y=340)


l4 = Label(win, text="Student No.", width=11,font=f1)
l4.place(x=530, y=340)
data = fetchrec()
ch = Combobox(win, font=f1, width=20,values=data)
ch.place(x=700, y=340)
ch.bind("<<ComboboxSelected>>", callback)

l5 = Label(win, text="Book Code", width=11,font=f1)
l5.place(x=530, y=410)
data1 = fetchrec1()
ch1 = Combobox(win, font=f1, width=20, values=data1)
ch1.place(x=700, y=410)
ch1.bind("<<ComboboxSelected>>", callback_book)

# ch = Combobox(win, font=f1, values=data)
# ch.place(x=700, y=410)
# ch.bind("<<ComboboxSelected>>")

t8 = Entry(win, bd=2, font=f1)
t8.place(x=1200, y=350)

l8 = Label(win, text=" Student Name ",width=14, font=f1)
l8.place(x=1000, y=340)

t9 = Entry(win, bd=2, font=f1)
t9.place(x=1200, y=410)

l9 = Label(win, text="Book Title",width=14, font=f1)
l9.place(x=1000, y=410)

l3 = Label(win, text=" Remark ",width=11, font=f1)
l3.place(x=530, y=480)

t5 = Entry(win, bd=2, font=f1)
t5.place(x=700, y=480)

b1 = Button(win, text="Add", font=f1, width=7, command=maxrec)
b1.place(x=530, y=570)

b2 = Button(win, text="Save", font=f1, width=7, command=saverec)
b2.place(x=630, y=570)

b3 = Button(win, text="Search", font=f1, width=7, command=serrec)
b3.place(x=730, y=570)

b4 = Button(win, text="Update", font=f1, width=7, command=uprec)
b4.place(x=830, y=570)

b5 = Button(win, text="Delete", font=f1, width=7, command=delrec)
b5.place(x=930, y=570)

b6 = Button(win, text="Exit", font=f1, width=7, command=quit)
b6.place(x=1030, y=570)


win.mainloop()