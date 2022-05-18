from tkinter import *
from tkinter import filedialog
from .sceneManagment import ScreenManager


class UIManager:
    def __init__(self):
        self.gui = Tk()
        self.gui.title("PNG MANIPULATOR")
        self.gui.geometry("500x500")
        self.label = Label(self.gui, text="IMPORT YOUR PNG FILE")
        self.label.pack()
        self.button = Button(
            text = "Upload", 
            command = self.uploadAction,
            height=5,
            width=15)

        self.button.pack()
        self.button.place(x=185,y=100)


    def start(self):
        self.gui.mainloop()
    def uploadAction(self,event = None):
        self.filename = filedialog.askopenfilename()
        print("You selected: " + self.filename)
        self.screenManager = ScreenManager(self.filename)
        self.runEditMode()
        
    def runEditMode(self):
        while True:
            self.screenManager.new()
            self.screenManager.run()


