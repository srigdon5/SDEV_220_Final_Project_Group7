from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import subprocess
import ast
from tkinter import PhotoImage
import os
from tkinter import ttk
import tkinter as tk
from library_back import Item, Patron, get_patron_by_id, add_fee, pay_fee
from library_back import Base, engine

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
root.title('EVPL Management System - Manage Fees')
root.geometry('400x265+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file='assets\\images\\design.png')
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)

"""------------------------------------------------------------------------------------------"""

frame = Frame(root, width=397, highlightbackground="black", highlightthickness=3, height=250, bg='#fff')
frame.place(x=1, y=10)

"""-----------------------------------------FEE AMOUNT----------------------------------------------"""


def validate_fee(value):
    dot_count = value.count('.')
    if dot_count <= 1 and value.replace('.', '', 1).isdigit():
        return True
    return False


fee_label = Label(text="Fee Amount:", fg='black', bg='white', font=('Arial', 12))
fee_label.place(x=40, y=50)

fee_var = tk.StringVar()
fee_var.set('$0.00')

fee_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
fee_entry.place(x=140, y=37)
fee_entry.insert(0, '$0.00')

fee_entry.bind("<FocusIn>", lambda event: fee_entry.delete(0, tk.END) if fee_entry.get() == '$0.00' else None)

fee_entry.bind("<FocusOut>", lambda event: fee_entry.insert(0, '$0.00') if not fee_entry.get() else None)
"""-----------------------------------------PATRON ID----------------------------------------------"""


def validate_patron_id(value):
    return value.isdigit()


patron_label = Label(text="Patron ID:", fg='black', bg='white', font=('Arial', 12))
patron_label.place(x=40, y=100)


patron_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
patron_entry.place(x=140, y=87)


"""-----------------------------------------PAY_FEE----------------------------------------------"""


def pay_button_click():
    fee_value = fee_entry.get()
    patron_value = patron_entry.get()

    if not validate_fee(fee_value):
        messagebox.showerror("Error", "Item ID must be valid integer.")
        return
    if not validate_patron_id(patron_value):
        messagebox.showerror("Error", "Customer ID must be valid integer.")
        return

    pay_fee(patron_value, fee_value)

    messagebox.showinfo("Success", "The payment was made towards the balance")

pay_btn = Button(frame, width=10, pady=7, text='PAY', bg='grey', fg='white', border=3, command=pay_button_click)

pay_btn.place(x=50, y=160)
"""-----------------------------------------ADD_FEE----------------------------------------------"""


def add_button_click():
    fee_value = fee_entry.get()
    patron_value = patron_entry.get()

    if not validate_fee(fee_value):
        messagebox.showerror("Error", "Fee amount must be valid integer.")
        return
    if not validate_patron_id(patron_value):
        messagebox.showerror("Error", "Customer ID must be valid integer.")
        return
    
    add_fee(patron_value, fee_value)

    messagebox.showinfo("Success", "The fee has been added to their account")

add_btn = Button(frame, width=10, pady=7, text='ADD', bg='grey', fg='white', border=3, command=add_button_click)

add_btn.place(x=155, y=160)

"""-----------------------------------------CANCEL----------------------------------------------"""


def abortproc():
    root.destroy()


cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=260, y=160)
"""----------------------------------------------------"""
root.mainloop()
