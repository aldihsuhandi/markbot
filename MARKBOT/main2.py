import tkinter as tk
from time import strftime
from PIL import ImageTk, Image
import datetime as dt
import os

class LoginPage(tk.Frame):

    def __init__(self):
        #Window
        self.login = tk.Tk()
        self.login.minsize(800, 500)
        self.login.title('Login Page')
        self.login.geometry('1000x500')
        self.login.config(bg="#2E3441")
        self.login.minsize(1000, 500)
        self.login.maxsize(1000, 500)

        #Welcome Label
        self.label_welcome = tk.Label(self.login, text="WELCOME!", fg="white", bg="#2E3441",font=("TW Cen MT", 60))
        self.label_welcome.place(relwidth=0.5, relheight=0.2, relx=0.25, rely=0.1)

        #  def timeWelcome(self):
        #      self.string_time = strftime('%H: %M: %S')
        #      self.label_time.config(text=self.string_time)
        #      self.label_time.after(200, timeWelcome)

        #  self.label_time = tk.Label(self.login, fg="white", bg="#2E3441", font=("TW Cen MT", 20))
        #  self.label_time.place(relwidth=0.5, relheight= 0.05, relx=0.25, rely=0.3)
        #  timeWelcome(self)

        self.label_date = tk.Label(self.login, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="#2E3441", font=("TW Cen MT", 30))
        self.label_date.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.35)

        #Input username
        self.frame_input=tk.Frame(self.login)
        self.frame_input.config(bg="#2E3441")

        self.label_username = tk.Label(self.frame_input, text="Username",fg="white", bg="#2E3441", font=("TW Cen MT", 18))
        self.username = tk.StringVar()
        self.entry_username = tk.Entry(self.frame_input, textvariable=self.username)

        self.label_password = tk.Label(self.frame_input, text="Password", fg="white", bg="#2E3441", font=("TW Cen MT", 18))
        self.password = tk.StringVar()
        self.entry_password = tk.Entry(self.frame_input, textvariable=self.password, show="*")

        self.label_username.place(width=150,height=20, relx=0.3, rely=0.1)
        self.entry_username.place(width=200,height=20, relx=0.460, rely=0.1)

        self.label_password.place(width=150, height=20, relx=0.3, rely=0.35)
        self.entry_password.place(width=200, height=20, relx=0.460, rely=0.35)

        self.frame_input.place(relwidth=1, relheight=0.3, relx=0, rely=0.6)

        #Login Button
        self.button_login = tk.Button(self.login, text="Sign in", width=20, height=2, command=self.validate)
        self.button_login.place(relx=0.5,rely=0.85, anchor="center")

        self.login.grid_rowconfigure(0,weight=1)
        self.login.grid_columnconfigure(0, weight=1)
        self.login.mainloop()


    def invalidAccount(self):
        self.invalid_screen = tk.Toplevel(self.login)
        self.invalid_screen.title("Invalid Login")
        self.invalid_screen.geometry("300x150")

        self.label_invalid = tk.Label(self.invalid_screen, text="Invalid password or username", font=("TW Cen MT", 16)).pack(anchor="center", pady=20)
        self.button_invalid = tk.Button(self.invalid_screen, text="OK", width = 20, height=2, font=(16),command=self.invalid_screen.destroy).pack(anchor="center")

    def validate(self):
        self.userinfo = self.username.get()
        self.passinfo = self.password.get()
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

        self.controller = controller
        controller.show_frame("SubjectPage")

        #  self.list_of_files = os.listdir()
        #  if self.userinfo in self.list_of_files:
        #      self.fileCheck = open(self.userinfo, "r")
        #      self.verify = self.fileCheck.read().splitlines()
        #      if self.passinfo in self.verify:
        #          self.login.destroy()
        #      else:
        #          self.invalidAccount()

        #  else:
        #      self.invalidAccount()


    def run(self):
        self.login.mainloop()

app = LoginPage()
app.run()
