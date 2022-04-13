from Sprites import grid 
from constants import settings
from Managment import sceneManagment
import pygame as pg
class GridManager:
    def __init__(self, screenManager,screen,col=0, row=0):
        self.cols = col
        self.screen = screen
        self.screenmanager = screenManager
        self.rows = row
        # definin matrix of locations
        #self.locations = [[0 for x in range(self.cols)] for y in range(self.rows)]
        
        self.grid = grid.Grid(screenManager= self.screenmanager)
        
        pass
    def updatingLocations(self):
        if(self.grid.selected == True):
            self.locations[self.grid.x][self.grid.y] = 1
        else: self.locations[self.grid.x][self.grid.y] = 0
        # this function adding a new location inside array
        # when we use deselect function we need to remove the last location    
    def moving_in_gridSystem(self, xLen = 0, yLen = 0):
        self.grid.x += xLen
        self.grid.y += yLen
        self.grid.mark_location(x = self.grid.x, y = self.grid.y)
    def select_tile(self, x,y):
        self.updatingLocations()
        if(self.grid.selected == False):
            self.grid.select_grid(x,y)
        else: self.grid.deselect_grid(x,y)
    def draw_grid_map(self):
        for x in range (0, settings.WIDTH, settings.TILESIZE):
            pg.draw.line(self.screen, settings.LIGHTGREY, (x, 0), (x, settings.HEIGHT))
        for y in range (0, settings.HEIGHT, settings.TILESIZE):
            pg.draw.line(self.screen, settings.LIGHTGREY, (0, y), (settings.WIDTH, y))




