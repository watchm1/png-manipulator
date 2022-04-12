from numpy import empty, int32
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
        # defination matrix array?
        self.matrix = empty((WIDTH, HEIGHT), dtype=int32)

        print(self.matrix)
        with open('example.txt', 'w') as f:
            pass
            


        

    
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
        #draw screen
        self.screen.fill(BGCOLOR)
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
                    Wall(self, self.user.x, self.user.y)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                # how can i make mutlti selectable tiles?
                mouse_pose = pg.mouse.get_pos()
                convertedPosx = mouse_pose[0] // TILESIZE
                convertedPosy = mouse_pose[1] // TILESIZE
                Wall(self, convertedPosx, convertedPosy)
            if event.type == pg.MOUSEMOTION:
                self.old_mouse_pos = self.new_mouse_pos
                self.new_mouse_pos = pg.mouse.get_pos()
                if self.new_mouse_pos != self.old_mouse_pos:
                    self.user.move(dx = self.new_mouse_pos[0] - self.old_mouse_pos[0], dy = self.new_mouse_pos[1] - self.old_mouse_pos[1])
                    


         
    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


class RunProject():
    #main class
    #main function
    def __init__(self):
        runTime = PngManipulator()
        runTime.show_start_screen()
        while True:
            runTime.new()
            runTime.move()
            runTime.show_go_screen()

RunProject()