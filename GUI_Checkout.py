from tkinter import *
from tkinter import messagebox
import subprocess
import ast
from tkinter import PhotoImage
import os
from tkinter import ttk

"""
Program: GUI_Checkout.py
Author: J.Swilling
Goal: to add a submenu to the "checkout" options in Books/Movies.py.
1. Significant constants
  
2. The inputs are
   
3. Computations:
    
4. The outputs are
 
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

item_label = Label(text="Item ID:", fg='black', bg='white', font=('Arial', 12))
item_label.place(x=40, y=50)

user_item = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user_item.place(x=140, y=37)
user_item.insert(0, "Enter Item ID")

"""----------------------------------------------------"""
user_label = Label(text="User ID:", fg='black', bg='white', font=('Arial', 12))
user_label.place(x=40, y=100)

user_ID = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user_ID.place(x=140, y=87)
user_ID.insert(0, "Enter Customer's ID")

"""----------------------------------------------------"""
Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=40, y=150)


drop = ttk.Combobox(frame, values=["North Branch", "South Branch", "East Branch", "West Branch", ""], width=30)
drop.current(0)
drop.place(x=140, y=137)

"""----------------------------------------------------"""
date_label = Label(text="Date:", fg='black', bg='white', font=('Arial', 12))
date_label.place(x=40, y=200)

user_date = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user_date.place(x=140, y=187)
user_date.insert(0, "")


"""----------------------------------------------------"""

"""----------------------------------------------------"""
remove_btn = Button(frame, width=10, pady=7, text='CHECKOUT', bg='grey', fg='white', border=3)
remove_btn.place(x=80, y=300)
"""----------------------------------------------------"""
cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3)
cancel_btn.place(x=230, y=300)
"""----------------------------------------------------"""
root.mainloop()
