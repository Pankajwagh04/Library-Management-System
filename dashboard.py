from tkinter import *
from PIL import Image, ImageTk
win=Tk()



# win.configure(bg="light blue")
path = Image.open("C:\photo\mansi-telharkar-4hnI1xdvxKo-unsplash.jpg")
path = path.resize((1520, 1080))
render = ImageTk.PhotoImage(path)
img = Label(win, image=render)
img.pack()


def open_stureg():
    import stureg

def open_bookmreg():
    import bookmreg

def open_bookisreg():
    import bookisreg

def open_bookretreg():
    import bookretreg

def open_finereg():
    import finereg

def open_book():
    import bookmreg


def open_studmast():
    import studmast

def open_bookmast():
    import bookmast

def open_bookissue():
    import bookissue

def open_bookreturn():
    import bookreturn

def open_Finemast():
    import Finemast

f1 = ("Arial", 15, 'bold')
f2 = ("Arial", 20, 'bold')

l1 = Label(win, text=" Library Management System", font=f2, fg='black', bg='pink')
l1.place(x=600, y=100)

b1 = Button(win, text="Studmast Entry Form ", font=f1,  command=open_studmast)
b1.place(x=400, y=200)

b2 = Button(win, text=" Book Entry Form ", font=f1,  command=open_bookmast)
b2.place(x=500, y=300)

b3 = Button(win, text=" Book Issue Form ", font=f1,  command=open_bookissue)
b3.place(x=600, y=400)

b4 = Button(win, text=" Book Return Form ", font=f1,  command=open_bookreturn)
b4.place(x=700, y=500)

b5 = Button(win, text=" Fine Mangement  ", font=f1,  command=open_Finemast)
b5.place(x=800, y=600)

l1 = Label(win, text=" Developed By ",width=20, font=f1)
l1.place(x=110, y=550)

l2 = Label(win, text=" Pankaj Wagh. ", width=20,font=f1)
l2.place(x=110, y=585)

l3 = Label(win, text="  Project Guide ",width=20, font=f1)
l3.place(x=1110, y=550)

l4 = Label(win, text=" Devendra Patil Sir ", width=20,font=f1)
l4.place(x=1110, y=585)

win.title(" Library System ")
win.configure(bg='light yellow')
win.geometry("1580x1050")

mb=Menu(win)
ReportMenu=Menu(mb)
ReportMenu.add_command(label="Student Register ",command=open_stureg)
ReportMenu.add_separator()
ReportMenu.add_command(label="Book Register ",command=open_book)
ReportMenu.add_separator()
ReportMenu.add_command(label="Book Issue Register ",command=open_bookisreg)
ReportMenu.add_separator()
ReportMenu.add_command(label="Book Return Register ",command=open_bookretreg)
ReportMenu.add_separator()
ReportMenu.add_command(label="Fine Register ",command=open_finereg)
ReportMenu.add_separator()
mb.add_cascade(label="Report",menu=ReportMenu)
win.config(menu=mb)




win.mainloop()