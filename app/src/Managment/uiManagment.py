import os
from tkinter import *
import customtkinter as ct
from tkinter import filedialog, colorchooser, messagebox
from .Helper import Helper
from .sceneManagment import ScreenManager
from .ImageProccess.Manipulator import Manipualtor

class UIManager:
    def __init__(self):
        
        ct.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
        ct.set_default_color_theme("dark-blue")
        self.color_code = None
        self.gui = Tk()
        self.gui.title("PNG MANIPULATOR")
        self.gui.geometry("400x400")
        self.gui.configure(background="Gray")
        self.canvas = ct.CTkCanvas(self.gui)
        self.label = ct.CTkLabel(self.gui, text="IMPORT YOUR PNG FILE", fg_color="blue", height=30)
        self.label.pack()
        self.label.place(x = 120, y = 50)
       ##############
        
        self.colorChooseButton = ct.CTkButton(
            text= "Choose Color",
            command= self.choose_color,
            height= 30,
            width= 30,
            
        )
        self.button = ct.CTkButton(
            text = "Upload", 
            command = self.uploadAction,
            height=30,
            width=30)

        self.colorChooseButton.pack()
        self.colorChooseButton.place(x=150,y=180)
        self.button.pack()
        self.button.place(x=165,y=140)
    
    def choose_color(self):
        self.color_code = colorchooser.askcolor(title ="Choose color")
        self.color = self.color_code
    
    def start(self):
        self.gui.mainloop()
    def uploadAction(self,event = None):
        if(self.color_code != None and self.color_code != (None,None)):
            self.filename = filedialog.askopenfilename()
            self.editedFileName = os.path.basename(self.filename)
            if(Helper.Helper.StringEmptyChecker(self.editedFileName)):
                self.screenManager = ScreenManager(self.editedFileName, self.color[0])
                self.runEditMode()
        else:
            messagebox.showerror("ERROR", "Please choose your color first")
    def runEditMode(self):
        while True:
            self.screenManager.new()
            self.screenManager.run()


