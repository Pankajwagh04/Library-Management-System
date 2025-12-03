from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Function to open the dashboard
def open_dashboard():
    import dashboard

# Login function
def login():
    username = t1.get()
    password = t2.get()

    if username == "pankaj" and password == "wagh":
        win.destroy()
        open_dashboard()
    else:
        if username != "pankaj":
            messagebox.showerror('Login Failed', "Invalid username")
        else:
            messagebox.showerror('Login Failed', "Invalid password")

# Main Window
win = tk.Tk()
win.configure(bg="#F0F0F0")
win.title("Login System")
win.geometry("1700x1300")

# Background Frame with shadow effect
bg_frame = tk.Frame(win, bg="white", width=450, height=400, relief="raised", bd=2)
bg_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
bg_frame.configure(relief="solid", bd=5)

# Title Label
l1 = Label(win, text='Login', font=("Georgia", 35, 'bold'), fg='#FF4F58', bg="#F0F0F0")
l1.place(relx=0.5, rely=0.25, anchor=CENTER)

# Username Label & Entry
l2 = Label(bg_frame, text='User Name', font=('Arial', 15, 'bold'), fg='#FF4F58', bg="white")
l2.place(x=50, y=80)
t1 = Entry(bg_frame, bd=2, font=('Arial', 15), width=25, bg="#F0F0F0", fg='black', relief="solid")
t1.place(x=50, y=120)

# Password Label & Entry
l4 = Label(bg_frame, text='Password', font=('Arial', 15, 'bold'), fg='#FF4F58', bg="white")
l4.place(x=50, y=170)
t2 = Entry(bg_frame, bd=2, font=('Arial', 15), width=25, bg="#F0F0F0", fg='black', show='*', relief="solid")
t2.place(x=50, y=210)

# Button Hover Effects
def on_enter(e):
    e.widget.config(bg="#FF4F58", fg="white")

def on_leave(e):
    e.widget.config(bg="#FF6B6B", fg="black")

# Login Button
b1 = Button(bg_frame, text='Login', font=('Arial', 15, 'bold'), width=10, bg='#FF6B6B', fg="black", command=login, relief="solid")
b1.place(x=70, y=270)
b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)

# Cancel Button
b2 = Button(bg_frame, text='Cancel', font=('Arial', 15, 'bold'), width=10, bg='#FF6B6B', fg="black", command=win.quit, relief="solid")
b2.place(x=230, y=270)
b2.bind("<Enter>", on_enter)
b2.bind("<Leave>", on_leave)

win.mainloop()


