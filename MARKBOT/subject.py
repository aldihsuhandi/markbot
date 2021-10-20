import tkinter as tk
from tkinter import *
from tkinter.ttk import *

class SubjectPage:
    def __init__(self):
        #Window
        self.subjectMenu = tk.Tk()
        self.subjectMenu.title('Subject Menu')
        self.subjectMenu.geometry('800x600')
        self.subjectMenu.config(bg = "#2E3441")
        self.subjectMenu.minsize(1000, 500)
        self.subjectMenu.maxsize(1000, 500)

        #header
        self.frame_blueheader = tk.Frame(self.subjectMenu)
        self.frame_blueheader.config(bg = "#2E3441")
        self.frame_blueheader.grid(row = 0, column = 1)

        #mid
        self.frame_mid = tk.Frame(self.subjectMenu, bg = "#d8dee9", width = 980, height = 480)
        self.frame_mid.place(relx = 0.5, rely = 0.5, anchor = "center")

        #text label
        self.textSelect = tk.Label(text="Select Subject", bg = "#d8dee9", fg = "#2e3441")
        self.textSelect.config(font=("Roboto", 28))
        self.textSelect.place(relx = 0.5, rely = 0.15, anchor = "center")

        #subject button
        self.englishLogo = tk.PhotoImage(file = r"img/english.png")
        self.englishButton = tk.Button(self.subjectMenu, text = "English", image = self.englishLogo, bg = "#d8dee9")
        self.englishButton.place(relx = 0.5, rely = 0.35, anchor = "center")

        # feedback
        self.feedbackLogo = tk.PhotoImage(file = r"img/feedback.png")
        self.feedbackButton = tk.Button(self.subjectMenu, text = "Feedback", image = self.feedbackLogo, command = self.popUpFeedback)
        self.feedbackButton.place(relx = 0.95, rely = 0.9, anchor = "center")

    def popUpFeedback(self):
        #window
        self.feedback = tk.Toplevel(self.subjectMenu)
        self.feedback.title("Feedback")
        self.feedback.geometry("300x500")
        self.feedback.minsize(400, 600)
        self.feedback.maxsize(400, 600)
        self.feedback.config(bg = "#2e3440")

        #mid
        self.frame = tk.Frame(self.feedback, bg = "#d8dee9", width = 380, height = 580)
        self.frame.place(relx = 0.5, rely = 0.5, anchor = "center")

        #input box
        self.chatFeedback = tk.Text(self.feedback, borderwidth = 1, fg = "#2e3440", bg = "#eceff4")
        self.chatFeedback.place(relx = 0.5, rely = 0.5, anchor = "center", width = 360, height = 560)

        #send button
        self.sendButton  = tk.Button(self.feedback, text = "Send", bg = "#239B56", command = self.spawnDialog)
        self.sendButton.place(relx = 0.87, rely = 0.93, anchor = "center")

        #grab focus
        self.feedback.transient(self.subjectMenu)
        self.feedback.grab_set()
        self.subjectMenu.wait_window(self.feedback)

    def spawnDialog(self):
        self.popUpDialog()
        self.chatFeedback.delete("1.0", "end")

    def popUpDialog(self):
        # window
        self.popUpDialog = tk.Toplevel(self.subjectMenu)
        self.popUpDialog.title('Dialog')
        self.popUpDialog.config(bg = "#2e3441")
        self.popUpDialog.minsize(200, 100)
        self.popUpDialog.maxsize(200, 100)
        self.popUpDialog.grab_set()

        #mid
        self.frame = tk.Frame(self.popUpDialog, bg = "#d8dee9", width = 180, height = 80)
        self.frame.place(relx = 0.5, rely = 0.5, anchor = "center")

        #label text
        self.thankyouLabel = tk.Label(self.popUpDialog, text = "Thank you for your feedback!", bg = "#d8dee9", fg = "#2e3441")
        self.thankyouLabel.place(relx = 0.5, rely = 0.3, anchor = "center")

        # ok button
        self.okButton = tk.Button(self.popUpDialog, text = "Ok", command = self.popUpDialog.destroy, bg = "#239b56")
        self.okButton.place(relx = 0.5, rely = 0.7, anchor = "center")

    def run(self):
        self.subjectMenu.mainloop()

app = SubjectPage()
app.run()
