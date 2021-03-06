#funstuff
from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk
from threading import *
from math import *
import os
import os.path


def retrieve():
    entrytxt = entry1.get()
    try:
        int(entrytxt)
    except:
        tkMessageBox.showwarning("Error", "Invalid input") 
        entry1.delete(0,END)
    entrytxt = entrytxt + ".txt"
    if os.path.isfile(entrytxt) and os.access(entrytxt, os.R_OK):
        doc = open(entrytxt, "r")
        account_number = doc.readline()
        account_number = account_number[0:-1]
        global account_number
        name = doc.readline()
        name = name[0:-1]
        global name
        label3.config(text=name)
        balance = doc.readline()
        balance = round(float(balance), 2)
        global balance
        label5.config(text=balance)
        doc.close()
        entry1.config(state=DISABLED)
    else:
       tkMessageBox.showwarning("Error", "Account does not exist") 
       entry1.delete(0,END)       


def withdraw_submit():
    entrytxt2 = entry2.get()
    try:
        entrytxt2_number = float(entrytxt2)
    except:
         tkMessageBox.showwarning("Error", "Invalid input") 
         entry2.delete(0,END)       
    if float(balance) >= float(entrytxt2):
        y = round(entrytxt2_number, 2)
        if entrytxt2_number - y != 0:
            tkMessageBox.showwarning("Error", "Invalid input") 
            entry2.delete(0,END)
        else:
            new_balance = float(balance) - float(entrytxt2)
            balance = new_balance
            balance = round(float(balance), 2)
            global balance
            label5.config(text=balance)
            entrytxt = entry1.get()
            entrytxt = entrytxt + ".txt"
            doc = open(entrytxt, "w")
            doc.write (account_number + "\n" + name + "\n" + str(new_balance)) 
            doc.close()
            entry2.delete(0,END)
            tkMessageBox.showinfo("Withdraw", "Transaction Successful")
    else:
        tkMessageBox.showwarning("Error", "Insufficient Funds") 
        entry2.delete(0,END)       
    
def deposit_submit():
    entrytxt3 = entry3.get()
    try:
        entrytxt3_number = float(entrytxt3)
        y = round(entrytxt3_number, 2)
        if entrytxt3_number - y != 0:
            tkMessageBox.showwarning("Error", "Invalid input") 
            entry3.delete(0,END)
        else:
            new_balance = float(balance) + float(entrytxt3)
            balance = new_balance
            balance = round(float(balance), 2)
            global balance
            label5.config(text=balance)
            entrytxt = entry1.get()
            entrytxt = entrytxt + ".txt"
            doc = open(entrytxt, "w")
            doc.write (account_number + "\n" + name + "\n" + str(new_balance)) 
            doc.close()
            entry3.delete(0,END)
            tkMessageBox.showinfo("Deposit", "Transaction Successful")
    except:
         tkMessageBox.showwarning("Error", "Invalid input") 
         entry3.delete(0,END)     

    
def transfer_submit():
    entrytxt4 = entry4.get()
    entrytxt4 = entrytxt4 + ".txt"
    if os.path.isfile(entrytxt4) and os.access(entrytxt4, os.R_OK):
        doc2 = open(entrytxt4, "r")
        account_number2 = doc2.readline()
        account_number2 = account_number2[0:-1]
        name2 = doc2.readline()
        name2 = name2[0:-1]
        balance2 = doc2.readline()
        doc2.close()
        entrytxt5 = entry5.get()
        try:
            entrytxt5_number = float(entrytxt5)
            y = round(entrytxt5_number, 2)
            if entrytxt5_number - y != 0:
                tkMessageBox.showwarning("Error", "Invalid input") 
                entry4.delete(0,END)
                entry5.delete(0,END)
            else:
                new_balance = float(balance) - float(entrytxt5)
                new_balance2 = float(balance2) + float(entrytxt5)
                new_balance2 = round(float(new_balance2), 2)
                balance = new_balance
                balance = round(float(balance), 2)
                global balance
                label5.config(text=balance)
                entrytxt = entry1.get()
                entrytxt = entrytxt + ".txt"
                doc = open(entrytxt, "w")
                doc.write (account_number + "\n" + name + "\n" + str(new_balance)) 
                doc.close()
                entrytxt4 = entry4.get()  
                entrytxt4 = entrytxt4 + ".txt"
                doc = open(entrytxt4, "w")
                doc.write (account_number2 + "\n" + name2 + "\n" + str(new_balance2)) 
                doc.close()
                entry4.delete(0,END)
                entry5.delete(0,END)
                tkMessageBox.showinfo("Transfer", "Transaction Successful")
        except:
            tkMessageBox.showwarning("Error", "Invalid input") 
            entry5.delete(0,END)  
    else:
        tkMessageBox.showwarning("Error", "Account does not exist") 
        entry4.delete(0,END)  
        entry5.delete(0,END)     

   
   
def logout():
    entry1.config(state=NORMAL)
    label3.config(text= "")
    entry1.delete(0,END)
    label5.config(text= "")
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)
    
def help():
    tkMessageBox.showinfo("Help", "Welcome to Fab Things Banking Company!  To begin, please enter your account number and click submit to log into your account. \n     -To withdraw, enter the amount you wish to extract and press the arrow key next to the box. \n     -To deposit, enter the amount you wish to add and press the arrow key next to the box. \n     -To transfer money to another account, enter the account number recieving the transfer, and the amount you wish to send.")
    
  
root = Tk() #gives us a blank canvas object to work with
root.title("Fab Things Banking")


entry1 = Entry(root)
entry1.grid(row=0, column=1)

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

button2 = Button(root, text=">", command=withdraw_submit)
button2.grid(row=3, column=2, sticky=W)

label7 = Label(root, text="Deposit: $")
label7.grid(row=4, column=0, sticky=W)

entry3 = Entry(root)
entry3.grid(row=4, column=1, sticky=W)

button3 = Button(root, text=">", command=deposit_submit)
button3.grid(row=4, column=2, sticky=W)

label8 = Label(root, text="Transfer to:")
label8.grid(row=5, column=0, sticky=W)

label9 = Label(root, text="     Account #:")
label9.grid(row=6, column=0, sticky=W)

entry4 = Entry(root)
entry4.grid(row=6, column=1, sticky=W)

label10 = Label(root, text="     Amount: $")
label10.grid(row=7, column=0, sticky=W)

entry5 = Entry(root)
entry5.grid(row=7, column=1, sticky=W)

button5 = Button(root, text=">", command=transfer_submit)
button5.grid(row=7, column=2, sticky=W)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Help", command=help)
filemenu.add_separator()
filemenu.add_command(label="Logout", command=logout)
menubar.add_cascade(label="Options", menu=filemenu)
root.config(menu=menubar)



mainloop()