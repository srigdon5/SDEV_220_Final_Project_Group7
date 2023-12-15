from tkinter import *
from tkinter import messagebox
import subprocess
import ast
from tkinter import PhotoImage, messagebox
import os
from tkinter import ttk
import tkinter as tk
from tkinter import Tk, Label, ttk, Entry, Button
from library_back import Item, Patron, add_patron

"""
Program: GUI_Patron.py
Author: J.Swilling
Goal: to add a submenu to the "Add Account" option in Accounts.py.
Description: This program creates a graphical user interface for adding Patrons to the EVPL Management System.
The interface includes entry fields for Patron ID, Branch ID, First/Last Name, Phone, Account type, Limit, Date, and Fees.
Form validation ensures that the user provides valid inputs, and the ADD button triggers the additional functionality for db.
"""


root = Tk()
root.title('EVPL Management System - Add Patron')
root.geometry('400x600+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file='assets\\images\\design.png')
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)


frame = Frame(root, width=397, highlightbackground="black", highlightthickness=3, height=620, bg='#fff')


frame.place(x=1, y=10)
"""-----------------------------------------Patron ID----------------------------------------------"""


def validate_id(value):
    return value.isdigit()


id_label = Label(text="Patron ID:", fg='black', bg='white', font=('Arial', 12))
id_label.place(x=40, y=50)

id_var = tk.StringVar()
id_var.set("Add Patron ID")

id_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
id_entry.place(x=145, y=37)
id_entry.insert(0, "Add Patron ID")

id_entry.bind("<FocusIn>", lambda event: id_entry.delete(0, tk.END) if id_entry.get() == "Add Patron ID" else None)

id_entry.bind("<FocusOut>", lambda event: id_entry.insert(0, "Add Patron ID") if not id_entry.get() else None)


"""-----------------------------------------BRANCH----------------------------------------------"""

Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=40, y=100)


branch_name = ttk.Combobox(frame, values=["Central Branch", "East Branch", "McCollough Branch", "North Park Branch", "Oaklyn Branch", "Red Bank Branch", "Stringtown Branch", "West Branch", "Washington Square-McCollough Branch"], width=30)
branch_name.current(0)
branch_name.place(x=145, y=87)


"""----------------------------------First_Name---------------------------------------"""
def validate_name(value):
    return len(value) <= 30

fname_label = Label(text="First Name:", fg='black', bg='white', font=('Arial', 12))
fname_label.place(x=40, y=150)

fname_var = tk.StringVar()
fname_var.set('First Name')

fname_entry = Entry(frame, width=25, fg='black', border=1, bg='white', font=('Microsoft Yahei UI Light', 11))
fname_entry.place(x=145, y=137)
fname_entry.insert(0, 'First Name')

fname_entry.bind("<FocusIn>", lambda event: fname_entry.delete(0, tk.END) if fname_entry.get() == 'First Name' else None)

fname_entry.bind("<FocusOut>", lambda event: fname_entry.insert(0, 'First Name') if not fname_entry.get() else None)

"""-----------------------------------------Last Name----------------------------------------------"""

lname_label = Label(text="Last Name:", fg='black', bg='white', font=('Arial', 12))
lname_label.place(x=40, y=200)

lname_var = tk.StringVar()
lname_var.set('Last Name')

lname_entry = Entry(frame, width=25, fg='black', border=1, bg='white', font=('Microsoft Yahei UI Light', 11))
lname_entry.place(x=145, y=187)
lname_entry.insert(0, 'Last Name')

lname_entry.bind("<FocusIn>", lambda event: lname_entry.delete(0, tk.END) if lname_entry.get() == 'Last Name' else None)

lname_entry.bind("<FocusOut>", lambda event: lname_entry.insert(0, 'Last Name') if not lname_entry.get() else None)



"""-----------------------------------------Phone Number----------------------------------------------"""
def validate_phone(value):
    dot_count = value.count('.')

    digits = value.replace('.', '')
    
    if len(digits) == 10 and dot_count == 2:
        return True
    else:
        return False
    

phone_label = Label(text="Phone:", fg='black', bg='white', font=('Arial', 12))
phone_label.place(x=40, y=250)

phone_var = tk.StringVar()
phone_var.set('Phone Number')

phone_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
phone_entry.place(x=145, y=237)
phone_entry.insert(0, 'Phone Number (xxx.xxx.xxxx)')

phone_entry.bind("<FocusIn>", lambda event: phone_entry.delete(0, tk.END) if phone_entry.get() == 'Phone Number' else None)

phone_entry.bind("<FocusOut>", lambda event: phone_entry.insert(0, 'Phone Number') if not phone_entry.get() else None)

"""-----------------------------------------Account Type----------------------------------------------"""

acct_label = Label(text="Account Type:", fg='black', bg='white', font=('Arial', 12))
acct_label.place(x=40, y=300)


account = ttk.Combobox(frame, values=["Adult", "Child"], width=30)
account.current(0)
account.place(x=145, y=287)
"""-----------------------------------------Limit----------------------------------------------"""

limit_label = Label(text="Limit:", fg='black', bg='white', font=('Arial', 12))
limit_label.place(x=40, y=350)


drop = ttk.Combobox(frame, values=["0/3", "1/3", "2/3", "3/3", ""], width=30)
drop.current(0)
drop.place(x=145, y=337)


"""-----------------------------------------DATE----------------------------------------------"""

date_label = tk.Label(root, text="Date:", fg='black', bg='white', font=('Arial', 12))
date_label.place(x=40, y=400)

date_var = tk.StringVar()

day_combobox = ttk.Combobox(root, values=[str(i).zfill(2) for i in range(1, 32)], width=5)
day_combobox.current(0)
day_combobox.place(x=145, y=400)

month_combobox = ttk.Combobox(root, values=[str(i).zfill(2) for i in range(1, 13)], width=5)
month_combobox.current(0)
month_combobox.place(x=205, y=400)

year_combobox = ttk.Combobox(root, values=[str(i) for i in range(2023, 2030)], width=5)
year_combobox.current(0)
year_combobox.place(x=265, y=400)

"""-----------------------------------------ADD/CANCEL----------------------------------------------"""

def add_button_click():
    # Retrieve values from the Entry widgets
    fname_value = fname_entry.get()
    lname_value = lname_entry.get()
    patron_name = str(fname_value + " " + lname_value)
    phone_value = phone_entry.get()
    day = day_combobox.get()
    month = month_combobox.get()
    year = year_combobox.get()
    account_type = account.get()
    branch_id = branch_name.current()
    branch_id += 1

    selected_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    date_var.set(selected_date)

    # Perform ADD button functionality here
    if not validate_name(fname_value):
        messagebox.showerror("Error", "First name must be 30 characters or less.")
        return
    if not validate_name(lname_value):
        messagebox.showerror("Error", "Last name must be 30 characters or less.")
        return
    if not validate_phone(phone_value):
        messagebox.showerror("Error", "Phone number must be a 10-digit numeric value following the example given.")
        return

    add_patron(branch_id, patron_name, phone_value, account_type)

    messagebox.showinfo("Success", "Information added to the database successfully.")
    
add_btn = Button(frame, width=10, pady=7, text='ADD', bg='grey', fg='white', border=3, command=add_button_click)
add_btn.place(x=80, y=520)


def abortproc():
    root.destroy()


cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=230, y=520)
"""----------------------------------------------------"""
root.mainloop()