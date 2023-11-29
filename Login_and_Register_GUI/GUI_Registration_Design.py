from tkinter import *
from tkinter import messagebox
import ast
import subprocess
import ast
from tkinter import PhotoImage



"""
Program: GUI_Registration_Design.py
Author: J.Swilling
Goal: Create a Registration GUI that can be easily integrated, use for Library management system.
1. Significant constants
    PASSWORD
    USERNAME
2. The inputs are
    Password and Username, and confirmation
3. Computations:
    comparison of text strings (User) and Integers (Password)
4. The outputs are
 Failure/Registered accounts
"""

# Create the main registration window
window = Tk()
window.title("EVPL Management System - Registration")
window.geometry('1225x750+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
window.iconbitmap("Login_and_Register_GUI\myIcon.ico")


background = PhotoImage(file="Login_and_Register_GUI\design.png")
background_label = Label(window, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)


# Function for handling user sign-up
def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    file = open('Login_and_Register_GUI\datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username == 'Username':
        messagebox.showinfo('Error:', 'Please enter a valid username.')
    elif username in r.keys():
        messagebox.showinfo('Error:', 'Taken, Please enter a valid username.')
    elif password == confirm_password:
        try:
            # Read existing user data from a file
            file = open('Login_and_Register_GUI\datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            # Update user data with the new username and password
            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            # Write the updated data back to the file and display a success message
            file = open('Login_and_Register_GUI\datasheet.txt', 'w')
            w = file.write(str(r))

            messagebox.showinfo('Register', 'Successfully Registered!')
        except:
            # Create a new file with default data if there's an issue
            file = open('Login_and_Register_GUI\datasheet.txt', 'w')
            pp = str({'Username': 'password'})
            file.write(pp)
            file.close()

    else:
        # Display an error message if passwords do not match
        messagebox.showinfo('Error:', 'Passwords do not match.')


def log():
    window.destroy()
    subprocess.Popen(['python', 'GUI_Login_Design.py'])


# Create a frame for labels and input fields
frame = Frame(width=450, highlightbackground="black", highlightthickness=3, height=80, bg="white")
frame.place(x=400, y=40)

heading = Label(frame, text='Evansville Vanderburgh Public Library', fg='black', bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
heading.place(x=25, y=18)


heading = Label(text='Register', fg="black", bg='white', font=('Microsoft Yahei UI Light', 23,
                                                               'bold'))
heading.place(x=570, y=130)

frame = Frame(window, width=900, highlightbackground="black", highlightthickness=3, height=500, bg='#fff')
frame.place(x=180, y=190)

"""----------------------------------First_Name---------------------------------------"""


# create functions for a responsive placeholder text
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'First Name')


# creates field for first name
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=190, y=83)
user.insert(0, 'First Name')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=80, y=102)
"""----------------------------------Last_Name----------------------------------------"""


# create functions for a responsive placeholder text
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'last Name')


# creates field for last name
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=190, y=183)
user.insert(0, 'Last Name')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=80, y=203)
"""----------------------------------Phone_Number-------------------------------------"""


# create functions for a responsive placeholder text
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Phone Number')


# creates field for phone number
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=170, y=288)
user.insert(0, 'Phone Number')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=80, y=307)
"""----------------------------------Username---------------------------------------- """


# create functions for a responsive placeholder text
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Create Username')


# creates field for username
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=605, y=83)
user.insert(0, 'Create Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=520, y=102)

"""----------------------------------Password---------------------------------------- """


# create functions for a responsive placeholder text
def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Create Password')


code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=605, y=184)
code.insert(0, 'Create Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=520, y=203)

"""----------------------------------Confirm Password---------------------------------------- """


# create functions for a responsive placeholder text
def on_enter(e):
    confirm_code.delete(0, 'end')


def on_leave(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm Password')


confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
confirm_code.place(x=605, y=288)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=520, y=307)
"""----------------------------------Policy Agreement-------------------------------"""

heading = Label(text='By confirmation, both parties are accepting responsibility to adhere to \n'
                     'the rules in the agreement. The agreement will detail what can be\n'
                     ' created with the licensed materials, how they can be used and \n'
                     'where they may appear on your website or blog posts.', fg="black", bg='white', font=('Microsoft Yahei UI Light', 6,
                                                               'bold'))
heading.place(x=450, y=560)

"""----------------------------------Button---------------------------------------- """

Button(frame, width=39, pady=7, text='Confirm', bg='black', fg='white', border=0, command=signup).place(x=295, y=425)

label = Label(text='Already have an account ? --', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=520, y=655)

# Link to the Sign-In Page
signin = Button(width=6, text='Log In', border=0, bg='white', cursor='hand2', fg='green', command=log)
signin.place(x=680, y=655)


# Start the Tkinter event loop to run the registration GUI
window.mainloop()
