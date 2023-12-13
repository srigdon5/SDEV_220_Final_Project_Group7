from tkinter import *
from tkinter import messagebox
import subprocess
import ast
from tkinter import PhotoImage, messagebox
import os
from tkinter import ttk
import tkinter as tk
from tkinter import Tk, Label, ttk, Entry, Button

"""
Program: GUI_Add.py
Author: J.Swilling
Goal: to add a submenu to the "add" option in Dashboard.py.
Description: This program creates a graphical user interface for adding items in the EVPL Management System.
The interface includes entry fields for Title, Author, ID Type, ID, Branch, Pages, Runtime, Date, and User ID.
Form validation ensures that the user provides valid inputs, and the ADD button triggers the addition functionality.
"""


root = Tk()
root.title('EVPL Management System - Add Item')
root.geometry('400x700+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file='assets\\images\\design.png')
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)


frame = Frame(root, width=397, highlightbackground="black", highlightthickness=3, height=680, bg='#fff')


frame.place(x=1, y=10)
"""-----------------------------------------TITLE----------------------------------------------"""


def validate_title(value):
    return len(value) <= 50


Title_label = Label(text="Title:", fg='black', bg='white', font=('Arial', 12))
Title_label.place(x=40, y=50)

title_var = tk.StringVar()
title_var.set("Add a Title")

title_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
title_entry.place(x=140, y=37)
title_entry.insert(0, "Add a Title")

title_entry.bind("<FocusIn>", lambda event: title_entry.delete(0, tk.END) if title_entry.get() == "Add a Title" else None)

title_entry.bind("<FocusOut>", lambda event: title_entry.insert(0, "Add a Title") if not title_entry.get() else None)


"""-----------------------------------------AUTHOR----------------------------------------------"""


def validate_author(value):
    return len(value) <= 50


Author_label = Label(text="Author:", fg='black', bg='white', font=('Arial', 12))
Author_label.place(x=40, y=100)

author_var = tk.StringVar()
author_var.set("Add author")

author_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
author_entry.place(x=140, y=87)
author_entry.insert(0, "Add author")

author_entry.bind("<FocusIn>", lambda event: author_entry.delete(0, tk.END) if author_entry.get() == "Add author" else None)

author_entry.bind("<FocusOut>", lambda event: author_entry.insert(0, "Add author") if not author_entry.get() else None)


"""-----------------------------------------GENRE----------------------------------------------"""
Genre_label = Label(text="Genre:", fg='black', bg='white', font=('Arial', 12))
Genre_label.place(x=40, y=150)


drop = ttk.Combobox(frame, values=["Action", "Comedy", "Horror", ""], width=30)
drop.current(0)
drop.place(x=140, y=137)

"""-----------------------------------------ID TYPE----------------------------------------------"""


def validate_id_type():
    selected_id_type = id_drop.get()
    if selected_id_type == "ISBN":
        entry_validation = frame.register(validate_isbn)
    elif selected_id_type == "ISAN":
        entry_validation = frame.register(validate_isan)
    else:
        return None

    id_entry.config(validate="key", validatecommand=(entry_validation, '%P'))


def validate_isbn(value):
    return len(value) <= 13 and value.isdigit()


def validate_isan(value):
    return len(value) <= 12 and value.isdigit()


ID_Type_label = Label(text="ID Type:", fg='black', bg='white', font=('Arial', 12))
ID_Type_label.place(x=40, y=200)


id_drop = ttk.Combobox(frame, values=["ISBN", "ISAN"], width=30)
id_drop.current(0)
id_drop.place(x=140, y=187)


"""-----------------------------------------ID----------------------------------------------"""
ID_label = Label(text="ID:", fg='black', bg='white', font=('Arial', 12))
ID_label.place(x=40, y=250)

id_var = tk.StringVar()
id_var.set('Enter Item ID')

id_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
id_entry.place(x=140, y=237)
id_entry.insert(0, 'Enter Item ID')

id_entry.bind("<FocusIn>", lambda event: id_entry.delete(0, tk.END) if id_entry.get() == 'Enter Item ID' else None)

id_entry.bind("<FocusOut>", lambda event: id_entry.insert(0, 'Enter Item ID') if not id_entry.get() else None)

"""-----------------------------------------BRANCH----------------------------------------------"""
Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=40, y=300)


drop = ttk.Combobox(frame, values=["North Branch", "South Branch", "East Branch", "West Branch", ""], width=30)
drop.current(0)
drop.place(x=140, y=287)
"""-----------------------------------------PAGES----------------------------------------------"""


def validate_pages(value):
    return value.isdigit()


page_label = Label(text="Page(s):", fg='black', bg='white', font=('Arial', 12))
page_label.place(x=40, y=350)

pages_var = tk.StringVar()
pages_var.set("# of pages")

pages_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
pages_entry.place(x=140, y=337)
pages_entry.insert(0, "# of pages")

pages_entry.bind("<FocusIn>", lambda event: pages_entry.delete(0, tk.END) if pages_entry.get() == '# of pages' else None)

pages_entry.bind("<FocusOut>", lambda event: pages_entry.insert(0, '# of pages') if not pages_entry.get() else None)

"""-----------------------------------------RUNTIME----------------------------------------------"""


def validate_runtime(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


run_label = Label(text="Runtime:", fg='black', bg='white', font=('Arial', 12))
run_label.place(x=40, y=400)

runtime_var = tk.StringVar()
runtime_var.set("Duration (hrs)")

runtime_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
runtime_entry.place(x=140, y=387)
runtime_entry.insert(0, "Duration (hrs)")

runtime_entry.bind("<FocusIn>", lambda event: runtime_entry.delete(0, tk.END) if runtime_entry.get() == 'Duration (hrs)' else None)

runtime_entry.bind("<FocusOut>", lambda event: runtime_entry.insert(0, 'Duration (hrs)') if not runtime_entry.get() else None)

"""-----------------------------------------DATE----------------------------------------------"""
date_label = tk.Label(root, text="Date:", fg='black', bg='white', font=('Arial', 12))
date_label.place(x=40, y=450)

date_var = tk.StringVar()

day_combobox = ttk.Combobox(root, values=[str(i).zfill(2) for i in range(1, 32)], width=5)
day_combobox.current(0)
day_combobox.place(x=140, y=450)

month_combobox = ttk.Combobox(root, values=[str(i).zfill(2) for i in range(1, 13)], width=5)
month_combobox.current(0)
month_combobox.place(x=200, y=450)

year_combobox = ttk.Combobox(root, values=[str(i) for i in range(2023, 2030)], width=5)
year_combobox.current(0)
year_combobox.place(x=260, y=450)


"""-----------------------------------------USER ID----------------------------------------------"""


def validate_user_id(value):
    return value.isdigit()


run_label = Label(text="User ID:", fg='black', bg='white', font=('Arial', 12))
run_label.place(x=40, y=500)

user_id_var = tk.StringVar()
user_id_var.set("Enter Staff ID")

user_id_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user_id_entry.place(x=140, y=487)
user_id_entry.insert(0, "Enter Staff ID")

user_id_entry.bind("<FocusIn>", lambda event: user_id_entry.delete(0, tk.END) if user_id_entry.get() == 'Enter Staff ID' else None)

user_id_entry.bind("<FocusOut>", lambda event: user_id_entry.insert(0, 'Enter Staff ID') if not user_id_entry.get() else None)

"""-----------------------------------------ADD/CANCEL----------------------------------------------"""


def add_button_click():
    # Retrieve values from the Entry widgets
    title_value = title_entry.get()
    author_value = author_entry.get()
    pages_value = pages_entry.get()
    runtime_value = runtime_entry.get()
    user_id_value = user_id_entry.get()
    day = day_combobox.get()
    month = month_combobox.get()
    year = year_combobox.get()

    selected_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    date_var.set(selected_date)

    # Perform ADD button functionality here
    if not validate_title(title_value):
        messagebox.showerror("Error", "Title must be 50 characters or less.")
        return
    if not validate_author(author_value):
        messagebox.showerror("Error", "Author must be 50 characters or less.")
        return
    if not validate_pages(pages_value):
        messagebox.showerror("Error", "Pages must be valid integer.")
        return
    if not validate_runtime(runtime_value):
        messagebox.showerror("Error", "Runtime must be a valid floating-point number.")
        return
    if not validate_user_id(user_id_value):
        messagebox.showerror("Error", "User ID must be valid integer.")
        return


add_btn = Button(frame, width=10, pady=7, text='ADD', bg='grey', fg='white', border=3, command=add_button_click)
add_btn.place(x=80, y=600)


def abortproc():
    root.destroy()


cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=230, y=600)
"""----------------------------------------------------"""
root.mainloop()
