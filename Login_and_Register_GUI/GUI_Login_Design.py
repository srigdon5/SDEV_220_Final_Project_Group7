from tkinter import *
from tkinter import messagebox
import subprocess
import ast
from tkinter import PhotoImage


"""
Program: GUI_Login_Design.py
Author: J.Swilling
Goal: Create a Login GUI that can be easily integrated, use this GUI for a library management system.
1. Significant constants
    PASSWORD
    USERNAME
2. The inputs are
    Password and Username
3. Computations:
    comparison of text strings (User) and Integers (Password)
4. The outputs are
 Login success/Failure/Help/Register an account
"""

""" create project and the dimensions for the login form and generate the window """
# declaring a separate variable to access tkinter
root = Tk()
root.title('EVPL Management System')
root.geometry('1225x750+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("myIcon.ico")


background = PhotoImage(file="background.png")
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)


""" define and configure loading screen on successful login"""


# creates variables to access the input from user in the password and username fields
def signin():
    username = user.get()
    password = code.get()

    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())

    if username in r.keys() and password == r[username]:
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen, text='Hello!', fg='black', bg='#fff', font=('Calibre(Body)', 50, 'bold')).pack(expand=True)

        screen.mainloop()
    else:
        messagebox.showerror('Invalid', 'invalid username or password')


""" Frame div area for labels and text input """
frame = Frame(root, width=450, highlightbackground="black", highlightthickness=3, height=80, bg="white")
frame.place(x=400, y=20)

heading = Label(frame, text='Evansville Vanderburgh Public Library', fg='black', bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
heading.place(x=25, y=12)


""" Label 1 placement and text """
heading = Label(text='Welcome', fg='black', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=550, y=120)

frame = Frame(root, width=450, highlightbackground="black", highlightthickness=3, height=450, bg="white")
frame.place(x=400, y=200)


""" Format a seamless input with no borders and placeholder text prompt that deletes on entering text field """

"""----------------------------------Username---------------------------------------- """


# create functions for a responsive placeholder text
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


# creates field for username
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=180, y=98)
user.insert(0, 'Username')

# bind text field 'Username' to be accessed in function above
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg='black').place(x=75, y=117)


"""----------------------------------Password---------------------------------------- """


# deletes text once text field is clicked
def on_enter(e):
    code.delete(0, 'end')


# re-iterates the placeholder text once an EMPTY text field is clicked off from
def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


# creates field for password
code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=180, y=182)
code.insert(0, 'Password')

# bind text field 'Password' to be accessed in function above
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=75, y=203)

"""----- Define function and Format buttons for input submission ('Sign in' and 'Sign Up') -------------"""


# Function to close the current window
def close_window():
    root.destroy()


# Function to open another program
def register():
    close_window()  # Close the current window
    subprocess.Popen(['python', 'GUI_Registration_Design.py'])


Button(frame, width=19, pady=7, text='Sign in', bg='black', fg='white', border=0, cursor='hand2',
       command=signin).place(x=50, y=254)

(Button(frame, width=19, pady=7, text='Sign up', bg='black', fg='white', border=0, cursor='hand2', command=register).place(x=242, y=254))


# Create a function to open the user manual program
def user_manual():
    subprocess.Popen(['python', 'userManual.py'])


# Create the link and bind it to the open_user_manual function
help_link = Button(frame, width=20, pady=7, text='Need help signing in?', bg='white', fg='green', border=0,
                   command=user_manual, cursor='hand2')
help_link.place(x=140, y=320)


# Start the Tkinter event loop to run the registration GUI
root.mainloop()
