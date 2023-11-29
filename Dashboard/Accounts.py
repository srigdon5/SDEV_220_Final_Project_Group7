from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast
import subprocess
import ast
from tkinter import PhotoImage


"""
Program: Accounts.py
Author: J.Swilling
Goal: Create a GUI for a module that displays customer accounts that can be easily
 integrated for a Library management system.
 
1. Significant constants
    USERNAME
    ID
    ACCOUNT_TYPE
    MAIN_BRANCH
    
2. The inputs are
    CUSTOMER_ID
    RETURN_ITEM
    DASHBOARD
    
3. Computations:
    comparison of text strings (Title/Desc) and Integers (IBSN/IASN/Amount Due/DATE)
    
4. The outputs are
 ISBN/ISAN/Amount Due/DATE
"""

# Create the main registration window
window = Tk()
window.title("EVPL Management System - Customer Accounts")
window.geometry('1225x750+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
window.iconbitmap("myIcon.ico")


background = PhotoImage(file="design.png")
background_label = Label(window, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)


# Create a frame for labels and input fields
frame = Frame(width=250, highlightbackground="black", highlightthickness=3, height=80, bg="white")
frame.place(x=500, y=20)

heading = Label(frame, text='Customer Accounts', fg='black', bg='white',
                font=('Microsoft YaHei UI Light', 16, 'bold'))

heading.place(x=20, y=18)

"""---------------------------------------------------------------------------------"""
frame = Frame(window, width=1000, highlightbackground="black", highlightthickness=3, height=600, bg='#fff')
frame.place(x=110, y=120)

"""----------------------------------USERNAME---------------------------------------"""


username = Button(frame, width=30, pady=7, text='Search', bg='grey', fg='white', border=3,)
username.place(x=55, y=25)


"""------------------------------------CUSTOMER ID--------------------------------------"""
# create functions for a responsive placeholder text


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Enter ID')


# creates field for username
user = Entry(frame, width=25, fg='black', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=60, y=95)
user.insert(0, "Enter a User ID")

# bind text field 'Enter ID' to be accessed in function above
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

"""----------------------------------CUSTOMER INFORMATION---------------------------"""
# labels for customer information
ID_label = Label(text="ID:", fg='black', bg='white', font=('Arial', 12))
ID_label.place(x=140, y=218)

Branch_label = Label(text="User:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=140, y=265)

Phone_label = Label(text="Phone:", fg='black', bg='white', font=('Arial', 12))
Phone_label.place(x=140, y=315)

Account_label = Label(text="Account Type:", fg='black', bg='white', font=('Arial', 12))
Account_label.place(x=140, y=365)

Checkout_label = Label(text="Main Branch:", fg='black', bg='white', font=('Arial', 12))
Checkout_label.place(x=140, y=415)

""""---------------------------------CUSTOMER ITEMS---------------------------------"""
# List box for customer's items
info_frame = Frame(width=500, highlightbackground="black", highlightthickness=1, height=250, bg="white")
my_scrollbar = Scrollbar(info_frame, orient=VERTICAL)

my_listbox = Listbox(info_frame, width=80, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)

# Configure scrollbar
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
info_frame.place(x=140, y=450)

my_listbox.pack(pady=15)


# Add item to listbox
my_listbox.insert(END, 'ITEM_ID')


# Add list to listbox
my_list = ['ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID','ITEM_ID']

# Iterate through and insert items from the list
for item in my_list:
    my_listbox.insert(END, item)


def return_selected():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)


"""----------------------------------ITEM TITLE-------------------------------------"""
item_title = Label(frame, width=39, pady=7, text='Item Title', bg='black', fg='white', border=0,)
item_title.place(x=650, y=25)


"""----------------------------------ITEM IMAGE---------------------------------------- """
img = PhotoImage(file='books.png')
img_label = Label(image=img, bg='#f0f0f0')
img_label.place(x=750, y=220)

"""----------------------------------RETURN ITEM---------------------------------------- """
return_button = Button(frame, width=20, pady=7, text='Return Item(s)', bg='grey', fg='white', border=3
                       , command=return_selected)

return_button.place(x=625, y=500)

"""----------------------------------BACK TO DASHBOARD---------------------------------------- """


def close_window():
    window.destroy()


# Function to open another program
def dashboard():
    close_window()  # Close the current window
    subprocess.Popen(['python', 'Dashboard_GUI.py'])


Button(frame, width=20, pady=7, text='Dashboard', bg='grey', fg='white', border=3,
       command=dashboard).place(x=800, y=500)

"""--------------------------------------------------------------------------------"""

# Start the Tkinter event loop to run the registration GUI
window.mainloop()
