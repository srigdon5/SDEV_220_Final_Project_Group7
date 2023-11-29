from tkinter import *
from tkinter import messagebox
import ast
import subprocess
import ast
from tkinter import PhotoImage


"""
Program: Dashboard_GUI.py
Author: J.Swilling
Goal: Create a Dashboard GUI that can be easily integrated for a Library management system.
1. Significant constants
    CHECKOUT
    RETURN
    SIGN_OUT
    
2. The inputs are
    BOOKS
    ACCOUNT
    MOVIES
    
3. Computations:
    comparison of text strings (Title/Desc) and Integers (Location/IBSN)
4. The outputs are
 Available/Unavailable Items
"""

# Create the main registration window
window = Tk()
window.title("EVPL Management System - Dashboard")
window.geometry('1225x750+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
window.iconbitmap("Login_and_Register_GUI\\myIcon.ico")


background = PhotoImage(file="Login_and_Register_GUI\\design.png")
background_label = Label(window, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)


# Create a frame for labels and input fields
frame = Frame(width=450, highlightbackground="black", highlightthickness=3, height=80, bg="white")
frame.place(x=400, y=40)

heading = Label(frame, text='Evansville Vanderburgh Public Library', fg='black', bg='white',
                font=('Microsoft YaHei UI Light', 16, 'bold'))

heading.place(x=25, y=18)


heading = Label(text='Dashboard', fg="black", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))

heading.place(x=540, y=130)

frame = Frame(window, width=1000, highlightbackground="black", highlightthickness=3, height=500, bg='#fff')
frame.place(x=110, y=190)

"""----------------------------------Accounts---------------------------------------"""


def close_window():
    window.destroy()


# Function to open another program
def accounts():
    close_window()  # Close the current window
    subprocess.Popen(['python', 'Dashboard\\Accounts.py'])


Button(frame, width=39, pady=7, text='Accounts', bg='black', fg='white', border=0, command=accounts).place(x=55, y=25)


"""----------------------------------Books----------------------------------------"""
Button(frame, width=39, pady=7, text='Books', bg='black', fg='white', border=0,).place(x=355, y=25)


"""----------------------------------Movies-------------------------------------"""
Button(frame, width=39, pady=7, text='Movies', bg='black', fg='white', border=0,).place(x=655, y=25)


"""----------------------------------RETURN---------------------------------------- """
# Function to open another program


def gotoreturn():
    close_window()  # Close the current window
    subprocess.Popen(['python', 'Dashboard\\Accounts.py'])


Button(frame, width=39, pady=15, text='Return', bg='grey', fg='white', border=3, command=gotoreturn).place(x=355, y=125)


"""----------------------------------ADD---------------------------------------- """
Button(frame, width=39, pady=15, text='Add', bg='grey', fg='white', border=3).place(x=355, y=225)


"""----------------------------------REMOVE---------------------------------------- """
Button(frame, width=39, pady=15, text='Remove', bg='grey', fg='white', border=3).place(x=355, y=325)


"""----------------------------------SIGN_OUT---------------------------------------- """


# Function to open another program
def signout():
    close_window()  # Close the current window
    subprocess.Popen(['python', 'Login_and_Register_GUI\\GUI_Login_Design.py'])


Button(frame, width=39, pady=7, text='Sign Out', bg='white', fg='black', border=3, command=signout).place(x=355, y=425)


# Start the Tkinter event loop to run the registration GUI
window.mainloop()