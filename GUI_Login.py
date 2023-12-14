from tkinter import *
from tkinter import messagebox
import subprocess
import ast
from tkinter import PhotoImage
import os
from tkinter import Tk, Button
import tkinter as tk



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


root = Tk()
root.title('EVPL Management System')
root.geometry('1225x750+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file='assets\\images\\design.png')
background_label = Label(root, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)




def signin():
    username = user_entry.get()
    password = pass_entry.get()

    file = open('assets\\datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()



    if username in r.keys() and password == r[username]:
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen, text='Hello!', fg='black', bg='#fff', font=('Calibre(Body)', 50, 'bold')).pack(expand=True)
        root.destroy()
        script_dir = os.path.dirname(os.path.realpath(__file__))
        script_path = os.path.join(script_dir, 'GUI_Dashboard.py')
        

        try:
            subprocess.run(['python', script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error launching subprocess: {e}")

    else:
        messagebox.showerror('Invalid', 'invalid username or password')



frame = Frame(root, width=450, highlightbackground="black", highlightthickness=3, height=80, bg="white")
frame.place(x=400, y=20)

heading = Label(frame, text='Evansville Vanderburgh Public Library', fg='black', bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
heading.place(x=25, y=12)



heading = Label(text='Welcome', fg='black', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=550, y=120)

frame = Frame(root, width=450, highlightbackground="black", highlightthickness=3, height=450, bg="white")
frame.place(x=400, y=200)




"""----------------------------------Username---------------------------------------- """

user_var = tk.StringVar()
user_var.set('Username')

user_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user_entry.place(x=180, y=98)
user_entry.insert(0, 'Username')

user_entry.bind("<FocusIn>", lambda event: user_entry.delete(0, tk.END) if user_entry.get() == 'Username' else None)

user_entry.bind("<FocusOut>", lambda event: user_entry.insert(0, 'Username') if not user_entry.get() else None)

Frame(frame, width=295, height=2, bg='black').place(x=75, y=117)


"""----------------------------------Password---------------------------------------- """


pass_var = tk.StringVar()
pass_var.set('Password')

pass_entry = tk.Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11), show='')
pass_entry.place(x=180, y=182)
pass_entry.insert(0, 'Password')

pass_entry.bind("<FocusIn>", lambda event: (pass_entry.delete(0, tk.END), pass_entry.config(show='')) if pass_entry.get() == 'Password' else None)
pass_entry.bind("<Key>", lambda event: pass_entry.config(show='*'))
pass_entry.bind("<FocusOut>", lambda event: (pass_entry.insert(0, 'Password'), pass_entry.config(show='')) if not pass_entry.get() else None)

tk.Frame(frame, width=295, height=2, bg='black').place(x=75, y=203)

"""----- Define function and Format buttons for input submission ('Sign in' and 'Sign Up') -------------"""



def close_window():
    root.destroy()



def register():
    close_window() 

   
    script_dir = os.path.dirname(os.path.realpath(__file__))

    
    script_path = os.path.join(script_dir, 'GUI_Registration.py')

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")


Button(frame, width=19, pady=7, text='Sign in', bg='black', fg='white', border=0, cursor='hand2',
       command=signin).place(x=50, y=254)

(Button(frame, width=19, pady=7, text='Sign up', bg='black', fg='white', border=0, cursor='hand2', command=register).place(x=242, y=254))



def user_manual():
    subprocess.Popen(['python', 'userManual.py'])




def user_manual():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Manual.py')
    

    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")

help_link = Button(frame, width=20, pady=7, text='Need help?', bg='white', fg='green', border=0,
                   command=user_manual, cursor='hand2')
help_link.place(x=140, y=320)



root.mainloop()
