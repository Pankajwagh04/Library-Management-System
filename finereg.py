import tkinter as tk
from tkinter import *
import mysql.connector
win = Toplevel()  # parent window
win.title("Fine Register")
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

mycur.execute("SELECT * from finemast")
r_set=mycur.fetchall()
f1=("arial",15,'bold')
l1=Label(win,text="Finemast Register ",font=("Arial",20,'bold'),bg='white')


e=Label(win,width=10,text='Return No.',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red' ,font=f1)
e.grid(row=0,column=0)
e=Label(win,width=10,text='Return Date',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=1)
e=Label(win,width=10,text='Student No',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=2)
e=Label(win,width=10,text='Reason',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=3)
e=Label(win,width=10,text='Amount',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=4)


#i=1



i=1
for student in r_set:
    for j in range(len(student)):
        width = 20
        if j in [4]:
            width = 40
        e = Entry(win, width=10, fg='blue',font=("arial",15,'bold'))
        e.grid(row=i+1, column=j)
        e.insert(END, student[j])
        e.configure(state='disabled')
    i = i + 1
win.config(bg='white')
win.mainloop()