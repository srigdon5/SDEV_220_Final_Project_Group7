from tkinter import *
from tkinter import messagebox, simpledialog
import subprocess
import ast
from tkinter import PhotoImage
import os
from tkinter import ttk
import tkinter as tk


"""
Program: GUI_Checkout.py
Author: J.Swilling
Goal: Create a GUI for handling item returns within the "return" options in Dashboard/Accounts.py.

1. Significant constants:

2. The inputs are:
    - Item ID
    - User ID (Staff ID)
    - Branch
    - Return Date
    - Fees Option
    - Item Condition

3. Computations:

4. The outputs are:
    - Display reminders or fee charts based on specific conditions, such as unpaid fees or poor item conditions.
"""


root = Tk()
root.title('EVPL Management System - Return Item')
root.geometry('400x200+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file='assets\\images\\design.png')
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)

"""------------------------------------------------------------------------------------------"""

frame = Frame(root, width=397, highlightbackground="black", highlightthickness=3, height=188, bg='#fff')
frame.place(x=1, y=10)

"""-----------------------------------------ITEM ID----------------------------------------------"""


def validate_item_id(value):
    return value.isdigit()


item_label = Label(text="Item ID:", fg='black', bg='white', font=('Arial', 12))
item_label.place(x=40, y=50)

item_var = tk.StringVar()
item_var.set("Enter Item ID")

item_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
item_entry.place(x=140, y=37)
item_entry.insert(0, "Enter Item ID")

item_entry.bind("<FocusIn>", lambda event: item_entry.delete(0, tk.END) if item_entry.get() == 'Enter Item ID' else None)

item_entry.bind("<FocusOut>", lambda event: item_entry.insert(0, 'Enter a Item ID') if not item_entry.get() else None)

"""-----------------------------------------PATRON ID----------------------------------------------"""


def validate_patron_id(value):
    return value.isdigit()


patron_label = Label(text="Patron ID:", fg='black', bg='white', font=('Arial', 12))
patron_label.place(x=40, y=100)

patron_var = tk.StringVar()
patron_var.set("Enter Patron ID")

patron_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
patron_entry.place(x=140, y=87)
patron_entry.insert(0, "Enter Patron ID")

patron_entry.bind("<FocusIn>", lambda event: patron_entry.delete(0, tk.END) if patron_entry.get() == 'Enter Patron ID' else None)

patron_entry.bind("<FocusOut>", lambda event: patron_entry.insert(0, 'Enter Patron ID') if not patron_entry.get() else None)


"""-----------------------------------------RETURN/CANCEL----------------------------------------------"""


def return_button_click():
    item_value = item_entry.get()
    patron_value = patron_entry.get()

    if not validate_item_id(item_value):
        messagebox.showerror("Error", "Item ID must be valid integer.")
        return
    if not validate_patron_id(patron_value):
        messagebox.showerror("Error", "Patron ID must be valid integer.")
        return


remove_btn = Button(frame, width=10, pady=7, text='RETURN', bg='grey', fg='white', border=3,
                    command=return_button_click)

remove_btn.place(x=80, y=130)
"""----------------------------------------------------"""


def abortproc():
    root.destroy()


cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=230, y=130)
"""----------------------------------------------------"""
root.mainloop()
