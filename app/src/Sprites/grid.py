from distutils.log import debug
import pygame as pg
from constants import settings
from Sprites import rect

class Grid(pg.sprite.Sprite):
    def __init__(self, screenManager):
        self.rect = None
        self.selected = False
        self.groups = screenManager.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.mark_location(0,0)    

    @property
    def get_pos(self):
        return (self.x, self.y);
    def mark_location(self, x,y):
        
        
        self.image = pg.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.YELLOW)
        self.rectMark = self.image.get_rect()
        self.x = x
        self.y = y
        self.rectMark.x = self.x
        self.rectMark.y = self.y

    def select_grid(self, x, y):
        if(self.selected == False):
            self.rect = rect.rect(x,y, image= self.image)
            self.selected = True
            self.rect.x = self.rectMark.x
            self.rect.y = self.rectMark.y
    def deselect_grid(self, x ,y ):
        # if(self.selected):
        #     self.image.fill(settings.YELLOW)
        #     self.rect = self.image.get_rect()
        #     self.selected = False
        if(self.selected == True):
            #self.rect.destroy()
            self.selected = False
    def multi_mark(self, xmax, ymax):
        pass

    def multi_select(self, xmax, ymax):
        pass

    def multi_deselect(self, xmax, ymax):
        pass