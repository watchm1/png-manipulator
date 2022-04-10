import pygame as pg
import sys
from settings import *
from sprites import *

class PngManipulator: 
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
    
    def load_data(self):
        pass

    
    def new(self):
        #initialize all variables and do all the setup for a new page
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.user = User(self, 10, 10)
        for x in range(10,20):
            Wall(self, x, 10)
            
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
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def events(self):
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
                if event.key == pg.MOUSEBUTTONDOWN:
                    mouse_pose = pg.mouse.get_pos()
                    self.user.move(dx = self.user.x + mouse_pose.x)
                if event.key == pg.K_SPACE:
                    Wall(self, self.user.x, self.user.y)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

runTime = PngManipulator()
runTime.show_start_screen()
while True:
    runTime.new()
    runTime.move()
    runTime.show_go_screen()