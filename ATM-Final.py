#funstuff
from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk
from datetime import datetime
from threading import *

def openfileR():
    print "help"

def openfileW():
    print "logout"

d= datetime.now()
y = d.year
h = d.hour

def process():
    



root = Tk() #gives us a blank canvas object to work with
root.title("Fab Things Banking")

#label1 = Label(root, text="Please enter account number", bg="white", anchor=W)
#label1.grid(row=0, column=0, sticky=EW, columnspan=2)

entry1 = Entry(root)
entry1.grid(row=1, column=0)
entry1.bind("<Return>", process)





image = Image.open("morning.jpg")
image = image.resize((150,120))
photo = ImageTk.PhotoImage(image)

label2 = Label(image=photo)
label2.image = photo # keep a reference!
label2.grid(row=0, column=0, sticky=EW)

label1 = Label(root, text="Good Morning")
label1.grid(row=0, column=0, sticky=EW, columnspan=4)









menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Help", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Logout", command=openfileW)

menubar.add_cascade(label="Options", menu=filemenu)

root.config(menu=menubar)







mainloop()