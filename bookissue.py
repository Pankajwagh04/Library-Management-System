from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
import datetime




# Main window setup
win = Toplevel()
win.title("Library Management System")
win.geometry("1580x1080")
f1 = ("Arial", 15, 'bold')
f2 = ("Arial", 20, 'bold')

# Load background image
path = Image.open(r"C:\photo\close-up-still-life-hard-exams_23-2149314077.jpg")
render = ImageTk.PhotoImage(path)

img = Label(win, image=render)
img.image = render  # ✅ Is line se reference store hoga
img.place(x=1, y=1)


# Clear fields
def clfield():

    cal1.delete(0, END)
    ch.delete(0, END)
    ch1.delete(0, END)
    cal2.delete(0, END)

def fetchrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    cursor = mydb.cursor()
    cursor.execute("select sno from studmast order by sno")
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
    cursor.execute("select bcode from bookmast order by  bcode")
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


# Fetch max record number
def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    mycur = mydb.cursor()
    mycur.execute("select * from bookissue")
    mydata = mycur.fetchall()
    mx = 0
    for i in mydata:
        mx=i[0]
    mx=mx+1
    t1.delete(0,END)
    t1.insert(0,mx)
    clfield()
# # Save record
# def saverec():
#     s1 = t1.get()
#     s2 = cal1.get()
#     s3 = ch.get()
#     s4 = ch1.get()
#     s5 = cal2.get()
#     if s2.strip() == "":
#         messagebox.showinfo('Warning...', 'please enter isno')
#         return
#     if s3.strip() == "":
#         messagebox.showinfo('Warning...', 'please enter sno')
#         return
#     if s4.strip() == "":
#         messagebox.showinfo('Warning...', 'please enter bcode')
#         return
#     if s5.strip() == "":
#         messagebox.showinfo('Warning...', 'please enter exretdate')
#         return
#
#     mydb = mysql.connector.connect (
#         user="root",
#         password="",
#         host="localhost",
#         database="lms",
#     )
#     mycur = mydb.cursor()
#     mycur.execute("insert into bookissue values(" + s1 + ",'" + s2 + "','" + s3 + "','" + s4 + "'," + s5 + ")")
#     mydb.commit()
#     messagebox.showinfo('confirm', "Record is Save")
#     maxrec()


def saverec():
    s1 = t1.get()
    s2 = cal1.get()  # should be YYYY-MM-DD
    s3 = ch.get()
    s4 = ch1.get()
    s5 = cal2.get()  # should be YYYY-MM-DD

    if s2.strip() == "":
        messagebox.showinfo('Warning...', 'please enter isdate')
        return
    if s3.strip() == "":
        messagebox.showinfo('Warning...', 'please enter sno')
        return
    if s4.strip() == "":
        messagebox.showinfo('Warning...', 'please enter bcode')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'please enter expertdate')
        return

    try:
        # Optional: Validate date format
        datetime.datetime.strptime(s2, "%Y-%m-%d")
        datetime.datetime.strptime(s5, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Date Format Error", "Dates must be in YYYY-MM-DD format.")
        return

    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    mycur = mydb.cursor()

    query = "INSERT INTO bookissue (isno, isdate, sno, bcode, expertdate) VALUES (%s, %s, %s, %s, %s)"
    values = (s1, s2, s3, s4, s5)

    mycur.execute(query, values)
    mydb.commit()
    messagebox.showinfo('Confirm', "Record is Saved")
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
    mycur.execute("select * from bookissue where isno=" + s1)
    mydata = mycur.fetchone()

    if mydata is not None:
        cal1.insert(0, mydata[1])
        ch.insert(0, mydata[2])
        ch1.insert(0, mydata[3])
        cal2.insert(0, mydata[4])
    else:
        messagebox.showinfo('confirm', 'Record is Not Found')
# Update record
def uprec():
    s1 = t1.get()
    s2 = cal1.get()
    s3 = ch.get()
    s4 = ch1.get()
    s5 = cal2.get()
    if s2.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter isno')
        return
    if s3.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter sno')
        return
    if s4.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter bcode')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter exretdate')
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms"
    )
    mycur = mydb.cursor()
    mycur.execute("UPDATE bookissue SET  sno='"+s3+"', bcode='"+s3+"', expertdate='"+s5+"'WHERE isno="+s1)
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
        mycur.execute("DELETE FROM bookissue WHERE isno=" + s1)
        mydb.commit()
        messagebox.showinfo('Confirm', 'Record Is Deleted')
        maxrec()

# Book Return Section
l1 = Label(win, text=" Book Issue ",width=15, font=f2, fg='black', bg='pink')
l1.place(x=600, y=100)

# Return No. Entry
l2 = Label(win, text="Issue No. ",width=11, font=f1)
l2.place(x=530, y=200)
t1 = Entry(win, bd=2,width=20, font=f1)
t1.place(x=700, y=200)

# Return Date Entry
l3 = Label(win, text="Issue Date",width=11, font=f1)
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
l5.place(x=530, y=400)
data1 = fetchrec1()
ch1 = Combobox(win, font=f1, width=20, values=data1)
ch1.place(x=700, y=400)
ch1.bind("<<ComboboxSelected>>", callback_book)

# ch = Combobox(win, font=f1, values=data)
# ch.place(x=700, y=410)
# ch.bind("<<ComboboxSelected>>")

t8 = Entry(win, bd=2, font=f1)
t8.place(x=1200, y=340)

l8 = Label(win, text=" Student Name ",width=14, font=f1)
l8.place(x=1000, y=340)

t9 = Entry(win, bd=2, font=f1)
t9.place(x=1200, y=400)

l9 = Label(win, text="Book Title",width=14, font=f1)
l9.place(x=1000, y=400)

l3 = Label(win, text=" Expertdate ",width=11, font=f1)
l3.place(x=530, y=480)

cal2 = DateEntry(win, selectmode="day",width=20, font=f1, date_pattern="yyyy-mm-dd")
cal2.place(x=700, y=480)

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