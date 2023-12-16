from tkinter import *
from tkinter import messagebox
import subprocess
import ast
from tkinter import PhotoImage, messagebox
import os
from tkinter import ttk
import tkinter as tk
from tkinter import Tk, Label, ttk, Entry, Button
from library_back import add_book, add_movie

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
root.geometry('400x585+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("assets\\images\\myIcon.ico")

background = PhotoImage(file='assets\\images\\design.png')
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)

frame = Frame(root, width=397, highlightbackground="black", highlightthickness=3, height=582, bg='#fff')

frame.place(x=1, y=10)
"""-----------------------------------------TITLE----------------------------------------------"""


def validate_title(value):
    return len(value) <= 50


Title_label = Label(text="Title:", fg='black', bg='white', font=('Arial', 12))
Title_label.place(x=40, y=50)


title_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
title_entry.place(x=140, y=37)


"""-----------------------------------------AUTHOR----------------------------------------------"""


def validate_author(value):
    return len(value) <= 50


Author_label = Label(text="Author:", fg='black', bg='white', font=('Arial', 12))
Author_label.place(x=40, y=100)


author_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
author_entry.place(x=140, y=87)


"""-----------------------------------------GENRE----------------------------------------------"""
genre_label = Label(text="Genre:", fg='black', bg='white', font=('Arial', 12))
genre_label.place(x=40, y=150)


genre_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
genre_entry.place(x=140, y=137)

"""-----------------------------------------ITEM_ID----------------------------------------------"""
id_label = Label(text="ISBN/ISAN:", fg='black', bg='white', font=('Arial', 12))
id_label.place(x=40, y=250)


id_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
id_entry.place(x=140, y=237)


"""-----------------------------------------BRANCH----------------------------------------------"""
Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=40, y=300)

branch_drop = ttk.Combobox(frame, values=["", "Central", "East", "West", "North Park", "Oaklyn",
                                          "Red Bank", "Stringtown", "West", "McCollough",
                                          "Washington Square-McCollough"], width=30)

branch_drop.current(0)
branch_drop.place(x=140, y=287)
"""-----------------------------------------PAGES----------------------------------------------"""


def validate_pages(value):
    return value.isdigit()


page_label = Label(text="Page(s):", fg='black', bg='white', font=('Arial', 12))
page_label.place(x=40, y=350)

pages_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
pages_entry.place(x=140, y=337)


"""-----------------------------------------RUNTIME----------------------------------------------"""


def validate_runtime(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


run_label = Label(text="Runtime:", fg='black', bg='white', font=('Arial', 12))
run_label.place(x=40, y=400)

runtime_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
runtime_entry.place(x=140, y=387)
"""-----------------------------------------MEDIUM-----------------------------------------------"""


medium_label = Label(text="Medium:", fg='black', bg='white', font=('Arial', 12))
medium_label.place(x=40, y=450)

medium = ttk.Combobox(frame, values=["", "paperback", "hard cover", "dvd", "blu-ray"], width=30)

medium.current(0)
medium.place(x=140, y=437)


"""-----------------------------------------ISBN/ISAN----------------------------------------------"""


def validate_isbn(value):
    return len(value) <= 13


def validate_isan(value):
    return len(value) <= 12


def validate_id_type(*args):
    selected_id_type = id_var.get()
    if selected_id_type == "ISBN":
        pages_entry.config(state='normal')  # Enable pages entry
        runtime_entry.config(state='disabled')  # Disable runtime entry
        medium['values'] = ["", "paperback", "hard cover"]
    elif selected_id_type == "ISAN":
        pages_entry.config(state='disabled')  # Disable pages entry
        runtime_entry.config(state='normal')  # Enable runtime entry
        medium['values'] = ["", "dvd", "blu-ray"]
    else:
        return None


ID_Type_label = Label(text="ISBN/ISAN:", fg='black', bg='white', font=('Arial', 12))
ID_Type_label.place(x=40, y=200)

id_var = tk.StringVar()
id_var.set("ISBN")  # Set the default value

id_drop = ttk.Combobox(frame, textvariable=id_var, values=["", "ISBN", "ISAN"], width=30)
id_drop.current(0)
id_drop.place(x=140, y=187)
selected_id_type = id_drop

# Bind the validate_id_type function to the ID Type variable
id_var.trace_add('write', validate_id_type)

"""-----------------------------------------ADD/CANCEL----------------------------------------------"""


def add_button_click():
    # Retrieve values from the Entry widgets
    title_value = title_entry.get()
    author_value = author_entry.get()
    genre_value = genre_entry.get()
    id_value = id_drop.grab_current()
    item_value = id_entry.get()
    branch_value = branch_drop.current()
    pages_value = pages_entry.get()
    runtime_value = runtime_entry.get()
    medium_value = medium.current()

    # Perform ADD button functionality here
    if not validate_title(title_value):
        messagebox.showerror("Error", "Title must be 50 characters or less.")
        return
    if id_value == "ISBN":
        if not validate_author(author_value):
            messagebox.showerror("Error", "Author must be 50 characters or less.")
            return
        if not validate_pages(pages_value):
            messagebox.showerror("Error", "Pages must be valid integer.")
            return
    if id_value == "ISAN":
        if not validate_runtime(runtime_value):
            messagebox.showerror("Error", "Runtime must be a valid floating-point number.")
            return
    
    #Calling the appropriate Add function
    if id_value == "ISBN":
        add_book(branch_value, item_value, title_value, genre_value, medium_value, pages_value, author_value)
        messagebox.showerror("Success", "Your book was added to the inventory.")
    else:
        add_movie(branch_value, item_value, title_value, genre_value, runtime_value, medium_value)
        messagebox.showerror("Success", "Your movie was added to the inventory.")

add_btn = Button(frame, width=10, pady=7, text='ADD', bg='grey', fg='white', border=3, command=add_button_click)
add_btn.place(x=80, y=500)


def abortproc():
    root.destroy()


cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=230, y=500)
"""----------------------------------------------------"""
root.mainloop()
