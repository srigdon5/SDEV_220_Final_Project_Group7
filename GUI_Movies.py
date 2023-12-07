from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast
import subprocess
import os
from tkinter import PhotoImage

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

# Create the main registration window
window = Tk()
window.title("EVPL Management System - Video Inventory")
window.geometry('1225x750+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
window.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file="assets\\images\\design.png")
background_label = Label(window, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)


# Create a frame for labels and input fields
frame = Frame(width=250, highlightbackground="black", highlightthickness=3, height=80, bg="white")
frame.place(x=500, y=20)

heading = Label(frame, text='Library Inventory', fg='black', bg='white',
                font=('Microsoft YaHei UI Light', 16, 'bold'))
heading.place(x=30, y=18)

"""---------------------------------- GET ITEMS BY TYPE : MOVIE -----------------------------------------"""
frame = Frame(window, width=1000, highlightbackground="black", highlightthickness=3, height=600, bg='#fff')
frame.place(x=110, y=120)

"""---------------------------------- SEARCHING BY: ---------------------------------------"""


search_id = Button(frame, width=30, pady=7, text='Search', bg='grey', fg='white', border=3)
search_id.place(x=55, y=25)

"""----------------------------------------TITLE----------------------------------------------------"""
Title_label = Label(text="Title:", fg='black', bg='white', font=('Arial', 12))
Title_label.place(x=140, y=218)

user = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=95, y=95)
user.insert(0, "Search by title")

"""----------------------------------------GENRE DROPDOWN----------------------------------------------------"""
Author_label = Label(text="Genre:", fg='black', bg='white', font=('Arial', 12))
Author_label.place(x=140, y=265)

drop = ttk.Combobox(frame, values=["Action", "Comedy", "Horror"], width=30)
drop.current(0)
drop.place(x=95, y=143)


"""----------------------------------------ISAN----------------------------------------------------"""
Genre_label = Label(text="ISAN:", fg='black', bg='white', font=('Arial', 12))
Genre_label.place(x=140, y=315)

user = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=95, y=192)
user.insert(0, "Search by isan")


"""----------------------------------------RUNTIME----------------------------------------------------"""
ISBN_label = Label(text="Runtime:", fg='black', bg='white', font=('Arial', 12))
ISBN_label.place(x=140, y=365)

user = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=95, y=242)
user.insert(0, "Search by runtime")


""""---------------------------------SHOW FILTERED ITEMS---------------------------------"""
# List box for customer's items
info_frame = Frame(width=500, highlightbackground="black", highlightthickness=1, height=280, bg="white")
my_scrollbar = Scrollbar(info_frame, orient=VERTICAL)

my_listbox = Listbox(info_frame, width=80, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)

# Configure scrollbar
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
info_frame.place(x=140, y=450)

my_listbox.pack(pady=15)


# Add item to listbox
my_listbox.insert(END, 'ITEM_ID')


# Add list to listbox
my_list = ['ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID', 'ITEM_ID']

# Iterate through and insert items from the list
for item in my_list:
    my_listbox.insert(END, item)


def return_selected():
    for items in reversed(my_listbox.curselection()):
        my_listbox.delete(items)


"""----------------------------------ITEM IMAGE---------------------------------------- """
img = PhotoImage(file='assets\\images\\movies.png')
img_label = Label(image=img, bg='#f0f0f0')
img_label.place(x=750, y=160)


"""----------------------------------Branch, ISAN, Status-------------------------------------"""
item_branch = Label(frame, text="Branch:", fg='black', bg='white', font=('Arial', 12))
item_branch.place(x=775, y=50)

item_isan = Label(frame, text="ISAN:", fg='black', bg='white', font=('Arial', 12))
item_isan.place(x=775, y=100)

item_status = Label(frame, text="Status:", fg='black', bg='white', font=('Arial', 12))
item_status.place(x=775, y=150)


"""----------------------------------Title, Runtime-------------------------------------"""
item_title = Label(frame,text='Title:', bg='white', fg='black',font=('Arial', 12))
item_title.place(x=638, y=215)

item_runtime = Label(frame, text="Runtime:", fg='black', bg='white', font=('Arial', 12))
item_runtime.place(x=638, y=265)


"""----------------------------------CHECKOUT ITEM---------------------------------------- """


def checkoutitem():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Checkout.py')
    python_interpreter = 'C:\\Users\\JSwil\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'

    try:
        subprocess.run([python_interpreter, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


return_button = Button(frame, width=20, pady=7, text='Checkout', bg='grey',
                       fg='white', border=3, command=checkoutitem)

return_button.place(x=625, y=500)

"""----------------------------------BACK TO DASHBOARD---------------------------------------- """


def close_window():
    window.destroy()


# Function to open another program
def dashboard():
    close_window()  # Close the current window
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Dashboard.py')
    python_interpreter = 'C:\\Users\\JSwil\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'
    # Replace with your Python interpreter path

    try:
        subprocess.run([python_interpreter, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


Button(frame, width=20, pady=7, text='Dashboard', bg='grey', fg='white', border=3,
       command=dashboard).place(x=800, y=500)

"""--------------------------------------------------------------------------------"""

# Start the Tkinter event loop to run the registration GUI
window.mainloop()
