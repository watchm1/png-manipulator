import pygame as pg
from constants import settings

class FilledGrid(pg.sprite.Sprite):
    def __init__(self, manager, x, y):
        self.groups = manager.middleGround
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.surface.Surface((settings.TILESIZE, settings.TILESIZE))       
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.optimizePositions()
    def optimizePositions(self):
        self.rect.x = self.x * settings.TILESIZE
        self.rect.y = self.y * settings.TILESIZE
        self.x // settings.TILESIZE 
        self.y // settings.TILESIZE 
    def return_pos(self):
        return (self.x, self.y)


    