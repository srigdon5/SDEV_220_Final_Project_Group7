from tkinter import *
from tkinter import messagebox
import ast
import subprocess
import ast
from tkinter import PhotoImage
import os
import tkinter as tk


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


window = Tk()
window.title("EVPL Management System - Registration")
window.geometry('1225x750+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
window.iconbitmap("assets\\images\\myIcon.ico")


background = PhotoImage(file="assets\\images\\design.png")
background_label = Label(window, image=background)
background_label.place(x=12, y=0, relwidth=1, relheight=1)

"""------------------------------------------------------------SIGN UP---------------------------------------------------"""

def signup():
    username = user_entry.get()
    password = pass_entry.get()
    confirm_password = conf_entry.get()

    file = open('assets\\datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username == 'Username':
        messagebox.showinfo('Error:', 'Please enter a valid username.')
    elif username in r.keys():
        messagebox.showinfo('Error:', 'Taken, Please enter a valid username.')
    elif password == confirm_password:
        try:
           
            file = open('assets\\datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)
           
           
            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()


            file = open('assets\\datasheet.txt', 'w')
            w = file.write(str(r))

            messagebox.showinfo('Register', 'Successfully Registered!')
        except:

            file = open('assets\\datasheet.txt', 'w')
            pp = str({'Username': 'password'})
            file.write(pp)
            file.close()

    else:

        messagebox.showinfo('Error:', 'Passwords do not match.')

def close_window():
    window.destroy()

    
def log():
    close_window()  
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'GUI_Login.py')
    
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching subprocess: {e}")

"""---------------------------------------------------------------------------------------------------------------"""

frame = Frame(width=450, highlightbackground="black", highlightthickness=3, height=80, bg="white")
frame.place(x=400, y=40)

heading = Label(frame, text='Evansville Vanderburgh Public Library', fg='black', bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
heading.place(x=25, y=18)

"""------------------------------------------------------------Register---------------------------------------------------"""
heading = Label(text='Register', fg="black", bg='white', font=('Microsoft Yahei UI Light', 23,
                                                               'bold'))
heading.place(x=570, y=130)

frame = Frame(window, width=900, highlightbackground="black", highlightthickness=3, height=500, bg='#fff')
frame.place(x=180, y=190)

"""----------------------------------First_Name---------------------------------------"""

fname_var = tk.StringVar()
fname_var.set('First Name')

fname_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
fname_entry.place(x=190, y=83)
fname_entry.insert(0, 'First Name')

fname_entry.bind("<FocusIn>", lambda event: fname_entry.delete(0, tk.END) if fname_entry.get() == 'First Name' else None)

fname_entry.bind("<FocusOut>", lambda event: fname_entry.insert(0, 'First Name') if not fname_entry.get() else None)

Frame(frame, width=295, height=2, bg='black').place(x=80, y=102)
"""----------------------------------Last_Name----------------------------------------"""

lname_var = tk.StringVar()
lname_var.set('Last Name')

lname_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
lname_entry.place(x=190, y=183)
lname_entry.insert(0, 'Last Name')

lname_entry.bind("<FocusIn>", lambda event: lname_entry.delete(0, tk.END) if lname_entry.get() == 'Last Name' else None)

lname_entry.bind("<FocusOut>", lambda event: lname_entry.insert(0, 'Last Name') if not lname_entry.get() else None)


Frame(frame, width=295, height=2, bg='black').place(x=80, y=203)
"""----------------------------------Phone_Number-------------------------------------"""

phone_var = tk.StringVar()
phone_var.set('Phone Number')

phone_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
phone_entry.place(x=170, y=288)
phone_entry.insert(0, 'Phone Number')

phone_entry.bind("<FocusIn>", lambda event: phone_entry.delete(0, tk.END) if phone_entry.get() == 'Phone Number' else None)

phone_entry.bind("<FocusOut>", lambda event: phone_entry.insert(0, 'Phone Number') if not phone_entry.get() else None)

Frame(frame, width=295, height=2, bg='black').place(x=80, y=307)
"""----------------------------------Username---------------------------------------- """

user_var = tk.StringVar()
user_var.set('Create Username')

user_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user_entry.place(x=605, y=83)
user_entry.insert(0, 'Create Username')

user_entry.bind("<FocusIn>", lambda event: user_entry.delete(0, tk.END) if user_entry.get() == 'Create Username' else None)

user_entry.bind("<FocusOut>", lambda event: user_entry.insert(0, 'Create Username') if not user_entry.get() else None)

Frame(frame, width=295, height=2, bg='black').place(x=520, y=102)

"""----------------------------------Password---------------------------------------- """

pass_var = tk.StringVar()
pass_var.set('Create Password')

pass_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
pass_entry.place(x=605, y=184)
pass_entry.insert(0, 'Create Password')

pass_entry.bind("<FocusIn>", lambda event: pass_entry.delete(0, tk.END) if pass_entry.get() == 'Create Password' else None)

pass_entry.bind("<FocusOut>", lambda event: pass_entry.insert(0, 'Create Password') if not pass_entry.get() else None)

Frame(frame, width=295, height=2, bg='black').place(x=520, y=203)

"""----------------------------------Confirm Password---------------------------------------- """

conf_var = tk.StringVar()
conf_var.set('Confirm Password')

conf_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
conf_entry.place(x=605, y=288)
conf_entry.insert(0, 'Confirm Password')

conf_entry.bind("<FocusIn>", lambda event: conf_entry.delete(0, tk.END) if conf_entry.get() == 'Confirm Password' else None)

conf_entry.bind("<FocusOut>", lambda event: conf_entry.insert(0, 'Confirm Password') if not pass_entry.get() else None)

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


signin = Button(width=6, text='Log In', border=0, bg='white', cursor='hand2', fg='green', command=log)
signin.place(x=680, y=655)



window.mainloop()
