import cv2 as cv
from tkinter import *
class Manipualtor:
    def __init__(self) -> None:
        self.img = None
    def getImage(self, img, locations, settings):
        self.locations = locations
        self.settings = settings
        self.img = cv.imread(img, cv.COLOR_RGB2BGR )
    def manipulate(self, color_code):
        #1->3
        #2->2
        #3->
        print(color_code)
        try:
            for i in self.locations:
                self.img[i[1]*self.settings:i[1]*self.settings+self.settings, i[0]*self.settings:i[0]*self.settings+self.settings,] = (color_code[2], color_code[1], color_code[0])
            cv.imshow("Edited Image",self.img)
            return True
        except:
            print("error")
            return False
    def execute(self, color_code):
        if(self.manipulate(color_code) is True):
            status = cv.imwrite("edited.jpg", self.img)
            print("STATUS : ", status) 
            
            
        
