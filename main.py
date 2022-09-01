import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql
from mysql import connector
import os
import sys
import subprocess
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import dates as mpl_dates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#This is all the connections to database.
# This is how you connect the app to a Database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bank"
)
# This is the cursor you use to manage and operate queries from your app into database
mycursor = mydb.cursor()
# This is just to check the connection to the database
if (mydb.is_connected()):
    print("Database Connected")
else:
    print("Database Not connected")

# 3695 Is the security code for project
# This is the creation of the main screen that you see.
root = Tk()
root.title("ATM")
root.config(bg="gainsboro")
root.geometry("785x700")
mainFrame = Frame(root, bd=20, width=774, height=700, relief=RIDGE)
mainFrame.grid()

# Variables for the next one person
balance0199 = 60000
global save


# Resizing all the images to fit buttons
# Resize your images 1
myPic = Image.open('leftAR.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
leftARNew = ImageTk.PhotoImage(resize1)

# Resize your images 2
myPic = Image.open('one.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
oneNew = ImageTk.PhotoImage(resize1)

# Resize your images 3
myPic = Image.open('two.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
twoNew = ImageTk.PhotoImage(resize1)

# Resize your images 4
myPic = Image.open('three.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
threeNew = ImageTk.PhotoImage(resize1)

# Resize your images 5
myPic = Image.open('four.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
fourNew = ImageTk.PhotoImage(resize1)

# Resize your images 6
myPic = Image.open('five.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
fiveNew = ImageTk.PhotoImage(resize1)

# Resize your images 7
myPic = Image.open('six.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
sixNew = ImageTk.PhotoImage(resize1)

# Resize your images 8
myPic = Image.open('seven.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
sevenNew = ImageTk.PhotoImage(resize1)

# Resize your images 9
myPic = Image.open('eight.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
eightNew = ImageTk.PhotoImage(resize1)

# Resize your images 10
myPic = Image.open('nine.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
nineNew = ImageTk.PhotoImage(resize1)

# Resize your images 11
myPic = Image.open('zero.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
zeroNew = ImageTk.PhotoImage(resize1)

# Resize your images 12
myPic = Image.open('rArrow.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
rightARNew = ImageTk.PhotoImage(resize1)

# Resize your images 13
myPic = Image.open('empty.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
emptyNew = ImageTk.PhotoImage(resize1)

# Resize your images 14
myPic = Image.open('cancel.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
cancelNew = ImageTk.PhotoImage(resize1)

# Resize your images 15
myPic = Image.open('clear.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
clearNew = ImageTk.PhotoImage(resize1)

# Resize your images 16
myPic = Image.open('enter.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
enterNew = ImageTk.PhotoImage(resize1)


topFrame1 = Frame(mainFrame, bd=7, width=800, height=300, relief=RIDGE)
topFrame1.grid(row=1, column=0, padx=40)
topFrame2 = Frame(mainFrame, bd=7, width=734, height=300, relief=RIDGE)
topFrame2.grid(row=0, column=0, padx=8)

topFrame2L = Frame(topFrame2, bd=4, width=190, height=300, relief=RIDGE)
topFrame2L.grid(row=0, column=0, padx=12)

topFrame2M = Frame(topFrame2, bd=5, width=300, height=300, relief=RIDGE)
topFrame2M.grid(row=0, column=1, padx=12)

topFrame2R = Frame(topFrame2, bd=5, width=190, height=300, relief=RIDGE)
topFrame2R.grid(row=0, column=2, padx=12)
#All the global variables

# ================================Functions================================================================
def enter_Pin():

    # This is the function that handles everything that happens if enter button is clicked
    global x
    pinNo = root.txtReciept.get("1.0", "end-1c")
    x = pinNo
    print(pinNo)
    mycursor.execute(f'SELECT * FROM bankdetials WHERE pin= "{pinNo}"')
    pin = mycursor.fetchall()
    print(pin)
    mydb.commit()
    mydb.close()
    count = mycursor.rowcount
    if ((count !=0)):
        root.txtReciept.delete("1.0", END)

        root.txtReciept.insert(END, "\t\t ATM" + "\n\n")
        root.txtReciept.insert(END, "Withdraw Cash\t\t\t Loan" + "\n\n\n\n\n")
        root.txtReciept.insert(END, "Savings\t\t\t Deposit" + "\n\n\n\n\n")
        root.txtReciept.insert(END, "Balance\t\t\t Request New Pin" + "\n\n\n\n\n")
        root.txtReciept.insert(END, "Graphical Info\t\t\t Print Statement" + "\n\n\n\n\n")
        # ================================LEFT Buttons============================================================
        root.btnArL1 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=withdraw)\
        .grid(row=0, column=0, padx=2, pady=2)
        root.btnArL2 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=reciept)\
        .grid(row=1, column=0, padx=2, pady=2)
        root.btnArL3 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=balance)\
        .grid(row=2, column=0, padx=2, pady=2)
        root.btnArL4 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=show_graph)\
        .grid(row=3, column=0, padx=2, pady=2)
        # ================================RIGHT Buttons===========================================================
        root.btnArR1 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=Loan)\
        .grid(row=0, column=0, padx=2, pady=2)
        root.btnArR2 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=deposit)\
        .grid(row=1, column=0, padx=2, pady=2)
        root.btnArR3 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=requestPin)\
        .grid(row=2, column=0, padx=2, pady=2)
        root.btnArR4 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=statement)\
        .grid(row=3, column=0, padx=2, pady=2)



    else:
        root.txtReciept.delete("1.0", END)
        root.txtReciept.insert(END, "\t\t Invalid Pin " + "\n")
        root.txtReciept.insert(END, "\t\t Try Again " + "\n")
        root.txtReciept.insert(END, "           Transaction will be terminated shortly" + "\n\n\n\n")
        root.after(5000, root.destroy)




def Clear():
    # this is the only way you can clear a pin
    # This is the functions that handels everything that happens when clear button is clicked
    root.txtReciept.delete("1.0", END)
    # ================================LEFT Buttons============================================================
    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=withdraw)\
    .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept)\
    .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance)\
    .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew)\
    .grid(row=3, column=0, padx=2, pady=2)
    # ================================RIGHT Buttons===========================================================
    root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan)\
    .grid(row=0, column=0, padx=2, pady=2)
    root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=deposit)\
    .grid(row=1, column=0, padx=2, pady=2)
    root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin)\
    .grid(row=2, column=0, padx=2, pady=2)
    root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement)\
    .grid(row=3, column=0, padx=2, pady=2)









def Cancel_Transaction():
    #  This is the functions that handels everything that happens when cancel button is clicked
    cancel = tkinter.messagebox.askyesno("ATM", "Confirm if you want to Leave ATM")
    if cancel > 0:
        root.destroy()
    return


def withdraw():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    # This is the cursor you use to manage and operate queries from your app into database
    mycursor = mydb.cursor()
    # This is just to check the connection to the database
    if (mydb.is_connected()):
        print("Database Connected")
    else:
        print("Database Not connected")

    # This is the function that handles everything that happens if enter button is clicked
    def withdrawAMNT():
        mycursor.execute(f'SELECT balance FROM bank.bankdetials WHERE pin= "{x}"')
        balance1 = mycursor.fetchall()
        print("This is the variable ", balance1[0][0])
        mydb.commit()
        balance = str(balance1[0][0])
        balanceInt = int(balance)
        print(balance)
        withDAmnt = root.txtReciept.get("2.0", "2.13")
        print("the amount to withdraw is ", withDAmnt)
        withDAmntInt = int(withDAmnt)
        new_Balance = int(balance) - int(withDAmnt)
        new_Balance = str(new_Balance)

        if (withDAmntInt <= balanceInt):
            print("you can draw this amount")
            mycursor.execute(f'UPDATE bankdetials SET balance= "{new_Balance}" WHERE pin= "{x}"')
            mydb.commit()

            root.txtReciept.delete("1.0", END)
            root.txtReciept.insert(END, f"\t You Withdrew $ {withDAmnt}")

            root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=withdraw) \
                .grid(row=0, column=0, padx=2, pady=2)
            root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept) \
                .grid(row=1, column=0, padx=2, pady=2)
            root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
                .grid(row=2, column=0, padx=2, pady=2)
            root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
                .grid(row=3, column=0, padx=2, pady=2)
            # ================================RIGHT Buttons===========================================================
            root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan) \
                .grid(row=0, column=0, padx=2, pady=2)
            root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=deposit) \
                .grid(row=1, column=0, padx=2, pady=2)
            root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin) \
                .grid(row=2, column=0, padx=2, pady=2)
            root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement) \
                .grid(row=3, column=0, padx=2, pady=2)
        elif(withDAmntInt >= balanceInt):
            print("Cannot withdraw that amount")
            root.txtReciept.delete("1.0", END)
            root.txtReciept.insert(END, "\t You have insufficient funds\n")
            root.txtReciept.insert(END, f"\t    You only have $ {balance}\n")




    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, "How Much do you want to withdraw $:  \n")
    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=withdrawAMNT) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
        .grid(row=3, column=0, padx=2, pady=2)
    # ================================RIGHT Buttons===========================================================
    root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=deposit) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement) \
        .grid(row=3, column=0, padx=2, pady=2)





def deposit():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    # This is the cursor you use to manage and operate queries from your app into database
    mycursor = mydb.cursor()
    # This is just to check the connection to the database
    if (mydb.is_connected()):
        print("Database Connected")
    else:
        print("Database Not connected")

    def depositAMNT():
        mycursor.execute(f'SELECT balance FROM bank.bankdetials WHERE pin= "{x}"')
        balance1 = mycursor.fetchall()
        print("This is the variable ", balance1[0][0])
        mydb.commit()
        balance = str(balance1[0][0])
        print(balance)
        DAmnt = root.txtReciept.get("2.0", "2.13")
        print("the amount to deposit is ", DAmnt)
        new_Balance = int(balance) + int(DAmnt)
        new_Balance = str(new_Balance)

        print("you can draw this amount")
        mycursor.execute(f'UPDATE bankdetials SET balance= "{new_Balance}" WHERE pin= "{x}"')
        mydb.commit()
        root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=withdraw) \
            .grid(row=0, column=0, padx=2, pady=2)
        root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept) \
            .grid(row=1, column=0, padx=2, pady=2)
        root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
            .grid(row=2, column=0, padx=2, pady=2)
        root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew)\
            .grid(row=3, column=0, padx=2, pady=2)
        # ================================RIGHT Buttons===========================================================
        root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan) \
            .grid(row=0, column=0, padx=2, pady=2)
        root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=deposit) \
            .grid(row=1, column=0, padx=2, pady=2)
        root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin) \
            .grid(row=2, column=0, padx=2, pady=2)
        root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement) \
            .grid(row=3, column=0, padx=2, pady=2)

        root.txtReciept.delete("1.0", END)
        root.txtReciept.insert(END, f"\t You Deposited $ {DAmnt}")

    # this function handels what happens if you want to deposit
    global DAmnt
    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, "How Much do you want to Deposit $: \n")
    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
        .grid(row=3, column=0, padx=2, pady=2)
    # ================================RIGHT Buttons===========================================================
    root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArR2 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=depositAMNT) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement) \
        .grid(row=3, column=0, padx=2, pady=2)





def Loan():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    # This is the cursor you use to manage and operate queries from your app into database
    mycursor = mydb.cursor()
    # This is just to check the connection to the database
    if (mydb.is_connected()):
        print("Database Connected")
    else:
        print("Database Not connected")
    # this function handles what happens if you want to take out a loan
    def loanExec():
        mycursor.execute(f'SELECT balance FROM bank.bankdetials WHERE pin= "{x}"')
        balance1 = mycursor.fetchall()
        print("This is the variable ", balance1[0][0])
        mydb.commit()
        mycursor.execute(f'SELECT loan FROM bank.bankdetials WHERE pin= "{x}"')
        loan1 = mycursor.fetchall()
        print("You have a loan of: ", loan1[0][0])
        mydb.commit()
        loanstr = str(loan1[0][0])
        balance = str(balance1[0][0])
        intBal = int(balance)
        print(balance)
        loanAMNT = root.txtReciept.get("2.0", "2.13")
        print("the amount to Loan is ", loanAMNT)
        intLoan = int(loanAMNT)
        GotLoan = intLoan * 0.2


        if (GotLoan<= intBal and loan1 == 0):
            print("you can Loan this amount")
            mycursor.execute(f'UPDATE bankdetials SET loan = "{loanAMNT}" WHERE pin= "{x}"')
            mydb.commit()

            root.txtReciept.delete("1.0", END)
            root.txtReciept.insert(END, f"\t You Lend $ {loanAMNT}")

            root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=withdraw) \
                .grid(row=0, column=0, padx=2, pady=2)
            root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept) \
                .grid(row=1, column=0, padx=2, pady=2)
            root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
                .grid(row=2, column=0, padx=2, pady=2)
            root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
                .grid(row=3, column=0, padx=2, pady=2)
            # ================================RIGHT Buttons===========================================================
            root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan) \
                .grid(row=0, column=0, padx=2, pady=2)
            root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=deposit) \
                .grid(row=1, column=0, padx=2, pady=2)
            root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin) \
                .grid(row=2, column=0, padx=2, pady=2)
            root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement) \
                .grid(row=3, column=0, padx=2, pady=2)
        elif(GotLoan>= intBal):
            print("Cannot Loan that amount with your credit status")
            root.txtReciept.delete("1.0", END)
            root.txtReciept.insert(END, "           You do not have credit for this amount \n")
            root.txtReciept.insert(END, "  You need atleast 20% of loan amount in balance \n")
            root.txtReciept.insert(END, f"             You only have a balance of $ {balance}\n")
        if(loan1 !=0):
            root.txtReciept.delete("1.0", END)
            print(f"Cannot Loan that amount with you already took out a loan of: $ {loanstr}")
            root.txtReciept.insert(END,f"\t     Cannot Loan that amount\n")
            root.txtReciept.insert(END, f"        You already have a loan amount of: $ {loanstr}")



    global loanAMNT
    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, "How Much do you want to Loan $: \n")
    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
        .grid(row=3, column=0, padx=2, pady=2)
    # ================================RIGHT Buttons===========================================================
    root.btnArR1 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=loanExec) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement) \
        .grid(row=3, column=0, padx=2, pady=2)

def balance():
    root.txtReciept.delete("1.0", END)
    # this function handles what happens if you want to check your balance
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    # This is the cursor you use to manage and operate queries from your app into database
    mycursor = mydb.cursor()
    # This is just to check the connection to the database
    if (mydb.is_connected()):
        print("Database Connected")
    else:
        print("Database Not connected")
    # This is the function that handles everything that happens if enter button is clicked


    print("This is the pin: ", x)
    mycursor.execute(f'SELECT balance FROM bank.bankdetials WHERE pin= "{x}"')
    balance1 = mycursor.fetchall()
    print("This is the variable ", balance1[0][0])
    mydb.commit()
    balance = str(balance1[0][0])
    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, "\tyour balance is: $ " + balance)


def statement():
        # this function handles what happens if you want to check your statement
        root.txtReciept.delete("1.0", END)
        # this function handles what happens if you want to check your balance
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
        )
        # This is the cursor you use to manage and operate queries from your app into database
        mycursor = mydb.cursor()
        # This is just to check the connection to the database
        if (mydb.is_connected()):
            print("Database Connected")
        else:
            print("Database Not connected")
        # This is the function that handles everything that happens if enter button is clicked

        print("This is the pin: ", x)
        mycursor.execute(f'SELECT balance FROM bank.bankdetials WHERE pin= "{x}"')
        balance1 = mycursor.fetchall()
        print("This is the variable ", balance1[0][0])
        mydb.commit()
        balance = str(balance1[0][0])


        mycursor.execute(f'SELECT first_name FROM bank.bankdetials WHERE pin= "{x}"')
        name = mycursor.fetchall()
        print("This is the variable ", name[0][0])
        mydb.commit()
        name1 = str(name[0][0])

        mycursor.execute(f'SELECT last_name FROM bank.bankdetials WHERE pin= "{x}"')
        lname = mycursor.fetchall()
        print("This is the variable ", lname[0][0])
        mydb.commit()
        name2 = str(lname[0][0])

        mycursor.execute(f'SELECT loan FROM bank.bankdetials WHERE pin= "{x}"')
        loan = mycursor.fetchall()
        print("This is the variable ", loan[0][0])
        mydb.commit()
        loan1 = str(loan[0][0])

        mycursor.execute(f'SELECT savings FROM bank.bankdetials WHERE pin= "{x}"')
        savings = mycursor.fetchall()
        print("This is the variable ", savings[0][0])
        mydb.commit()
        save1 = str(savings[0][0])

        root.txtReciept.insert(END, f"\t   Hello Mr. {name1} {name2}.\n")
        root.txtReciept.insert(END, "             Here is your account info as follows: \n\n\n")
        root.txtReciept.insert(END, f"                Your account Balance is: ${balance}\n\n")
        root.txtReciept.insert(END, f"\tYour Loan amount  is: ${loan1}\n\n")
        root.txtReciept.insert(END, f"                 Your savings amount  is: ${save1}\n\n")
        root.txtReciept.insert(END, f"          Thank you for banking with OJ Banking.")



def show_graph():
    plt.style.use("classic")

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycursor = mydb.cursor()
    # This is just to check the connection to the database
    if (mydb.is_connected()):
        print("Database Connected")
    else:
        print("Database Not connected")

    mycursor.execute(f"SELECT balance FROM  bank.bankdetials WHERE pin={x}")
    bal = mycursor.fetchone()
    print(bal)
    mycursor.execute(f"SELECT loan FROM  bank.bankdetials WHERE pin={x}")
    loan = mycursor.fetchone()
    print(loan)
    mycursor.execute(f"SELECT savings FROM  bank.bankdetials WHERE pin={x}")
    save = mycursor.fetchone()
    print(save)

    mydb.commit()
    Names_x = ['Balance', 'Loan', 'Savings']
    amount_y = []

    for balance in bal:
        amt = int(bal[0])
        amount_y.append(amt)
    for loans in loan:
        amt = int(loan[0])
        amount_y.append(amt)
    for savings in save:
        amt = int(save[0])
        amount_y.append(amt)

    print(Names_x)
    print(amount_y)

    # Balance for graph



    # Maak eie varialbe sit name in (account)
    x_amount = np.arange(len(Names_x))

    # Geruik heirdie sit variable van x_amount en account
    plt.xticks(x_amount,Names_x)

    # Window size
    fig = plt.figure(figsize=(5.6, 6.0), dpi=50)
    # Om plot op te maak, bar(x-axis,y-axis)
    fig.add_subplot(111).bar(Names_x, amount_y, width= 0.5)
    # Dispaly canvas in tkinter in txtReciept
    chart = FigureCanvasTkAgg(fig, root.txtReciept)
    chart.get_tk_widget().grid(row=0, column=0)

    plt.xlabel('Accounts')
    plt.ylabel('Amount in R')
    plt.title('Graphical account info')



def reciept():
    #this function handels what happens if you want to have savings on hand and if you wanted to add savings.
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    # This is the cursor you use to manage and operate queries from your app into database
    mycursor = mydb.cursor()
    # This is just to check the connection to the database
    if (mydb.is_connected()):
        print("Database Connected")
    else:
        print("Database Not connected")

    # this function handles what happens if you want to take out a loan
    def savings():
        mycursor.execute(f'SELECT balance FROM bank.bankdetials WHERE pin= "{x}"')
        balance1 = mycursor.fetchall()
        print("This is the variable ", balance1[0][0])
        mydb.commit()
        mycursor.execute(f'SELECT savings FROM bank.bankdetials WHERE pin= "{x}"')
        save1 = mycursor.fetchall()
        print("You have a savings of: ", save1[0][0])
        mydb.commit()
        savestr = str(save1[0][0])
        balance = str(balance1[0][0])
        intBal = int(balance)
        print(balance)
        saveAMNT = root.txtReciept.get("3.0", "3.13")
        print("the amount to save is ", saveAMNT)
        intsave = int(saveAMNT)
        DBsave = int(savestr)
        savings = intsave + DBsave
        deductBal = intBal - intsave
        savings = str(savings)
        deductBal = str(deductBal)

        if (intsave <= intBal):
            print("you can saving amount this amount")
            mycursor.execute(f'UPDATE bankdetials SET savings = "{savings}" WHERE pin= "{x}"')
            mydb.commit()
            mycursor.execute(f'UPDATE bankdetials SET balance = "{deductBal}" WHERE pin= "{x}"')
            mydb.commit()

            root.txtReciept.delete("1.0", END)
            root.txtReciept.insert(END, f"\t              You saved ${saveAMNT}")

            root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=withdraw) \
                .grid(row=0, column=0, padx=2, pady=2)
            root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept) \
                .grid(row=1, column=0, padx=2, pady=2)
            root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
                .grid(row=2, column=0, padx=2, pady=2)
            root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew
                                 ) \
                .grid(row=3, column=0, padx=2, pady=2)
            # ================================RIGHT Buttons===========================================================
            root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan) \
                .grid(row=0, column=0, padx=2, pady=2)
            root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=deposit) \
                .grid(row=1, column=0, padx=2, pady=2)
            root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew,
                                  command=requestPin) \
                .grid(row=2, column=0, padx=2, pady=2)
            root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement) \
                .grid(row=3, column=0, padx=2, pady=2)
        elif (intsave >= intBal):
            print("You have Inssufficient funds")
            root.txtReciept.delete("1.0", END)
            root.txtReciept.insert(END, "             Your balance has insufficient funds\n")
            root.txtReciept.insert(END, f"              You only have a balance of ${balance}\n")

    mycursor.execute(f'SELECT balance FROM bank.bankdetials WHERE pin= "{x}"')
    balance1 = mycursor.fetchall()
    print("This is the variable ", balance1[0][0])
    mydb.commit()
    mycursor.execute(f'SELECT savings FROM bank.bankdetials WHERE pin= "{x}"')
    save1 = mycursor.fetchall()
    print("You have a savings of: ", save1[0][0])
    mydb.commit()
    savestr = str(save1[0][0])


    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, f"You currently have ${savestr} in savings  \n")
    root.txtReciept.insert(END, "How Much do you want to Save $: \n")
    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=savings) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
        .grid(row=3, column=0, padx=2, pady=2)
    # ================================RIGHT Buttons===========================================================
    root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement) \
        .grid(row=3, column=0, padx=2, pady=2)


def Start_program():

    os.startfile("main.py")


def requestPin():
    root.txtReciept.delete("1.0", END)
    # this function handles what happens if you want to check your balance
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    # This is the cursor you use to manage and operate queries from your app into database
    mycursor = mydb.cursor()
    # This is just to check the connection to the database
    if (mydb.is_connected()):
        print("Database Connected")
    else:
        print("Database Not connected")
    # This is the function that handles everything that happens if enter button is clicked
    def newPIN():

        print("This is the pin: ", x)
        mycursor.execute(f'SELECT pin FROM bank.bankdetials WHERE pin= "{x}"')
        Info = mycursor.fetchall()

        mydb.commit()

        newPin = root.txtReciept.get("4.0", "4.13")
        mycursor.execute(f'UPDATE bankdetials SET pin= "{newPin}" WHERE pin= "{x}"')
        mydb.commit()
        root.txtReciept.delete("1.0", END)
        root.txtReciept.insert(END, f"\t      Your New PIN is '{newPin}'\n")
        root.txtReciept.insert(END, "\tYou Will need to sign in again")
        root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=withdraw) \
            .grid(row=0, column=0, padx=2, pady=2)
        root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept) \
            .grid(row=1, column=0, padx=2, pady=2)
        root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
            .grid(row=2, column=0, padx=2, pady=2)
        root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
            .grid(row=3, column=0, padx=2, pady=2)
        # ================================RIGHT Buttons===========================================================
        root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan) \
            .grid(row=0, column=0, padx=2, pady=2)
        root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=deposit) \
            .grid(row=1, column=0, padx=2, pady=2)
        root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin) \
            .grid(row=2, column=0, padx=2, pady=2)
        root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement) \
            .grid(row=3, column=0, padx=2, pady=2)

        messagebox.showinfo("New PIN", "The Program will restart and you must log in again with the new pin.")
        root.destroy()
        os.system("python main.py")



    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, "\t             Welcome to GNB\n")
    root.txtReciept.insert(END, "\t    Enter new PIN at the end\n")
    root.txtReciept.focus_set()
    root.txtReciept.insert(END, "\t    your PIN will be updated\n")
    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew) \
        .grid(row=3, column=0, padx=2, pady=2)
    # ================================RIGHT Buttons===========================================================
    root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArR3 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=newPIN) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement) \
        .grid(row=3, column=0, padx=2, pady=2)

def back():
    for item in root.txtReciept.winfo_children():
        item.destroy()
    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, "\t\t ATM" + "\n\n")
    root.txtReciept.insert(END, "Withdraw Cash\t\t\t Loan" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Savings\t\t\t Deposit" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Balance\t\t\t Request New Pin" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Graphical Info\t\t\t Print Statement" + "\n\n\n\n\n")
    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=withdraw) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=reciept) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=balance) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=show_graph) \
        .grid(row=3, column=0, padx=2, pady=2)
    # ================================RIGHT Buttons===========================================================
    root.btnArR1 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=Loan) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArR2 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=deposit) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArR3 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=requestPin) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArR4 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=statement) \
        .grid(row=3, column=0, padx=2, pady=2)


# This gives value 0 to button 0 and it also puts value at the end of txtreciept
def btn0():
    value0 = 0
    root.txtReciept.insert(END, value0)
    return

# This gives value 1 to button 1 and it also puts value at the end of txtreciept
def btn1():
    value1 = 1
    root.txtReciept.insert(END, value1)


# This gives value 2 to button 2 and it also puts value at the end of txtreciept
def btn2():
    value2 = 2
    root.txtReciept.insert(END, value2)


# This gives value 3 to button 3 and it also puts value at the end of txtreciept
def btn3():
    value3 = 3
    root.txtReciept.insert(END, value3)


# This gives value 4 to button 4 and it also puts value at the end of txtreciept
def btn4():
    value4 = 4
    root.txtReciept.insert(END, value4)


# This gives value 5 to button 5 and it also puts value at the end of txtreciept
def btn5():
    value5 = 5
    root.txtReciept.insert(END, value5)


# This gives value 6 to button 6 and it also puts value at the end of txtreciept
def btn6():
    value6 = 6
    root.txtReciept.insert(END, value6)


# This gives value 7 to button 7 and it also puts value at the end of txtreciept
def btn7():
    value7 = 7
    root.txtReciept.insert(END, value7)


# This gives value 8 to button 8 and it also puts value at the end of txtreciept
def btn8():
    value8 = 8
    root.txtReciept.insert(END, value8)


# This gives value 9 to button 9 and it also puts value at the end of txtreciept
def btn9():
    value9 = 9
    root.txtReciept.insert(END, value9)


# ===============================Adding where TEXT comes:Screen===========================================
root.txtReciept = Text(topFrame2M, height=20, width=40, bd=12, font=("arial", 9, "bold"))
root.txtReciept.grid(row=0, column=0)

# ================================LEFT Buttons============================================================
root.btnArL1 = Button(topFrame2L,  width=145, height=65, state=DISABLED, image=leftARNew, command=withdraw)\
.grid(row=0, column=0, padx=2, pady=2)
root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept)\
.grid(row=1, column=0, padx=2, pady=2)
root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance)\
.grid(row=2, column=0, padx=2, pady=2)
root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew)\
.grid(row=3, column=0, padx=2, pady=2)
# ================================RIGHT Buttons===========================================================
root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan)\
.grid(row=0, column=0, padx=2, pady=2)
root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=deposit)\
.grid(row=1, column=0, padx=2, pady=2)
root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin)\
.grid(row=2, column=0, padx=2, pady=2)
root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew)\
.grid(row=3, column=0, padx=2, pady=2)
# ==============================PIN PAD===================================================================

root.btn1 = Button(topFrame1, width=145, height=65, state=NORMAL, image=oneNew, command=btn1)\
.grid(row=0, column=0, padx=2, pady=2)
root.btn2 = Button(topFrame1, width=145, height=65, state=NORMAL, image=twoNew, command=btn2)\
.grid(row=1, column=0, padx=2, pady=2)
root.btn3 = Button(topFrame1, width=145, height=65, state=NORMAL, image=threeNew, command=btn3)\
.grid(row=2, column=0, padx=2, pady=2)
root.btnPlain1 = Button(topFrame1, width=145, height=65, state=NORMAL, image=emptyNew)\
.grid(row=3, column=0, padx=2, pady=2)

root.btn4 = Button(topFrame1, width=145, height=65, state=NORMAL, image=fourNew, command=btn4)\
.grid(row=0, column=1, padx=2, pady=2)
root.btn5 = Button(topFrame1, width=145, height=65, state=NORMAL, image=fiveNew, command=btn5)\
.grid(row=1, column=1, padx=2, pady=2)
root.btn6 = Button(topFrame1, width=145, height=65, state=NORMAL, image=sixNew, command=btn6)\
.grid(row=2, column=1, padx=2, pady=2)
root.btnZero = Button(topFrame1, width=145, height=65, state=NORMAL, image=zeroNew, command=btn0)\
.grid(row=3, column=1, padx=2, pady=2)

root.btn7 = Button(topFrame1, width=145, height=65, state=NORMAL, image=sevenNew, command=btn7)\
.grid(row=0, column=2, padx=2, pady=2)
root.btn8 = Button(topFrame1, width=145, height=65, state=NORMAL, image=eightNew, command=btn8)\
.grid(row=1, column=2, padx=2, pady=2)
root.btn9 = Button(topFrame1, width=145, height=65, state=NORMAL, image=nineNew, command=btn9)\
.grid(row=2, column=2, padx=2, pady=2)
root.btnPlain2 = Button(topFrame1, width=145, height=65, state=NORMAL, image=emptyNew)\
.grid(row=3, column=2, padx=2, pady=2)
root.btnClear = Button(topFrame1, width=145, height=65, state=NORMAL, image=clearNew, command=Clear)\
.grid(row=0, column=3, padx=2, pady=2)
root.btnCancel = Button(topFrame1, width=145, height=65, state=NORMAL, image=cancelNew, command=Cancel_Transaction)\
.grid(row=1, column=3, padx=2, pady=2)
root.btnEnter = Button(topFrame1, width=145, height=65, state=NORMAL, image=enterNew, command=enter_Pin)\
.grid(row=2, column=3, padx=2, pady=2)
root.btnPlain3 = Button(topFrame1, width=145, height=65, state=NORMAL, image=rightARNew, command=back)\
.grid(row=3, column=3, padx=2, pady=2)


'''Here is where you call the main loop and to run the project.'''
root.mainloop()



