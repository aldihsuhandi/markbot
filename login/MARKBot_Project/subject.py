import tkinter as tk
from PIL import ImageTk,Image

class SubjectPage:

    def __init__(self):
        #Window
        self.subjectMenu = tk.Tk()
        self.subjectMenu.title('Subject Menu')
        self.subjectMenu.geometry('800x600')
        self.subjectMenu.config(bg="#2E3441")

        #header
        self.frame_blueheader = tk.Frame(self.subjectMenu)
        self.frame_blueheader.config(bg="#2E3441")
        self.frame_blueheader.grid(row=0,column=1)
        self.columnconfigure(1, minsize=800)

        #mid
        self.frame_mid = tk.Frame(self.subjectMenu)
        canvasImage = tk.Canvas(self.frame_mid, width = 200, height = 200)
        canvasImage.grid(row=1, column=0, padx=5,pady=5)

        img = ImageTk.PhotoImage(Image.open("cb.jpeg"))
        canvasImage.create_image(20,20, anchor="nw", image=img)

        #feedback
        img_feedback = tk.PhotoImage(file = r"C:\Users\Mbe\PycharmProjects\MARKBot_Project\feedback.png")
        self.button_feedback = tk.Button(self.frame_mid, image = img_feedback).grid(row=2,column=2)

