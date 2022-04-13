import pygame as pg
import sys
from settings import *
from sprites import *

class PngManipulator: 
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.bg = pg.image.load('background2.jpg')
        self.bg = pg.transform.scale(self.bg, (WIDTH, HEIGHT))
        self.screen.blit(self.bg, (0,0))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        # defination matrix array?
        
    def load_data(self):
        pass
    def new(self):
        #initialize all variables and do all the setup for a new page
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.screen.blit(self.bg, (0,0))
        self.user = Grid(self, 10, 10)
    def update(self):
        #update portion of the game loop
        self.all_sprites.update()
        self.events()
    def move(self):
        #game loop - setting user movement
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.update()
            self.draw()
    def draw(self):
        #draw screen
        self.screen.blit(self.bg, (0,0))
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def draw_grid(self):
        #drawing the grid
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    def events(self):
        #event listener
        self.old_mouse_pos = (0,0)
        self.new_mouse_pos = (0,0)
        # catching all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:  
                    self.user.move(dx = -1)
                if event.key == pg.K_RIGHT:
                    self.user.move(dx = 1)
                if event.key == pg.K_UP:
                    self.user.move(dy = -1)
                if event.key == pg.K_DOWN:
                    self.user.move(dy = 1)
                if event.key == pg.K_SPACE:
                    FilledGrid(self, self.user.x, self.user.y)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pose = pg.mouse.get_pos()
                convertedPosx = mouse_pose[0] // TILESIZE
                convertedPosy = mouse_pose[1] // TILESIZE
                self.user.x = convertedPosx
                self.user.y = convertedPosy
                FilledGrid(self, convertedPosx, convertedPosy)
            if event.type == pg.MOUSEMOTION:
                self.old_mouse_pos = self.new_mouse_pos
                self.new_mouse_pos = pg.mouse.get_pos()
                if self.new_mouse_pos != self.old_mouse_pos: 
                    pass        
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass