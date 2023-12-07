from tkinter import *
from tkinter import messagebox
import subprocess
import ast
from tkinter import PhotoImage
import os
from tkinter import ttk

"""
Program: GUI_Add.py
Author: J.Swilling
Goal: to add a submenu to the "add" option in Dashboard.py.
1. Significant constants
  
2. The inputs are
   
3. Computations:
    
4. The outputs are
 
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

"""------------------------------------------------------------------------------------------"""

frame = Frame(root, width=397, highlightbackground="black", highlightthickness=3, height=680, bg='#fff')
frame.place(x=1, y=10)

Title_label = Label(text="Title:", fg='black', bg='white', font=('Arial', 12))
Title_label.place(x=40, y=50)

user = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=140, y=37)
user.insert(0, "Add a Title")

"""----------------------------------------------------"""
Author_label = Label(text="Author:", fg='black', bg='white', font=('Arial', 12))
Author_label.place(x=40, y=100)

user = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=140, y=87)
user.insert(0, "Add author")

"""----------------------------------------------------"""
Genre_label = Label(text="Genre:", fg='black', bg='white', font=('Arial', 12))
Genre_label.place(x=40, y=150)


drop = ttk.Combobox(frame, values=["Action", "Comedy", "Horror", ""], width=30)
drop.current(0)
drop.place(x=140, y=137)

"""----------------------------------------------------"""
ID_Type_label = Label(text="ID Type:", fg='black', bg='white', font=('Arial', 12))
ID_Type_label.place(x=40, y=200)


id_drop = ttk.Combobox(frame, values=["ISBN", "ISAN"], width=30)
id_drop.current(0)
id_drop.place(x=140, y=187)


"""----------------------------------------------------"""
ID_label = Label(text="ID:", fg='black', bg='white', font=('Arial', 12))
ID_label.place(x=40, y=250)

user = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=140, y=237)
user.insert(0, "Enter the item ID")
"""----------------------------------------------------"""
Branch_label = Label(text="Branch:", fg='black', bg='white', font=('Arial', 12))
Branch_label.place(x=40, y=300)


drop = ttk.Combobox(frame, values=["North Branch", "South Branch", "East Branch", "West Branch", ""], width=30)
drop.current(0)
drop.place(x=140, y=287)
"""----------------------------------------------------"""
page_label = Label(text="Page(s):", fg='black', bg='white', font=('Arial', 12))
page_label.place(x=40, y=350)

user = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=140, y=337)
user.insert(0, "")
"""----------------------------------------------------"""
run_label = Label(text="Runtime:", fg='black', bg='white', font=('Arial', 12))
run_label.place(x=40, y=400)

user = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=140, y=387)
user.insert(0, "")
"""----------------------------------------------------"""
run_label = Label(text="Date:", fg='black', bg='white', font=('Arial', 12))
run_label.place(x=40, y=450)

user = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=140, y=437)
user.insert(0, "")
"""----------------------------------------------------"""
run_label = Label(text="User ID:", fg='black', bg='white', font=('Arial', 12))
run_label.place(x=40, y=500)

user = Entry(frame, width=25, fg='grey', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=140, y=487)
user.insert(0, "Enter Staff ID")
"""----------------------------------------------------"""
add_btn = Button(frame, width=10, pady=7, text='ADD', bg='grey', fg='white', border=3)
add_btn.place(x=80, y=600)
"""----------------------------------------------------"""

def abortproc():
    root.destroy()

cancel_btn = Button(frame, width=10, pady=7, text='CANCEL', bg='grey', fg='white', border=3, command=abortproc)
cancel_btn.place(x=230, y=600)
"""----------------------------------------------------"""
root.mainloop()
