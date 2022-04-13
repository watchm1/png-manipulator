from settings import *
from sprites import *
from Managment.sceneManagment import ScreenManager
from png_manipulator import PngManipulator

class RunProject():
    #main class
    #main function
    def __init__(self):
        runTime = ScreenManager()
        
        while True:
            runTime.new()
            runTime.run()
            

RunProject()