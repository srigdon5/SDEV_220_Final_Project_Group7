from tkinter import *
from tkinter import messagebox
import subprocess
import ast
from tkinter import PhotoImage
import os
from tkinter import ttk
import tkinter as tk
from library_back import remove_item
"""
Program: GUI_Remove.py
Author: J.Swilling
Goal: to add a submenu to the "remove" option in Dashboard.py.
1. Significant constants
    - No significant constants defined in this section.

2. The inputs are
    - User input through the GUI, including:
        - Item ID

3. Computations:
    - Validation of user inputs:
        - Checking if Item ID is a valid integer.

4. The outputs are
    - Displayed through the GUI:
        - Feedback messages for validation errors.
        
"""


root = Tk()
root.title('EVPL Management System - Remove Item')
root.geometry('400x200+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file='assets\\images\\design.png')
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)

"""------------------------------------------------------------------------------------------"""

frame = Frame(root, width=397, highlightbackground="black", highlightthickness=3, height=200, bg='#fff')
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


"""-----------------------------------------REMOVE/CANCEL----------------------------------------------"""


def remove_button_click():
    # Retrieve values from the Entry widgets
    item_value = item_entry.get()

    if not validate_item_id(item_value):
        messagebox.showerror("Error", "Item ID must be a valid integer.")
        return

    # Fetch item details (title and branches) based on item ID (you'll need to implement this)
    item_details = fetch_item_details(item_value)

    if item_details:
        confirmation_message = f"Are you sure you want to remove the item '{item_details['title']}' from branches: {', '.join(item_details['branches'])}?"
        
        confirmation = messagebox.askquestion("Confirm Remove", confirmation_message)

        if confirmation == 'yes':
            # User confirmed, proceed with removal
            confirm_removal(item_value)
        else:
            # User canceled the removal
            messagebox.showinfo("Cancelled", "Item removal was cancelled.")
    else:
        messagebox.showerror("Error", "Item not found.")
    # Create a confirmation popup window
    confirmation_window = Toplevel(root)
    confirmation_window.title("Confirm Remove")

    # Add a confirmation button to proceed with removal
    confirm_button = Button(confirmation_window, text="Confirm", command=lambda: confirm_removal(item_value))
    confirm_button.pack()
    # Close the confirmation window
    confirmation_window.destroy()


def confirm_removal(item_id):
    # Perform the actual removal of the item (you'll need to implement this)
    removal = remove_item(item_id)
    if removal == True:
        messagebox.showinfo("Success", "Item removed successfully.")
    else:
        messagebox.showerror("Error", "Item not found.")

# Replace these functions with your actual implementation


def fetch_item_details(item_id):
    # Replace with your logic to fetch item details
    # Return a dictionary containing title and branches
    # Example: {"title": "Sample Title", "branches": ["Branch1", "Branch2"]}
    pass


def remove_item(item_id):
    # Replace with your logic to remove the item
    pass


remove_btn = Button(frame, width=10, pady=7, text='REMOVE', bg='grey', fg='white', border=3,
                    command=remove_button_click)

remove_btn.place(x=80, y=100)
"""----------------------------------------------------"""


def abortproc():
    root.destroy()


cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=230, y=100)
"""----------------------------------------------------"""
root.mainloop()
