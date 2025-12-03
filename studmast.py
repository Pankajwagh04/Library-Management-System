from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk


# Initialize Tkinter window first
win =Toplevel()

# Load and display image
path = Image.open(r"C:\Users\panka\OneDrive\Documents\WhatsApp Image 2025-03-01 at 11.04.16_e8c59965.jpg")
path = path.resize((1520, 1280))
render = ImageTk.PhotoImage(path)
img = Label(win, image=render)
img.pack()


# win = Tk()
def clfield():
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.delete(0, END)
    t7.delete(0, END)

def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    mycur = mydb.cursor()
    mycur.execute("select * from studmast")
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
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get().strip()
    s6 = ch.get()  # ✅ Use Combobox value instead of Entry
    s7 = t7.get()

    if not s2.strip():
        messagebox.showinfo('Warning...', 'Please enter Student Name')
        return
    if not s3.strip():
        messagebox.showinfo('Warning...', 'Please enter Address')
        return
    if not s4.strip():
        messagebox.showinfo('Warning...', 'Please enter City')
        return
    if not s5.strip():
        messagebox.showinfo('Warning...', 'Please enter Contact')
        return
    if not s6.strip():
        messagebox.showinfo('Warning...', 'Please enter Add Year')
        return
    if not s7.strip():
        messagebox.showinfo('Warning...', 'Please enter Deposit')
        return

    try:
        mydb = mysql.connector.connect(user="root", password="", host="localhost", database="lms")
        mycur = mydb.cursor()

        query = "INSERT INTO studmast (sno, sname, sadd, city, contact, ayear, deposit) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (s1, s2, s3, s4, s5, s6, s7)
        mycur.execute(query, values)

        mydb.commit()
        messagebox.showinfo('Confirm', "Record Is Saved")
        maxrec()
    except Exception as e:
        messagebox.showerror("Error", f"Database Error: {str(e)}")

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
    mycur.execute("select * from studmast where sno=" + s1)
    mydata = mycur.fetchone()

    if mydata is not None:
        t2.insert(0, mydata[1])
        t3.insert(0, mydata[2])
        t4.insert(0, mydata[3])
        t5.insert(0, mydata[4])
        t6.insert(0, mydata[5])
        t7.insert(0, mydata[6])
    else:
        messagebox.showinfo('confirm', 'Record Is Not Found')

def uprec():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    s6 = ch.get()  # ✅ Use Combobox for 'ayear'
    s7 = t7.get()

    if s2.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter Student Name')
        return
    if s3.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter Address')
        return
    if s4.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter City')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter Contact')
        return
    if s6.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter Add Year')
        return
    if s7.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter Deposit')
        return

    try:
        mydb = mysql.connector.connect(user="root", password="", host="localhost", database="lms")
        mycur = mydb.cursor()

        query = "UPDATE studmast SET sname=%s, sadd=%s, city=%s, contact=%s, ayear=%s, deposit=%s WHERE sno=%s"
        values = (s2, s3, s4, s5, s6, s7, int(s1))
        mycur.execute(query, values)

        mydb.commit()
        messagebox.showinfo('Confirm', "Record Is Updated")
        maxrec()
    except Exception as e:
        messagebox.showerror("Error", f"Database Error: {str(e)}")


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
        mycur.execute("DELETE FROM studmast WHERE sno=" + s1)
        mydb.commit()
        messagebox.showinfo('Confirm', 'Record Is Deleted')
        maxrec()


win.title(" Student Information  ")
win.geometry("1580x1280")
f1 = ("Arial", 15, 'bold')
f2 = ("Arial", 20, 'bold')

f1 = ("Book Antiqua", 15, 'bold',)
f2 = ("Book Antiqua", 20, 'bold')

l1 = Label(win, text=" Student Information ", width=20,font=f2, fg='black')
l1.place(x=600, y=100)



l2 = Label(win, text=" Student No. ",width=11, font=f1)
l2.place(x=530, y=200)
t1 = Entry(win, bd=2,width=20, font=f1)
t1.place(x=700, y=200)



l3 = Label(win, text=" Student Name ", width=11,font=f1)
l3.place(x=530, y=270)
t2 = Entry(win, bd=2, width=20,font=f1)
t2.place(x=700, y=270)



l4 = Label(win, text=" Student Add ",width=11, font=f1)
l4.place(x=530, y=340)
t3 = Entry(win, bd=2,width=20, font=f1)
t3.place(x=700, y=340)



l5 = Label(win, text=" City ",width=11, font=f1)
l5.place(x=530, y=410)
t4 = Entry(win, bd=2, width=20,font=f1)
t4.place(x=700, y=410)



l6 = Label(win, text=" Contact ", width=11,font=f1)
l6.place(x=530, y=480)
t5 = Entry(win, bd=2, width=20,font=f1)
t5.place(x=700, y=480)



l7 = Label(win, text=" Add Year ", width=11,font=f1)
l7.place(x=530, y=550)
t6 = Entry(win, bd=2,width=20, font=f1)
t6.place(x=700, y=550)
data = ["FY-BCA","SY-BCA","TY-BCA","FY-Bsc","SY-Bsc","TY-Bsc","FY-B.Com","SY-B.Com","TY-B.Com",]
ch = ttk.Combobox(win, values=data, width=20,font=f1)
ch.place(x=700, y=550)

l8 = Label(win, text="Deposit", width=11,font=f1)
l8.place(x=530, y=620)
t7 = Entry(win, bd=2, width=20,font=f1)
t7.place(x=700, y=620)

b1 = Button(win, text="Add", font=f1, width=6, command=maxrec)
b1.place(x=530, y=700)

b2 = Button(win, text="Save", font=f1, width=6, command=saverec)
b2.place(x=630, y=700)

b3 = Button(win, text="Search", font=f1, width=6, command=serrec)
b3.place(x=730, y=700)

b4 = Button(win, text="Update", font=f1, width=6, command=uprec)
b4.place(x=830, y=700)

b5 = Button(win, text="Delete", font=f1, width=6, command=delrec)
b5.place(x=930, y=700)

b6 = Button(win, text="Exit", font=f1, width=6, command=quit)
b6.place(x=1030, y=700)

win.mainloop()
