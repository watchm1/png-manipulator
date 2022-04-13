from Sprites import grid
from constants import settings
import pygame as pg
class GridManager:
    def __init__(self, manager,col=0, row=0):
        # definin matrix of locations
        self.cols = col
        self.rows = row
        self.locations = []
        self.screen = manager.screen
        self.manager = manager
        self.create_in_scene(manager = manager)
        

    def create_in_scene(self, manager):
        self.grid = grid.Grid(manager = manager, x= 0,y= 0)
    
    def updatingLocations(self, selectedTile):
        self.locations.append(selectedTile)
        # this function adding a new location inside array
        # when we use deselect function we need to remove the last location 
        print(self.locations)  

    def moving_in_gridSystem(self, xLen = 0, yLen = 0):
        self.grid.x += xLen
        self.grid.y += yLen
        self.grid.optimizePositions()
        

    def select_tile(self, x,y):
        self.selectedTile = grid.FilledGrid(manager = self.manager, x= x, y= y)
        self.updatingLocations(selectedTile= self.selectedTile.return_pos())
        pass
    def draw_grid_map(self):
        for x in range (0, settings.WIDTH, settings.TILESIZE):
            pg.draw.line(self.screen, settings.LIGHTGREY, (x, 0), (x, settings.HEIGHT))
        for y in range (0, settings.HEIGHT, settings.TILESIZE):
            pg.draw.line(self.screen, settings.LIGHTGREY, (0, y), (settings.WIDTH, y))




