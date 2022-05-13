
from Managment.sceneManagment import ScreenManager

class RunProject():
    #main class
    #main function
    def __init__(self):
        runTime = ScreenManager()
        
        while True:
            runTime.new()
            runTime.run()

RunProject()