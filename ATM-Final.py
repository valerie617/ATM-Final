#funstuff
from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk
from datetime import datetime
from threading import *
from math import *


d= datetime.now()
y = d.year
h = d.hour

def process():
    print blah

def openfileR():
    print "file r"

def openfileW():
    print "file w"

def retrieve():
    entrytxt = entry1.get()
    entrytxt = entrytxt + ".txt"
    doc = open(entrytxt, "r")
    account_number = doc.readline()
    account_number = account_number[0:-1]
    name = doc.readline()
    name = name[0:-1]
    label3.config(text=name)
    balance = doc.readline()
    balance = balance[0:-1]
    label5.config(text="$"+balance)
    #insert()

#def insert():
    #label3.insert(name)

def submit():
    entrytxt2 = entry2.get()
    balance = entrytxt2 - balance
    print balance
  
root = Tk() #gives us a blank canvas object to work with
root.title("Fab Things Banking")


entry1 = Entry(root)
entry1.grid(row=0, column=1)



#image = Image.open("morning.jpg")
#image = image.resize((150,120))
#photo = ImageTk.PhotoImage(image)

#label2 = Label(image=photo)
#label2.image = photo # keep a reference!
#label2.grid(row=0, column=0, sticky=EW)

label1 = Label(root, text="Account number:")
label1.grid(row=0, column=0)


button1 = Button(root, text="Submit", command=retrieve)
button1.grid(row=0, column=3)



label2 = Label(root, text="Name:")
label2.grid(row=1, column=0, sticky=W)

label3 = Label(root, text="")
label3.grid(row=1, column=1, sticky=W)

label4 = Label(root, text="Balance:")
label4.grid(row=2, column=0, sticky=W)

label5 = Label(root, text= "")
label5.grid(row=2, column=1, sticky=W)

label6 = Label(root, text="Withdraw: $")
label6.grid(row=3, column=0, sticky=W)

entry2 = Entry(root)
entry2.grid(row=3, column=1, sticky=W)
entry2.bind("<Return>", process)

button2 = Button(root, text=">", command=submit)
button2.grid(row=3, column=2, sticky=W)

label7 = Label(root, text="Deposit: $")
label7.grid(row=4, column=0, sticky=W)

entry3 = Entry(root)
entry3.grid(row=4, column=1, sticky=W)
entry3.bind("<Return>", process)

button3 = Button(root, text=">", command=submit)
button3.grid(row=4, column=2, sticky=W)

label8 = Label(root, text="Transfer to:")
label8.grid(row=5, column=0, sticky=W)

label9 = Label(root, text="     Account #:")
label9.grid(row=6, column=0, sticky=W)

entry4 = Entry(root)
entry4.grid(row=6, column=1, sticky=W)
entry4.bind("<Return>", process)

button4 = Button(root, text=">", command=submit)
button4.grid(row=6, column=2, sticky=W)

label10 = Label(root, text="     Amount: $")
label10.grid(row=7, column=0, sticky=W)

entry5 = Entry(root)
entry5.grid(row=7, column=1, sticky=W)
entry5.bind("<Return>", process)

button5 = Button(root, text=">", command=submit)
button5.grid(row=7, column=2, sticky=W)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Help", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Logout", command=openfileW)

menubar.add_cascade(label="Options", menu=filemenu)

root.config(menu=menubar)







mainloop()