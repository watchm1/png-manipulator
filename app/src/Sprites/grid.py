import pygame as pg
from constants import settings

class Grid(pg.sprite.Sprite):
    def __init__(self, manager,x, y):
        self.selected = False
        self.groups = manager.middleGround
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.surface.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.YELLOW)
        self.rect = self.image.get_rect()
        self.manager = manager
        self.x = x
        self.y = y
    
    def optimizePositions(self):
        self.rect.x = self.x * settings.TILESIZE
        self.rect.y = self.y * settings.TILESIZE
        self.x // settings.TILESIZE 
        self.y // settings.TILESIZE 
    @property
    def get_pos(self):
        return (self.x, self.y);

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


    