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
root.geometry('400x465+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("assets\\images\\myIcon.ico")

background = PhotoImage(file='assets\\images\\design.png')
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)

frame = Frame(root, width=397, highlightbackground="black", highlightthickness=3, height=452, bg='#fff')

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

title_entry.bind("<FocusIn>",
                 lambda event: title_entry.delete(0, tk.END) if title_entry.get() == "Add a Title" else None)

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

author_entry.bind("<FocusIn>",
                  lambda event: author_entry.delete(0, tk.END) if author_entry.get() == "Add author" else None)

author_entry.bind("<FocusOut>", lambda event: author_entry.insert(0, "Add author") if not author_entry.get() else None)

"""-----------------------------------------GENRE----------------------------------------------"""
genre_label = Label(text="Genre:", fg='black', bg='white', font=('Arial', 12))
genre_label.place(x=40, y=150)

genre_var = tk.StringVar()
genre_var.set("Add genre")

genre_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
genre_entry.place(x=140, y=137)
genre_entry.insert(0, "Add genre")

genre_entry.bind("<FocusIn>", lambda event: genre_entry.delete(0, tk.END) if genre_entry.get() == "Add genre" else None)

genre_entry.bind("<FocusOut>", lambda event: genre_entry.insert(0, "Add genre") if not genre_entry.get() else None)

"""-----------------------------------------BRANCH----------------------------------------------"""
Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=40, y=250)

branch_drop = ttk.Combobox(frame, values=["", "Central", "East", "West", "North Park", "Oaklyn",
                                          "Red Bank", "Stringtown", "West", "McCollough",
                                          "Washington Square-McCollough"], width=30)

branch_drop.current(0)
branch_drop.place(x=140, y=237)
"""-----------------------------------------PAGES----------------------------------------------"""


def validate_pages(value):
    return value.isdigit()


page_label = Label(text="Page(s):", fg='black', bg='white', font=('Arial', 12))
page_label.place(x=40, y=300)

pages_var = tk.StringVar()
pages_var.set("# of pages")

pages_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
pages_entry.place(x=140, y=287)
pages_entry.insert(0, "# of pages")

pages_entry.bind("<FocusIn>",
                 lambda event: pages_entry.delete(0, tk.END) if pages_entry.get() == '# of pages' else None)

pages_entry.bind("<FocusOut>", lambda event: pages_entry.insert(0, '# of pages') if not pages_entry.get() else None)

"""-----------------------------------------RUNTIME----------------------------------------------"""


def validate_runtime(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


run_label = Label(text="Runtime:", fg='black', bg='white', font=('Arial', 12))
run_label.place(x=40, y=350)

runtime_var = tk.StringVar()
runtime_var.set("Duration (hrs)")

runtime_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
runtime_entry.place(x=140, y=337)
runtime_entry.insert(0, "Duration (hrs)")

runtime_entry.bind("<FocusIn>",
                   lambda event: runtime_entry.delete(0, tk.END) if runtime_entry.get() == 'Duration (hrs)' else None)

runtime_entry.bind("<FocusOut>",
                   lambda event: runtime_entry.insert(0, 'Duration (hrs)') if not runtime_entry.get() else None)

"""-----------------------------------------ID TYPE----------------------------------------------"""


def validate_isbn(value):
    return len(value) <= 13 and value.isdigit()


def validate_isan(value):
    return len(value) <= 12 and value.isdigit()


def validate_id_type(*args):
    selected_id_type = id_var.get()
    if selected_id_type == "ISBN":
        pages_entry.config(state='normal')  # Enable pages entry
        runtime_entry.config(state='disabled')  # Disable runtime entry
    elif selected_id_type == "ISAN":
        pages_entry.config(state='disabled')  # Disable pages entry
        runtime_entry.config(state='normal')  # Enable runtime entry
    else:
        return None


ID_Type_label = Label(text="ID Type:", fg='black', bg='white', font=('Arial', 12))
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
    branch_value = branch_drop.grab_current()
    pages_value = pages_entry.get()
    runtime_value = runtime_entry.get()

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
    if not validate_id_type(id_value):
        messagebox.showerror("Error", "User ID must be valid integer.")
        return
    
    #Calling the appropriate Add function
    if id_value == "ISBN":
        add_book()

add_btn = Button(frame, width=10, pady=7, text='ADD', bg='grey', fg='white', border=3, command=add_button_click)
add_btn.place(x=80, y=400)


def abortproc():
    root.destroy()


cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=230, y=400)
"""----------------------------------------------------"""
root.mainloop()
