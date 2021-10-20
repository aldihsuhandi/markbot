import tkinter as tk
from tkinter import *
from tkinter.ttk import *

class MainPage:
    def __init__(self):
        #Window
        self.mainMenu = tk.Tk()
        self.mainMenu.title('Subject Menu')
        self.mainMenu.geometry('800x600')
        self.mainMenu.config(bg = "#2E3441")
        self.mainMenu.minsize(1000, 800)
        self.mainMenu.maxsize(1000, 800)

        #label
        self.labelMenu = tk.Frame(self.mainMenu, bg = "#d8dee9", width = 650, height = 800)
        self.labelMenu.place(relx = 0, rely = 0.5, anchor = "center")
        self.textLabel = tk.Label(self.mainMenu, text="Welcome!", fg = "#2e3441")
        self.textLabel.place(relx = 0.5, rely = 0.5, anchor = "center")

    def run(self):
        self.mainMenu.mainloop()

page = MainPage()
page.run()
