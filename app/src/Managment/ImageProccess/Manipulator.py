import cv2
import numpy as np
class Manipualtor:
    def __init__(self, img) -> None:
        self.newImg = cv2.imread(img, cv2.COLOR_RGB2RGBA)
        self.colors = cv2.cvtColor(self.newImg, cv2.COLOR_RGB2RGBA)
        
    def __execute(self):
        pass

    def proccessImg(self,img, color):
        self.__execute(img, color)

