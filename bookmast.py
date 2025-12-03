from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk


# Initialize Tkinter window first hyy7
win =Toplevel()

# Load and display image
path = Image.open(r"C:\Users\panka\OneDrive\Documents\WhatsApp Image 2025-03-01 at 11.04.16_bd7dfe80.jpg")
path = path.resize((1520, 1080))
render = ImageTk.PhotoImage(path)
img = Label(win, image=render)
img.pack()

def clfield():
    t2.delete(0, END)
    t3.delete(0, END)
    ch.delete(0, END)
    ch1.delete(0, END)
    ch2.delete(0, END)
    t7.delete(0, END)

def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    mycur = mydb.cursor()
    mycur.execute("select * from bookmast")
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
    s4 = ch.get()
    s5 = ch1.get()
    s6 = ch2.get()
    s7 = t7.get()
    if s2.strip() == "":
        messagebox.showinfo('Warning...', 'please enter bcode')
        return
    if s3.strip() == "":
        messagebox.showinfo('Warning...', 'please enter bauther')
        return
    if s4.strip() == "":
        messagebox.showinfo('Warning...', 'please enter publication')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'please enter language')
        return
    if s6.strip() == "":
        messagebox.showinfo('Warning...', 'please enter btype')
        return
    if s7.strip() == "":
        messagebox.showinfo('Warning...', 'please enter price')
        return
    mydb = mysql.connector.connect (

        user="root",
        password="",
        host="localhost",
        database="lms",
    )
    mycur = mydb.cursor()
    mycur.execute("insert into bookmast value(" + s1 + ",'" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + s6 + "','" + s7 + "')")
    mydb.commit()
    messagebox.showinfo('confirm', "Record  Is Saved")
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
    mycur.execute("select * from bookmast where bcode=" + s1)
    mydata = mycur.fetchone()

    if mydata is not None:
        t2.insert(0, mydata[1])
        t3.insert(0, mydata[2])
        ch.insert(0, mydata[3])
        ch1.insert(0, mydata[4])
        ch2.insert(0, mydata[5])
        t7.insert(0, mydata[6])
    else:
        messagebox.showinfo('confirm', 'Record Is Not Found')

def uprec():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = ch.get()
    s5 = ch1.get()
    s6 = ch2.get()
    s7 = t7.get()
    if s2.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter bcode')
        return
    if s3.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter bauther')
        return
    if s4.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter publication')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter language')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter btype')
        return
    if s5.strip() == "":
        messagebox.showinfo('Warning...', 'Please enter price')
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",

        database="lms"
    )
    mycur = mydb.cursor()
    mycur.execute(
        f"UPDATE bookmast SET btitle='{s2}', bauther='{s3}', publication='{s4}', language='{s5}',btype='{s6}',price='{s7}' WHERE bcode={s1}")
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
        mycur.execute("DELETE FROM bookmast WHERE bcode=" + s1)
        mydb.commit()
        messagebox.showinfo('Confirm', 'Record Is Deleted')
        maxrec()


win.title("LMS")
win.geometry("1580x1080")
f1 = ("Arial", 15, 'bold')
f2 = ("Arial", 20, 'bold')

l1 = Label(win, text="Book Information", font=f2,  fg='black')
l1.place(x=600, y=100)

l2 = Label(win, text=" Book Code ",width=11, font=f1)
l2.place(x=530, y=200)
t1 = Entry(win, bd=2,width=20, font=f1)
t1.place(x=700, y=200)

l3 = Label(win, text=" Book Title ", width=11,font=f1)
l3.place(x=530, y=270)
t2 = Entry(win, bd=2, width=20,font=f1)
t2.place(x=700, y=270)

l4 = Label(win, text=" Auther ",width=11, font=f1)
l4.place(x=530, y=340)
t3 = Entry(win, bd=2,width=20, font=f1)
t3.place(x=700, y=340)

l5 = Label(win, text=" Publication ",width=11, font=f1)
l5.place(x=530, y=410)
data = ["prashant publication", "Katha","bengali Center",	"Oxford", "Speaking Tiger Books", "Arihant Publications", "Bloomsbury India", "Srishti Publishing", "Roli Books"]
ch = ttk.Combobox(win, values=data,width=20, font=f1)
ch.place(x=700, y=410)

l6 = Label(win, text=" Language ", width=11,font=f1)
l6.place(x=530, y=480)
data = ["English","Hindi","Marathi","Bengali","Telugu","Urdu"]
ch1 = ttk.Combobox(win, values=data, width=20,font=f1)
ch1.place(x=700, y=480)

l7 = Label(win, text=" Book Type ", width=11,font=f1)
l7.place(x=530, y=550)
data = ["Autobiography","Mystery","Horror","South Indian","Eastern","Thriller","History","Crime","Classics"]
ch2 = ttk.Combobox(win, values=data,width=20, font=f1)
ch2.place(x=700, y=550)

l8 = Label(win, text="Price", width=11,font=f1)
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
