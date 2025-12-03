import tkinter as tk
from tkinter import *
import mysql.connector
win = Toplevel()  # parent window
win.title("Student Register")
win.geometry("")  # width and height of window
#https://www.plus2net.com/python/tkinter-mysql.php0
####### end of connection ####

mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="lms"
    )
mycur=mydb.cursor()

mycur.execute("SELECT * from studmast")
r_set=mycur.fetchall()
f1=("arial",15,'bold')
l1=Label(win,text="Student  Register ",font=("Arial",20,'bold'),bg='white')


e=Label(win,width=10,text='Student No',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red' ,font=f1)
e.grid(row=0,column=0)
e=Label(win,width=10,text='Student Name',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=1)
e=Label(win,width=10,text='Student Address',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=2)
e=Label(win,width=10,text='City',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=3)
e=Label(win,width=10,text='Contact',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=4)
e=Label(win,width=10,text='Year',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red' ,font=f1)
e.grid(row=0,column=5)
e=Label(win,width=10,text='deposit',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=6)
#i=1


i=1
for student in r_set:
    for j in range(len(student)):
        width = 20
        if j in [1, 2, 3]:
            width = 40
        e = Entry(win, width=10, fg='blue',font=("arial",15,'bold'))
        e.grid(row=i+1, column=j)
        e.insert(END, student[j])
        e.configure(state='disabled')
    i = i + 1
win.config(bg='white')
win.mainloop()