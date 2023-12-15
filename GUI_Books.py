from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast
import subprocess
import os
from tkinter import PhotoImage
from library_back import Item, Patron, search_items_by_title, get_branch_names

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
    return len(value) <= 50


Title_label = Label(text="Title:", fg='black', bg='white', font=('Arial', 12))
Title_label.place(x=140, y=218)

title_var = tk.StringVar()
title_var.set("Add a Title")

title_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
title_entry.place(x=90, y=95)
title_entry.insert(0, "Search by title")

title_entry.bind("<FocusIn>", lambda event: title_entry.delete(0, tk.END) if title_entry.get() == "Search by title" else None)

title_entry.bind("<FocusOut>", lambda event: title_entry.insert(0, "Search by title") if not title_entry.get() else None)

"""----------------------------------------AUTHOR----------------------------------------------------"""


def validate_author(value):
    return len(value) <= 50


Author_label = Label(text="Author:", fg='black', bg='white', font=('Arial', 12))
Author_label.place(x=140, y=265)

author_var = tk.StringVar()
author_var.set("Add author")

author_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
author_entry.place(x=90, y=143)
author_entry.insert(0, "Search by author")

author_entry.bind("<FocusIn>", lambda event: author_entry.delete(0, tk.END) if author_entry.get() == "Search by author" else None)

author_entry.bind("<FocusOut>", lambda event: author_entry.insert(0, "Search by author") if not author_entry.get() else None)


"""----------------------------------------GENRE DROPDOWN----------------------------------------------------"""
Genre_label = Label(text="Genre:", fg='black', bg='white', font=('Arial', 12))
Genre_label.place(x=140, y=315)

drop = ttk.Combobox(frame, values=["Myths", "Mystery", "Thriller", "Historical", "Historical Fiction"], width=30)
drop.current(0)
drop.place(x=90, y=192)


"""----------------------------------------ISBN----------------------------------------------------"""


def validate_id_type(value):
    return len(value) <= 13


ISBN_label = Label(text="ISBN:", fg='black', bg='white', font=('Arial', 12))
ISBN_label.place(x=140, y=365)

isbn_var = tk.StringVar()
isbn_var.set("ISBN")

isbn_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
isbn_entry.place(x=90, y=242)
isbn_entry.insert(0, "Search by isbn")

isbn_entry.bind("<FocusIn>", lambda event: isbn_entry.delete(0, tk.END) if isbn_entry.get() == "Search by isbn" else None)

isbn_entry.bind("<FocusOut>", lambda event: isbn_entry.insert(0, "Search by isbn") if not isbn_entry.get() else None)


"""----------------------------------------BRANCH DROPDOWN----------------------------------------------------"""
Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=140, y=415)

drop = ttk.Combobox(frame, values=get_branch_names(), width=30)
drop.current(0)
drop.place(x=90, y=292)


""""---------------------------------SHOW FILTERED ITEMS---------------------------------"""
info_frame = Frame(width=500, highlightbackground="black", highlightthickness=1, height=250, bg="white")
info_frame.place(x=140, y=460)

my_scrollbar = Scrollbar(info_frame, orient=VERTICAL)
my_listbox = Listbox(info_frame, width=80, yscrollcommand=my_scrollbar.set, selectmode=SINGLE)

my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)


my_listbox.pack(pady=15)


my_listbox.insert(END, 'ITEM_ID')


my_list = ['ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID']

for item in my_list:
    my_listbox.insert(END, item)


def return_selected():
    for items in reversed(my_listbox.curselection()):
        my_listbox.delete(items)


"""----------------------------------ITEM IMAGE---------------------------------------- """
img = PhotoImage(file='assets\\images\\books_small.png')
img_label = Label(image=img, bg='#f0f0f0')
img_label.place(x=750, y=160)

"""---------------------------------Branch, IBSN, Status--------------------------------"""

item_branch = Label(frame, text="Branch:", fg='black', bg='white', font=('Arial', 12))
item_branch.place(x=775, y=50)

item_isbn = Label(frame, text="ISBN:", fg='black', bg='white', font=('Arial', 12))
item_isbn.place(x=775, y=100)

item_status = Label(frame, text="Status:", fg='black', bg='white', font=('Arial', 12))
item_status.place(x=775, y=150)

"""----------------------------------Title, Author, Pages-------------------------------------"""
item_title = Label(frame, text='Title:', bg='white', fg='black', font=('Arial', 12))
item_title.place(x=638, y=215)

item_author = Label(frame, text="Author(s):", fg='black', bg='white', font=('Arial', 12))
item_author.place(x=638, y=265)

item_pages = Label(frame, text="Page(s):", fg='black', bg='white', font=('Arial', 12))
item_pages.place(x=638, y=315)

"""----------------------------------CHECKOUT ITEM(S)---------------------------------------- """


def checkoutitem():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Checkout.py')

    try:
        subprocess.run(['python' , script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


return_button = Button(frame, width=20, pady=7, text='Checkout', bg='grey',
                       fg='white', border=3, command=checkoutitem)

return_button.place(x=625, y=500)
"""---------------------------------- SEARCH ---------------------------------------"""


def search_button_click():
    title_value = title_entry.get()
    author_value = author_entry.get()
    isbn_value = isbn_entry.get()

    if title_value is None:
        pass 
    else:
        if not validate_title(title_value):
            messagebox.showerror("Error", "Title must be 50 characters or less.")
            return
    if author_value is None:
        pass
    else:
        if not validate_author(author_value):
            messagebox.showerror("Error", "Author must be 50 characters or less.")
            return
    if isbn_value is None:
        pass
    else:
        if not validate_id_type(isbn_value):
            messagebox.showerror("Error", "Valid ISBN must be 13 characters long.")
            return

    items_found = search_items_by_title(title_value)

    # Process the found items (example: displaying them in a messagebox)
    if items_found:
        items_info = '\n'.join([f"Title: {item.title}, Item Type: {item.item_type}, Status: {item.status}" for item in items_found])
        messagebox.showinfo("Search Results", f"Items Found:\n{items_info}")
    else:
        messagebox.showinfo("Search Results", "No items found with that title.")

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
