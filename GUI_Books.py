from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast
import subprocess
import os
from tkinter import PhotoImage
from library_back import Item, Patron, search_books, get_genres, get_branch_names

"""
Program: GUI_Books.py
Author: J.Swilling
Goal: Create a GUI for a module that displays available books that can be easily
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
    comparison of text strings (Title/Desc) and Integers (IBSN/ISAN/Amount Due/DATE)
    
4. The outputs are
 ISBN/ISAN/Amount Due/DATE
"""

window = Tk()
window.title("EVPL Management System - Book Inventory")
window.geometry('1225x750+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
window.iconbitmap("assets\\images\\myIcon.ico")

background = PhotoImage(file="assets\\images\\design.png")
background_label = Label(window, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)

frame = Frame(width=250, highlightbackground="black", highlightthickness=3, height=80, bg="white")
frame.place(x=500, y=20)

heading = Label(frame, text='Library Inventory', fg='black', bg='white',
                font=('Microsoft YaHei UI Light', 16, 'bold'))
heading.place(x=30, y=18)

"""---------------------------------------------------------------------------"""
frame = Frame(window, width=1000, highlightbackground="black", highlightthickness=3, height=600, bg='#fff')
frame.place(x=110, y=120)

"""----------------------------------------TITLE----------------------------------------------------"""


def validate_title(value):
    return len(value) <= 300


Title_label = Label(text="Title:", fg='black', bg='white', font=('Arial', 12))
Title_label.place(x=140, y=218)


title_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
title_entry.place(x=90, y=95)


"""----------------------------------------AUTHOR----------------------------------------------------"""


def validate_author(value):
    return len(value) <= 50


Author_label = Label(text="Author:", fg='black', bg='white', font=('Arial', 12))
Author_label.place(x=140, y=265)


author_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
author_entry.place(x=90, y=143)


"""----------------------------------------GENRE DROPDOWN----------------------------------------------------"""
Genre_label = Label(text="Genre:", fg='black', bg='white', font=('Arial', 12))
Genre_label.place(x=140, y=315)

genre_list = get_genres()
genre_list.insert(0, "")
genre_drop = ttk.Combobox(frame, values=genre_list, width=30)

genre_drop.current(0)
genre_drop.place(x=90, y=192)

"""----------------------------------------ISBN----------------------------------------------------"""


def validate_id_type(value):
    return len(value) <= 13


ISBN_label = Label(text="ISBN:", fg='black', bg='white', font=('Arial', 12))
ISBN_label.place(x=140, y=365)


isbn_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
isbn_entry.place(x=90, y=242)


"""----------------------------------------BRANCH DROPDOWN----------------------------------------------------"""
Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=140, y=415)

branches = get_branch_names()
branches.insert(0, "")
branch_drop = ttk.Combobox(frame, values=branches, width=30)


branch_drop.current(0)
branch_drop.place(x=90, y=292)

""""---------------------------------SHOW FILTERED ITEMS---------------------------------"""
info_frame = Frame(width=500, highlightbackground="black", highlightthickness=1, height=250, bg="white")
info_frame.place(x=140, y=460)

my_scrollbar = Scrollbar(info_frame, orient=VERTICAL)
my_scrollbar_horizontal = Scrollbar(info_frame, orient=HORIZONTAL)
my_listbox = Listbox(info_frame, width=80, yscrollcommand=my_scrollbar.set, xscrollcommand=my_scrollbar_horizontal.set, selectmode=SINGLE)

my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_scrollbar_horizontal.config(command=my_listbox.xview)
my_scrollbar_horizontal.pack(side=BOTTOM, fill=X)

my_listbox.pack(pady=15)


def return_selected():
    for items in reversed(my_listbox.curselection()):
        my_listbox.delete(items)


def show_item_details(selected_item):
    # Create a popup window
    popup_window = Toplevel(window)
    popup_window.title("Item Details")
    popup_window.geometry('400x300')

    item_details = selected_item.split('|')

    for detail in item_details:
        Label(popup_window, text=detail.strip(), padx=10, pady=5).pack()


def on_item_single_click(event):
    selected_item_index = my_listbox.curselection()
    if selected_item_index:
        selected_item = my_listbox.get(selected_item_index[0])
        show_item_details(selected_item)


my_listbox.bind('<ButtonRelease-1>', on_item_single_click)

"""----------------------------------ITEM IMAGE---------------------------------------- """
img = PhotoImage(file='assets\\images\\books_small.png')
img_label = Label(image=img, bg='#f0f0f0')
img_label.place(x=750, y=200)


"""----------------------------------CHECKOUT ITEM(S)---------------------------------------- """


def checkoutitem():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Checkout.py')

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


return_button = Button(frame, width=20, pady=7, text='Checkout', bg='grey',
                       fg='white', border=3, command=checkoutitem)

return_button.place(x=625, y=500)
"""---------------------------------- SEARCH ---------------------------------------"""


def search_button_click():
    title_value = title_entry.get()
    author_value = author_entry.get()
    genre_value = genre_drop.get()
    isbn_value = isbn_entry.get()
    branch_value = branch_drop.current()

    # Validate inputs
    if not title_value.strip() and not author_value.strip() and not isbn_value.strip() and genre_value == "" and branch_value == "":
        messagebox.showerror("Error", "All fields cannot be empty.")
        return

    if title_value.strip() and not validate_title(title_value):
        messagebox.showerror("Error", "Title must be 300 characters or less.")
        return

    if author_value.strip() and not validate_author(author_value):
        messagebox.showerror("Error", "Author must be 50 characters or less.")
        return

    if isbn_value.strip() and not validate_id_type(isbn_value):
        messagebox.showerror("Error", "Valid ISBN must be 13 characters long.")
        return

    # Check if all fields are None, indicating that they are empty
    if all(field is None for field in (title_value, author_value, genre_value, isbn_value, branch_value)):
        messagebox.showerror("Error", "All fields cannot be empty.")
        return
    
    search_results = search_books(title=title_value, author=author_value, genre=genre_value, isbn=isbn_value, branch_id=branch_value)
    for item in search_results:
        my_listbox.destroy(0, END)
        my_listbox.insert(END, f"ID: {item[0]} | Title: {item[1]} | Author: {item[2]} | Medium: {item[3]} | Pages: {item[4]} | Branch: {item[5]} | Availability: {item[6]}")


search_id = Button(frame, width=30, pady=7, text='Search', bg='grey', fg='white', border=3, command=search_button_click)
search_id.place(x=55, y=25)

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
