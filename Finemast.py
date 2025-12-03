from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.ttk import Combobox

win = Toplevel()
win.title("Library Management System")
win.geometry("1580x1080")

path = Image.open(r"C:\photo\old-books-436498_1280.jpg")
path = path.resize((1520, 1080))
render = ImageTk.PhotoImage(path)
img = Label(win, image=render)
img.pack()

# win = Tk()
def clfield():
    cal.delete(0, END)
    ch.delete(0, END)
    t4.delete(0, END)
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

def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    mycur = mydb.cursor()
    mycur.execute("select * from finemast")
    mydata = mycur.fetchall()
    mx = 0
    for i in mydata:
        mx = i[0]
    mx = mx + 1
    t1.delete(0, END)
    t1.insert(0, mx)
    clfield()

def saverec():
    s1 = t1.get()
    s2 = cal.get()
    s3 = ch.get()
    s4 = t4.get()
    s5 = t5.get()
    print(s1,s2,s3,s4,s5)
    if s2.strip() == "":
        messagebox.showinfo('Warning...', 'please enter rno')
        return
    if s3.strip() == "":
        messagebox.showinfo('Warning...', 'please enter sno')
        return
    if s4.strip() == "":
        messagebox.showinfo('Warning...', 'please enter reason')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'please enter amount')
        return
    mydb = mysql.connector.connect (

        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    mycur = mydb.cursor()
    mycur.execute("insert into finemast value(" + s1 + ",'" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "')")
    mydb.commit()
    messagebox.showinfo('confirm', "record Is Save")
    maxrec()


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
    mycur.execute("select * from finemast where rno=" + s1)
    mydata = mycur.fetchone()

    if mydata is not None:
        cal.insert(0, mydata[1])
        ch.insert(0, mydata[2])
        t4.insert(0, mydata[3])
        t5.insert(0, mydata[4])
    else:
        messagebox.showinfo('confirm', 'rec is not found')

def uprec():
    s1 = t1.get()
    s2 = cal.get()
    s3 = ch.get()
    s4 = t4.get()
    s5 = t5.get()
    if s2.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter rno')
        return
    if s3.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter sno')
        return
    if s4.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter reason')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter amount')
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms"
    )
    mycur = mydb.cursor()
    mycur.execute(
        f"UPDATE finemast SET rdate='{s2}', sno='{s3}', reason='{s4}', amount='{s5}' WHERE rno={s1}")
    mydb.commit()
    messagebox.showinfo('Confirm', "Record Is Updated")
    maxrec()

def delrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
        charset="utf8"
    )
    mycur = mydb.cursor()
    ans = messagebox.askyesno('Confirm', 'Are you sure you want to delete?')
    if ans:
        s1 = t1.get()
        mycur.execute("DELETE FROM finemast WHERE rno=" + s1)
        mydb.commit()
        messagebox.showinfo('Confirm', 'Record is deleted')
        maxrec()




win.title("Library Management System")
win.geometry("1580x1080")
f1 = ("Arial", 15, 'bold')
f2 = ("Arial", 20, 'bold')

l1 = Label(win, text=" Book Fine ",width=15, font=f2, fg='black')
l1.place(x=600, y=100)

l2 = Label(win, text=" Return No.", width=11,font=f1, )
l2.place(x=530, y=200)
t1 = Entry(win, bd=2,width=20, font=f1)
t1.place(x=700, y=200)

l3 = Label(win, text="Return Date ",width=11, font=f1)
l3.place(x=530, y=270)
cal = DateEntry(win, selectmode="day",width=20, font=f1, date_pattern="yyyy-mm-dd")
cal.place(x=700, y=270)

l4 = Label(win, text="Student No.",width=11, font=f1)
l4.place(x=530, y=340)
data = fetchrec()
ch = Combobox(win, font=f1, width=20,values=data)
ch.place(x=700, y=340)
ch.bind("<<ComboboxSelected>>", callback)

t8 = Entry(win, bd=2, width=20,font=f1)
t8.place(x=1200, y=340)

l8 = Label(win, text=" Student Name ",width=14, font=f1)
l8.place(x=1000, y=340)
# t9 = Entry(win, bd=2, font=f1)
# t9.place(x=1200, y=400)

l5 = Label(win, text="Reason ", width=11,font=f1)
l5.place(x=530, y=410)
t4 = Entry(win, bd=2,width=20, font=f1)
t4.place(x=700, y=410)



l6 = Label(win, text="Amount", width=11,font=f1)
l6.place(x=530, y=480)
t5 = Entry(win, bd=2, width=20,font=f1)
t5.place(x=700, y=480)

b1 = Button(win, text="Add", font=f1, width=6, command=maxrec)
b1.place(x=530, y=570)

b2 = Button(win, text="Save", font=f1, width=6, command=saverec)
b2.place(x=630, y=570)

b3 = Button(win, text="Search", font=f1, width=6, command=serrec)
b3.place(x=730, y=570)

b4 = Button(win, text="Update", font=f1, width=6, command=uprec)
b4.place(x=830, y=570)

b5 = Button(win, text="Delete", font=f1, width=6, command=delrec)
b5.place(x=930, y=570)

b6 = Button(win, text="Exit", font=f1, width=6, command=quit)
b6.place(x=1030, y=570)


win.mainloop()

