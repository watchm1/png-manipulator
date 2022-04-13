import pygame as pg
from settings import *

class Grid(pg.sprite.Sprite):
    def __init__(self, runTime, x, y, xmax=0, ymax=0,  rectHeight=0, rectWidth=0):
        self.groups = runTime.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.run_time = runTime
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    

class FilledGrid(pg.sprite.Sprite):
    def __init__(self, runTime, x, y):
        self.groups = runTime.all_sprites, runTime.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.run_time = runTime
        self.x = x
        self.y = y
        
    
    def get_filled_grid(self):
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill((192,192,192))
        self.rect = self.image.get_rect()
        self.rect.x = self.x*TILESIZE
        self.rect.y = self.y*TILESIZE
