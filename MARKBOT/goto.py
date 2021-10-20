import tkinter as tk
from tkinter import font as tkfont
from time import strftime
from PIL import Image, ImageTk
import datetime as dt
import os

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.config(bg="#2e3441")

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.login = controller
        self.login.minsize(1000, 500)
        self.login.maxsize(1000, 500)
        self.login.title('Login Page')
        self.login.geometry('1000x500')

        self.label_welcome = tk.Label(self.login, text="WELCOME!", fg="white", bg="#2E3441", font=("TW Cen MT", 60))
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

        #  self.controller = controller

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
        #  label.pack(side="top", fill="x", pady=10)

        #  button1 = tk.Button(self, text="Go to Page One",
        #                      command=lambda: controller.show_frame("PageOne"))
        #  button2 = tk.Button(self, text="Go to Page Two",
        #                      command=lambda: controller.show_frame("PageTwo"))
        #  button1.pack()
        #  button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
