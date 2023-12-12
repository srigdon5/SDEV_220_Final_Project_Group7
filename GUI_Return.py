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
root.geometry('400x400+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file='assets\\images\\design.png')
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)

"""------------------------------------------------------------------------------------------"""

frame = Frame(root, width=397, highlightbackground="black", highlightthickness=3, height=380, bg='#fff')
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
staff_var.set("Enter Item ID")

staff_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
staff_entry.place(x=140, y=87)
staff_entry.insert(0, "Enter Staff ID")

staff_entry.bind("<FocusIn>", lambda event: staff_entry.delete(0, tk.END))

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

"""-----------------------------------------FEES----------------------------------------------"""
fee_label = Label(text="Fees:", fg='black', bg='white', font=('Arial', 12))
fee_label.place(x=40, y=250)


fee_entry = ttk.Combobox(frame, values=["Paid", "Unpaid", "Waived"], width=30)
fee_entry.current(0)
fee_entry.place(x=140, y=237)
"""-----------------------------------------CONDITION----------------------------------------------"""
condition_label = Label(text="Condition:", fg='black', bg='white', font=('Arial', 12))
condition_label.place(x=40, y=300)

condition_entry = ttk.Combobox(frame, values=["Excellent", "Good", "Fair", "Poor"], width=30)
condition_entry.current(0)
condition_entry.place(x=140, y=287)
"""-----------------------------------------RETURN/CANCEL----------------------------------------------"""


def return_button_click():
    # Retrieve values from the Entry widgets
    item_value = item_entry.get()
    id_value = staff_entry.get()
    fees_option = fee_entry.get()
    condition = condition_entry.get()

    if not validate_item_id(item_value):
        messagebox.showerror("Error", "Item ID must be valid integer.")
        return
    if not validate_staff_id(id_value):
        messagebox.showerror("Error", "Staff ID must be valid integer.")
        return
    if fees_option == "Unpaid":
        reminder_message = "Caution: If unpaid, a separate bill must be sent."

        messagebox.showinfo("Unpaid Fees Reminder", reminder_message)
    if condition == "Poor":
        fee_chart_message = "Fee Chart for Poor Condition:\n" \
                            "1. Minor Damage - $10\n" \
                            "2. Moderate Damage - $20\n" \
                            "3. Severe Damage - $30"
        messagebox.showinfo("Poor Condition Fee Chart", fee_chart_message)


remove_btn = Button(frame, width=10, pady=7, text='RETURN', bg='grey', fg='white', border=3,
                    command=return_button_click)

remove_btn.place(x=80, y=330)
"""----------------------------------------------------"""


def abortproc():
    root.destroy()


cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=230, y=330)
"""----------------------------------------------------"""
root.mainloop()
