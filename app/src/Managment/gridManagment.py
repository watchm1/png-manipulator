from Sprites import grid
from constants import settings
import pygame as pg


class GridManager:
    def __init__(self, manager, col=0, row=0):
        # definin matrix of locations
        self.cols = col
        self.rows = row
        self.tiles = []
        self.screen = manager.screen
        self.manager = manager
        self.create_in_scene(manager, 0, 0)

    def create_in_scene(self, manager, x, y):
        self.grid = grid.Grid(manager=manager, x=x, y=y)

    def moving_in_gridSystem(self, xLen=0, yLen=0):

        self.grid.x += xLen
        self.grid.y += yLen
        self.grid.optimizePositions()

    def unselectTile(self):
        length = len(self.manager.middleGround.sprites())
        self.manager.middleGround.remove(
            self.manager.middleGround.sprites()[1:length])
        self.tiles.clear()
        print(self.tiles)

    def selectTile(self, x, y):
        if (x, y) not in self.tiles:
            self.tile = grid.FilledGrid(manager=self.manager, x=x, y=y)
            self.tile.image.fill((255, 255, 255))
            self.tile.image.set_alpha(80)
            print(self.tiles)
            self.tiles.append((x, y))

    def draw_grid_map(self):
        for x in range(0, settings.WIDTH, settings.TILESIZE):
            pg.draw.line(self.screen, settings.LIGHTGREY,
                         (x, 0), (x, settings.HEIGHT))
        for y in range(0, settings.HEIGHT, settings.TILESIZE):
            pg.draw.line(self.screen, settings.LIGHTGREY,
                         (0, y), (settings.WIDTH, y))
