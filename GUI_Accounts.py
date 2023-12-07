from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast
import subprocess
import os
from tkinter import PhotoImage
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from library_back import Item, Patron, search_items_by_title, search_items_by_title_branch, Base, engine

"""
Program: GUI_Accounts.py
Author: J.Swilling
Goal: Create a GUI for a module that displays customer accounts that can be easily
 integrated for a Library management system.
 
1. Significant constants
   USERNAME = "username"
   ID = "ID"
   ACCOUNT_TYPE = "account_type"
   MAIN_BRANCH = "main_branch"
    
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
window.iconbitmap("assets\\images\\myIcon.ico")


# Create the tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

background = PhotoImage(file="assets\\images\\design.png")
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

"""----------------------------------GET CUSTOMER ITEMS---------------------------------------"""



# Placeholder function to fetch customer information by ID
def get_customer_info_by_id(user_id, Session):
    with Session() as session:
        try:
            patron = session.query(Patron).filter_by(patron_id=user_id).first()
            if patron:
                return {
                    'patron_id': patron.patron_id,
                    'name': patron.name,
                    'phone': patron.phone,
                    'account_type': patron.account_type,
                    'branch_id': patron.branch_id,
                    'limit_reached': patron.limit_reached
                }
            else:
                return {}  # Return an empty dictionary if no patron is found
        except SQLAlchemyError as e:
            print(f"Error fetching customer info: {e}")
            return {}


def get_customer_items(user_id, Session):
    with Session() as session:
        try:
            patron = session.query(Patron).filter_by(patron_id=user_id).first()
            if patron:
                return [
                    {'item_id': patron.item_id, 'fees': patron.fees}
                ] if patron.item_id else []
            else:
                return []  # Return an empty list if no patron is found
        except SQLAlchemyError as e:
            print(f"Error fetching customer items: {e}")
            return []


def search():
    user_id = user.get()

    # Check if the current content is the placeholder text
    if user_id == 'Enter a User ID':
        user_id = ''  # Set it to an empty string for searching

    if user_id:
        customer_info = get_customer_info_by_id(user_id, Session)
        customer_items = get_customer_items(user_id, Session)

        # Clear labels
        ID_label.config(text="ID:")
        User_label.config(text="User:")
        Phone_label.config(text="Phone:")
        Account_label.config(text="Account Type:")
        Branch_label.config(text="Main Branch:")
        Limit_label.config(text="Account Lock:")

        # Update labels with customer information
        if customer_info:
            ID_label.config(text=f"ID: {customer_info.get('patron_id', 'None')}")
            User_label.config(text=f"User: {customer_info.get('name', 'None')}")
            Phone_label.config(text=f"Phone: {customer_info.get('phone', 'None')}")
            Account_label.config(text=f"Account Type: {customer_info.get('account_type', 'None')}")
            Branch_label.config(text=f"Main Branch: {customer_info.get('branch_id', 'None')}")
            Limit_label.config(text=f"Account Lock: {customer_info.get('limit_reached', 'None')}")

        # Clear and update Listbox
        my_listbox.delete(0, END)
        if not customer_items:
            my_listbox.insert(END, "No items found for this user.")
        else:
            for item in customer_items:
                my_listbox.insert(END, f"Item ID: {item['item_id']}, Fees: {item['fees']}")

        
        user.delete(0, 'end')
        user.insert(0, 'Enter a User ID')


search_id = Button(frame, width=30, pady=7, text='Search', bg='grey', fg='white', border=3, command=search)
search_id.place(x=55, y=25)

"""------------------------------------CUSTOMER ID--------------------------------------"""
# create functions for a responsive placeholder text


def on_enter(e):
    name = user.get()
    if name == 'Enter a User ID':
        user.delete(0, 'end')
        user.insert(0, '')  # Clear the entry and move the insertion point to the beginning


def on_leave(e):
    name = user.get()
    if not name:  # Check if the user hasn't entered anything
        user.insert(0, 'Enter a User ID')


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

User_label = Label(text="User:", fg='black', bg='white', font=('Arial', 12))
User_label.place(x=140, y=265)

Phone_label = Label(text="Phone:", fg='black', bg='white', font=('Arial', 12))
Phone_label.place(x=140, y=315)

Account_label = Label(text="Account Type:", fg='black', bg='white', font=('Arial', 12))
Account_label.place(x=140, y=365)

Branch_label = Label(text="Main Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=140, y=415)

Limit_label = Label(text="Account Lock:", fg='black', bg='white', font=('Arial', 12))
Limit_label.place(x=140, y=465)

""""---------------------------------CUSTOMER ITEMS---------------------------------"""
# List box for customer's items
info_frame = Frame(width=500, highlightbackground="black", highlightthickness=1, height=250, bg="white")
my_scrollbar = Scrollbar(info_frame, orient=VERTICAL)

my_listbox = Listbox(info_frame, width=80, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)

# Configure scrollbar
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
info_frame.place(x=140, y=500)

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
img = PhotoImage(file='assets\\images\\books.png')
img_label = Label(image=img, bg='#f0f0f0')
img_label.place(x=750, y=220)

"""----------------------------------RETURN ITEM---------------------------------------- """


def returnitem():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Return.py')
    python_interpreter = 'C:\\Users\\JSwil\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'

    try:
        subprocess.run([python_interpreter, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


return_button = Button(frame, width=20, pady=7, text='Return', bg='grey', fg='white', border=3
                       , command=returnitem)

return_button.place(x=625, y=500)

"""----------------------------------BACK TO DASHBOARD---------------------------------------- """


def close_window():
    window.destroy()


# Function to open another program
def dashboard():
    close_window()  # Close the current window
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Dashboard.py')
    python_interpreter = 'C:\\Users\\JSwil\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'  # Replace with your Python interpreter path

    try:
        subprocess.run([python_interpreter, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


Button(frame, width=20, pady=7, text='Dashboard', bg='grey', fg='white', border=3,
       command=dashboard).place(x=800, y=500)

"""--------------------------------------------------------------------------------"""

# Start the Tkinter event loop to run the registration GUI
window.mainloop()
