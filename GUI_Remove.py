from tkinter import *
from tkinter import messagebox
import subprocess
import ast
from tkinter import PhotoImage
import os
from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry


"""
Program: GUI_Remove.py
Author: J.Swilling
Goal: to add a submenu to the "remove" option in Dashboard.py.
1. Significant constants
    - No significant constants defined in this section.

2. The inputs are
    - User input through the GUI, including:
        - Item ID
        - Staff ID
        - Branch selection
        - Date
        - Details
        - Fees selection

3. Computations:
    - Validation of user inputs:
        - Checking if Item ID is a valid integer.
        - Checking if Staff ID is a valid integer.
        - Checking if Details field does not exceed 100 characters.

4. The outputs are
    - Displayed through the GUI:
        - Feedback messages for validation errors.
        - If fees are set to "Unpaid," a reminder message is displayed about updating dues for the customer's account.
"""


root = Tk()
root.title('EVPL Management System - Remove Item')
root.geometry('400x700+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file='assets\\images\\design.png')
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)

"""------------------------------------------------------------------------------------------"""

frame = Frame(root, width=397, highlightbackground="black", highlightthickness=3, height=680, bg='#fff')
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

item_entry.bind("<FocusIn>", lambda event: item_entry.delete(0, tk.END))


"""-----------------------------------------STAFF ID----------------------------------------------"""


def validate_staff_id(value):
    return value.isdigit()


user_label = Label(text="User ID:", fg='black', bg='white', font=('Arial', 12))
user_label.place(x=40, y=100)

staff_var = tk.StringVar()
staff_var.set("Enter Staff ID")

id_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
id_entry.place(x=140, y=87)
id_entry.insert(0, "Enter Staff ID")

id_entry.bind("<FocusIn>", lambda event: id_entry.delete(0, tk.END))


"""-----------------------------------------BRANCH----------------------------------------------"""
Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=40, y=150)


drop = ttk.Combobox(frame, values=["North Branch", "South Branch", "East Branch", "West Branch", ""], width=30)
drop.current(0)
drop.place(x=140, y=137)

"""-----------------------------------------DATE----------------------------------------------"""

date_label = tk.Label(text="Date:", fg='black', bg='white', font=('Arial', 12))
date_label.place(x=40, y=200)


cal = DateEntry(frame, width=12, background='dark-blue', foreground='white', borderwidth=2, year=2023, month=12, day=7)
cal.place(x=140, y=187)

"""-----------------------------------------DETAILS----------------------------------------------"""


def validate_detail(value):
    return len(value) <= 100


detail_label = Label(text="Details:", fg='black', bg='white', font=('Arial', 12))
detail_label.place(x=40, y=250)


detail_entry = Text(frame, width=40, height=10, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
detail_entry.place(x=40, y=277)


"""-----------------------------------------FEES----------------------------------------------"""
fee_label = Label(text="Fees:", fg='black', bg='white', font=('Arial', 12))
fee_label.place(x=40, y=527)


fee_entry = ttk.Combobox(frame, values=["Paid", "Unpaid", "Waived"], width=30)
fee_entry.current(0)
fee_entry.place(x=120, y=518)
"""-----------------------------------------REMOVE/CANCEL----------------------------------------------"""


def remove_button_click():
    # Retrieve values from the Entry widgets
    item_value = item_entry.get()
    id_value = id_entry.get()
    detail_value = detail_entry.get("1.0", "end-1c")
    fees_option = fee_entry.get()

    if not validate_item_id(item_value):
        messagebox.showerror("Error", "Item ID must be valid integer.")
        return
    if not validate_staff_id(id_value):
        messagebox.showerror("Error", "Staff ID must be valid integer.")
        return
    if not validate_detail(detail_value):
        messagebox.showerror("Error", "(Details) field may not exceed 100 characters.")
        return
    if fees_option == "Unpaid":
        reminder_message = "Caution: Update dues for the customer's account! If unpaid, a separate bill must be sent."
        messagebox.showinfo("Unpaid Fees Reminder", reminder_message)


remove_btn = Button(frame, width=10, pady=7, text='REMOVE', bg='grey', fg='white', border=3,
                    command=remove_button_click)

remove_btn.place(x=80, y=600)
"""----------------------------------------------------"""


def abortproc():
    root.destroy()


cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=230, y=600)
"""----------------------------------------------------"""
root.mainloop()
