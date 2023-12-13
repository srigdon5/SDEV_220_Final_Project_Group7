from tkinter import *
from tkinter import messagebox
import ast
import subprocess
import ast
from tkinter import PhotoImage
import os

"""
Program: GUI_Dashboard.py
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
window.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file="assets\\images\\design.png")
background_label = Label(window, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)


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


def accounts():
    close_window()  # Close the current window
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Accounts.py')

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


Button(frame, width=39, pady=7, text='Accounts', bg='black', fg='white', border=0, command=accounts).place(x=55, y=25)


"""----------------------------------Books----------------------------------------"""


def books():
    close_window()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Books.py')

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


Button(frame, width=39, pady=7, text='Books', bg='black', fg='white', border=0, command=books).place(x=355, y=25)


"""----------------------------------Movies-------------------------------------"""


def movies():
    close_window()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Movies.py')

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


Button(frame, width=39, pady=7, text='Movies', bg='black', fg='white', border=0, command=movies).place(x=655, y=25)

"""----------------------------------RETURN---------------------------------------- """


def gotoreturn():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Return.py')

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


Button(frame, width=39, pady=15, text='Return', bg='grey', fg='white', border=3, command=gotoreturn).place(x=355, y=125)


"""----------------------------------ADD---------------------------------------- """


def additem():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Add.py')

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


Button(frame, width=39, pady=15, text='Add', bg='grey', fg='white', border=3, command=additem).place(x=355, y=225)


"""----------------------------------REMOVE---------------------------------------- """


def removeitem():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Remove.py')

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


Button(frame, width=39, pady=15, text='Remove', bg='grey', fg='white', border=3, command=removeitem).place(x=355, y=325)


"""----------------------------------SIGN_OUT---------------------------------------- """


# Function to open another program
def signout():
    response = messagebox.askyesno("Logout Confirmation", "Are you sure you would like to log out?")

    if response:
        close_window()  # Close the current window
        script_dir = os.path.dirname(os.path.realpath(__file__))
        script_path = os.path.join(script_dir, 'GUI_Login.py')

        try:
            subprocess.run(['python', script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error launching subprocess: {e}")


Button(frame, width=39, pady=7, text='Sign Out', bg='white', fg='black', border=3, command=signout).place(x=355, y=425)


window.mainloop()
