import tkinter as tk
from Managment.sceneManagment import ScreenManager
from Managment.uiManagment import UIManager
class RunProject():
    #main class
    #main function
    def __init__(self):
        manager = UIManager()
        manager.start()
        #runTime = ScreenManager()
        
        # while True:
        #     runTime.new()
        #     runTime.run()


RunProject()