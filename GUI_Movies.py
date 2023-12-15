from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast
import subprocess
import os
from tkinter import PhotoImage
from library_back import get_branch_names, get_genres, search_movies


"""
Program: GUI_Movies.py
Author: J.Swilling
Goal: Create a GUI for a module that displays available movies that can be easily
 integrated for a Library management system.
 
1. Significant constants
   ID = "ID"
    
2. The inputs are 
    TITLE
    GENRE
    ISAN
    Runtime
    RETURN
    DASHBOARD
    
3. Computations:
    comparison of text strings (Title/Desc) and Integers (IBSN/ISAN/Amount Due/DATE)
    
4. The outputs are
ISAN/BRANCH/STATUS/TITLE/RUNTIME
"""

window = Tk()
window.title("EVPL Management System - Video Inventory")
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

"""---------------------------------- GET ITEMS BY TYPE : MOVIE -----------------------------------------"""
frame = Frame(window, width=1000, highlightbackground="black", highlightthickness=3, height=600, bg='#fff')
frame.place(x=110, y=120)

"""----------------------------------------TITLE----------------------------------------------------"""


def validate_title(value):
    return len(value) <= 50


Title_label = Label(text="Title:", fg='black', bg='white', font=('Arial', 12))
Title_label.place(x=140, y=218)

title_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
title_entry.place(x=95, y=95)

"""----------------------------------------GENRE DROPDOWN----------------------------------------------------"""
Genre_label = Label(text="Genre:", fg='black', bg='white', font=('Arial', 12))
Genre_label.place(x=140, y=265)

genres = get_genres()
genres.insert(0, "")
genre_drop = ttk.Combobox(frame,values=genres, width=30)

genre_drop.current(0)
genre_drop.place(x=95, y=143)

"""----------------------------------------ISAN----------------------------------------------------"""


def validate_id_type(value):
    return len(value) <= 12


isan_label = Label(text="ISAN:", fg='black', bg='white', font=('Arial', 12))
isan_label.place(x=140, y=315)

isan_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
isan_entry.place(x=95, y=192)

"""----------------------------------------RUNTIME----------------------------------------------------"""


def validate_runtime(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


run_label = Label(text="Runtime:", fg='black', bg='white', font=('Arial', 12))
run_label.place(x=140, y=365)

runtime_entry = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
runtime_entry.place(x=95, y=242)

"""----------------------------------------BRANCH DROPDOWN----------------------------------------------------"""
Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=140, y=415)

branches = get_branch_names()
branches.insert(0, "")
branch_drop = ttk.Combobox(frame, values=branches, width=30)


branch_drop.current(0)
branch_drop.place(x=95, y=292)
""""---------------------------------SHOW FILTERED ITEMS---------------------------------"""
info_frame = Frame(width=500, highlightbackground="black", highlightthickness=1, height=280, bg="white")
my_scrollbar = Scrollbar(info_frame, orient=VERTICAL)

my_listbox = Listbox(info_frame, width=80, yscrollcommand=my_scrollbar.set, selectmode=SINGLE)

my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
info_frame.place(x=140, y=450)

my_listbox.pack(pady=15)

my_listbox.insert(END, 'ITEM_ID')

my_list = ['ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID']

for item in my_list:
    my_listbox.insert(END, item)


def return_selected():
    for items in reversed(my_listbox.curselection()):
        my_listbox.delete(items)


"""----------------------------------ITEM IMAGE---------------------------------------- """
img = PhotoImage(file='assets\\images\\movies.png')
img_label = Label(image=img, bg='#f0f0f0')
img_label.place(x=750, y=200)


"""----------------------------------CHECKOUT ITEM---------------------------------------- """


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
    genre_value = genre_drop.grab_current()  # Get the selected genre
    isan_value = isan_entry.get()
    runtime_value = runtime_entry.get()
    branch_value = branch_drop.grab_current()

    if not title_value.strip() and genre_value == "" and not isan_value.strip() and not runtime_value.strip():
        messagebox.showerror("Error", "All fields cannot be empty.")
        return

    if title_value.strip() and not validate_title(title_value):
        messagebox.showerror("Error", "Title must be 50 characters or less.")
        return

    if isan_value.strip() and not validate_id_type(isan_value):
        messagebox.showerror("Error", "Valid ISAN must be 12 characters long.")
        return

    if runtime_value.strip() and not validate_runtime(runtime_value):
        messagebox.showerror("Error", "Runtime must be a valid floating-point number.")
        return


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
