import pygame as pg
from constants import settings
class rect:
    def __init__(self, x, y,image: pg.surface = None):
        image.fill((192,192,192))
        self.rect = image.get_rect()
        self.x = x
        self.y = y
    
        