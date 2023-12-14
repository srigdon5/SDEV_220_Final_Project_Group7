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
from library_back import Item, Patron, get_patron_by_id, search_items_by_title, search_items_by_title_branch, Base, engine

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


window = Tk()
window.title("EVPL Management System - Customer Accounts")
window.geometry('1225x750+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
window.iconbitmap("assets\\images\\myIcon.ico")



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

background = PhotoImage(file="assets\\images\\design.png")
background_label = Label(window, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)



frame = Frame(width=250, highlightbackground="black", highlightthickness=3, height=80, bg="white")
frame.place(x=500, y=20)

heading = Label(frame, text='Customer Accounts', fg='black', bg='white',
                font=('Microsoft YaHei UI Light', 16, 'bold'))
heading.place(x=20, y=18)

"""---------------------------------------------------------------------------------"""
frame = Frame(window, width=1000, highlightbackground="black", highlightthickness=3, height=600, bg='#fff')
frame.place(x=110, y=120)



"""------------------------------------CUSTOMER ID--------------------------------------"""



def validate_customer_id(value):
    return value.isdigit()


user_var = tk.StringVar()
user_var.set('Enter a User ID')

customer_entry = Entry(frame, width=25, fg='black', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
customer_entry.place(x=60, y=95)
customer_entry.insert(0, 'Enter a User ID')

customer_entry.bind("<FocusIn>", lambda event: customer_entry.delete(0, tk.END) if customer_entry.get() == 'Enter a User ID' else None)

customer_entry.bind("<FocusOut>", lambda event: customer_entry.insert(0, 'Enter a User ID') if not customer_entry.get() else None)

"""----------------------------------SEARCH---------------------------------------"""
def search():
    user_id = customer_entry.get()
    customer_value = customer_entry.get()

    if not validate_customer_id(customer_value):
        messagebox.showerror("Error", "Customer ID must be valid integer.")
        return

    # Check if the current content is the placeholder text
    if user_id == 'Enter a User ID':
        user_id = ''  # Set it to an empty string for searching

    if user_id:
        customer_info = get_patron_by_id(user_id)
        
        if customer_info:
            User_label.config(text=f"User: {customer_info.get('name', 'None')}")
            Phone_label.config(text=f"Phone: {customer_info.get('phone', 'None')}")
            Account_label.config(text=f"Account Type: {customer_info.get('account_type', 'None')}")
            Branch_label.config(text=f"Main Branch: {customer_info.get('branch_name', 'None')}")
            Limit_label.config(text=f"Account Lock: {customer_info.get('limit_reached', 'None')}")
        else:
            messagebox.showinfo("Info", "No information found for this user.")

        # Clear labels
        ID_label.config(text="ID:")
        User_label.config(text="User:")
        Phone_label.config(text="Phone:")
        Account_label.config(text="Account Type:")
        Branch_label.config(text="Main Branch:")
        Limit_label.config(text="Account Lock:")

        # Update labels with customer information
        if customer_info:
            User_label.config(text=f"User: {customer_info.get('name', 'None')}")
            Phone_label.config(text=f"Phone: {customer_info.get('phone', 'None')}")
            Account_label.config(text=f"Account Type: {customer_info.get('account_type', 'None')}")
            Branch_label.config(text=f"Main Branch: {customer_info.get('branch_name', 'None')}")
            Limit_label.config(text=f"Account Lock: {customer_info.get('limit_reached', 'None')}")

        # Clear and update Listbox
        my_listbox.delete(0, END)
        if not customer_items:
            my_listbox.insert(END, "No items found for this user.")
        else:
            for inventory in customer_items:
                my_listbox.insert(END, f"Item ID: {inventory['item_id']}, Fees: {inventory['fees']}")

        customer_entry.delete(0, 'end')
        customer_entry.insert(0, 'Enter a User ID')


search_id = Button(frame, width=20, pady=7, text='Search', bg='grey', fg='white', border=3, command=search)
search_id.place(x=65, y=25)

"""----------------------------------ADD PATRON---------------------------------------"""
def patron(): 
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Patron.py')

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")



patron_add = Button(frame, width=20, pady=7, text='Add Account', bg='grey', fg='white', border=3, command=patron)
patron_add.place(x=260, y=25)

"""----------------------------------CUSTOMER INFORMATION---------------------------"""

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

info_frame = Frame(width=500, highlightbackground="black", highlightthickness=1, height=250, bg="white")
my_scrollbar = Scrollbar(info_frame, orient=VERTICAL)

my_listbox = Listbox(info_frame, width=80, yscrollcommand=my_scrollbar.set, selectmode=SINGLE)


my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
info_frame.place(x=140, y=500)

my_listbox.pack(pady=15)



my_listbox.insert(END, 'ITEM_ID')



my_list = ['ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID',
           'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID']


for item in my_list:
    my_listbox.insert(END, item)


def return_selected():
    for select in reversed(my_listbox.curselection()):
        my_listbox.delete(select)


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

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


return_button = Button(frame, width=20, pady=7, text='Return', bg='grey', fg='white', border=3,
                       command=returnitem)

return_button.place(x=625, y=500)

"""----------------------------------BACK TO DASHBOARD---------------------------------------- """


def close_window():
    window.destroy()



def dashboard():
    close_window()  
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Dashboard.py')

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


Button(frame, width=20, pady=7, text='Dashboard', bg='grey', fg='white', border=3,
       command=dashboard).place(x=800, y=500)

"""--------------------------------------------------------------------------------"""


window.mainloop()
