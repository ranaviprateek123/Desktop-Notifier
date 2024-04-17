from tkinter import *
from tkinter import messagebox
import os

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Add your login credentials here
    if username == "admin" and password == "password":
        root.destroy()
        os.system("python notifierpy.py")  # Launch the notifier app after successful login
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = Tk()
root.title("Login Page")
root.geometry("300x200")

label_username = Label(root, text="Username:")
label_username.pack()
entry_username = Entry(root)
entry_username.pack()

label_password = Label(root, text="Password:")
label_password.pack()
entry_password = Entry(root, show="*")
entry_password.pack()

btn_login = Button(root, text="Login", command=login)
btn_login.pack()

root.mainloop()
