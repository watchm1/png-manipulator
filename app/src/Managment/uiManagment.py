import os
from tkinter import *
from tkinter import filedialog, colorchooser, messagebox
import tkinter
import numpy as np
from .Helper import Helper
from .sceneManagment import ScreenManager
from .ImageProccess.Manipulator import Manipualtor


class UIManager:
    def __init__(self):
        self.color_code = None
        self.gui = Tk()
        self.gui.title("PNG MANIPULATOR")
        self.gui.geometry("500x500")
        self.label = Label(self.gui, text="IMPORT YOUR PNG FILE")
        self.label.pack()
       ##############
        self.colorChooseButton = Button(
            text= "Choose Color",
            command= self.choose_color,
            height= 5,
            width= 15
        )
        self.button = Button(
            text = "Upload", 
            command = self.uploadAction,
            height=5,
            width=15)

        self.colorChooseButton.pack()
        self.colorChooseButton.place(x=185,y=180)
        self.button.pack()
        self.button.place(x=185,y=100)


    def choose_color(self):
        self.color_code = colorchooser.askcolor(title ="Choose color")
        return self.color_code
    def start(self):
        self.gui.mainloop()

    def uploadAction(self,event = None):
        if(self.color_code != None and self.color_code != (None,None)):
            self.filename = filedialog.askopenfilename()
            self.editedFileName = os.path.basename(self.filename)
            if(Helper.Helper.StringEmptyChecker(self.editedFileName)):
                self.screenManager = ScreenManager(self.editedFileName)
                self.runEditMode()
        else:
            messagebox.showerror("ERROR", "Please choose your color first")
        
    def runEditMode(self):
        while True:
            self.screenManager.new()
            self.screenManager.run()


