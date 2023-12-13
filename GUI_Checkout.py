from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import subprocess
import ast
from tkinter import PhotoImage
import os
from tkinter import ttk
import tkinter as tk



"""
Program: GUI_Checkout.py
Author: J.Swilling
Goal: Implement a GUI for checking out items in the Books/Movies section.
1. Constants:
    - None mentioned explicitly in the code.
2. Inputs:
    - Item ID
    - Customer ID
3. Computations:
    - Validation of item ID and customer ID.
    - Checking the current checkout count and determining eligibility.
4. Outputs:
    - Messages indicating successful checkout or checkout cancellation.
"""


root = Tk()
root.title('EVPL Management System - Checkout Item')
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
item_var.set('Enter Item ID')

item_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
item_entry.place(x=140, y=37)
item_entry.insert(0, 'Enter Item ID')

item_entry.bind("<FocusIn>", lambda event: item_entry.delete(0, tk.END) if item_entry.get() == 'Enter Item ID' else None)

item_entry.bind("<FocusOut>", lambda event: item_entry.insert(0, 'Enter Item ID') if not item_entry.get() else None)
"""-----------------------------------------CUSTOMER ID----------------------------------------------"""


def validate_customer_id(value):
    return value.isdigit()


checkout_count = 0

user_label = Label(text="User ID:", fg='black', bg='white', font=('Arial', 12))
user_label.place(x=40, y=100)

customer_var = tk.StringVar()
customer_var.set("Enter Customer ID")

customer_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
customer_entry.place(x=140, y=87)
customer_entry.insert(0, "Enter Customer ID")

customer_entry.bind("<FocusIn>", lambda event: customer_entry.delete(0, tk.END) if customer_entry.get() == 'Enter Customer ID' else None)

customer_entry.bind("<FocusOut>", lambda event: customer_entry.insert(0, 'Enter Customer ID') if not customer_entry.get() else None)

"""-----------------------------------------BRANCH----------------------------------------------"""
Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=40, y=150)


drop = ttk.Combobox(frame, values=["North Branch", "South Branch", "East Branch", "West Branch", ""], width=30)
drop.current(0)
drop.place(x=140, y=137)

"""-----------------------------------------DATE----------------------------------------------"""
date_label = tk.Label(root, text="Date:", fg='black', bg='white', font=('Arial', 12))
date_label.place(x=40, y=200)

date_var = tk.StringVar()

# Comboboxes for day, month, and year
day_combobox = ttk.Combobox(root, values=[str(i).zfill(2) for i in range(1, 32)], width=5)
day_combobox.current(0)
day_combobox.place(x=140, y=200)

month_combobox = ttk.Combobox(root, values=[str(i).zfill(2) for i in range(1, 13)], width=5)
month_combobox.current(0)
month_combobox.place(x=200, y=200)

year_combobox = ttk.Combobox(root, values=[str(i) for i in range(2023, 2030)], width=5)
year_combobox.current(0)
year_combobox.place(x=260, y=200)




"""-----------------------------------------CHECKOUT/CANCEL----------------------------------------------"""


def checkout_button_click():
    global checkout_count
    item_value = item_entry.get()
    customer_value = customer_entry.get()

    if not validate_item_id(item_value):
        messagebox.showerror("Error", "Item ID must be valid integer.")
        return
    if not validate_customer_id(customer_value):
        messagebox.showerror("Error", "Customer ID must be valid integer.")
        return

    checkout_count = simpledialog.askinteger("Checkout Count", "Please enter your current checkout count (1, 2, or 3):",
                                             minvalue=1, maxvalue=3)

    if checkout_count is not None:
        if checkout_count == 3:
            # If the checkout count is 3, cancel the checkout
            messagebox.showwarning("Checkout Limit Exceeded",
                                   "Customer has reached a checkout limit of 3. Checkout canceled.")
        else:
            # If the checkout count is less than 3, checkout is successful
            messagebox.showinfo("Checkout Successful", f"Successfully checked out. {checkout_count}/3")


remove_btn = Button(frame, width=10, pady=7, text='CHECKOUT', bg='grey', fg='white', border=3,
                    command=checkout_button_click)

remove_btn.place(x=80, y=300)
"""----------------------------------------------------"""


def abortproc():
    root.destroy()


cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=230, y=300)
"""----------------------------------------------------"""
root.mainloop()
