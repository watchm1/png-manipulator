import pygame as pg
from Managment import gridManagment
from constants.settings import * 
class ScreenManager: 
    def __init__(self):
        # Screen Managment
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.bg = pg.image.load('background2.jpg')
        self.bg = pg.transform.scale(self.bg, (WIDTH, HEIGHT))
        self.screen.blit(self.bg, (0,0))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        
    def is_running(self):
        self.running = True
        while self.running:
            self.date = self.clock.tick(FPS) / 1000
            self.update()
            self.draw()

    def new(self):
        #initialize all variables and do all the setup for a new page
        self.all_sprites = pg.sprite.Group()
        self.screen.blit(self.bg, (0,0))
        #self.user = Grid(self, 10, 10)
        self.gridManager = gridManagment.GridManager(screenManager = self, screen = self.screen, col = HEIGHT // TILESIZE, row = WIDTH // TILESIZE)
        


    def draw(self):
        self.screen.blit(self.bg, (0,0))
        self.gridManager.draw_grid_map()
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        
    def update(self):
        # updating stuff
        self.all_sprites.update()
        self.events()
        
        
    def quit():
        pg.quit()
    def events(self):
        self.old_mouse_pos = (0,0)
        self.new_mouse_pos = (0,0)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.gridManager.moving_in_gridSystem(xLen= -1 * TILESIZE)
                if event.key == pg.K_RIGHT:
                    self.gridManager.moving_in_gridSystem(xLen= 1 * TILESIZE)
                if event.key == pg.K_UP:
                    self.gridManager.moving_in_gridSystem(yLen= -1 * TILESIZE)
                if event.key == pg.K_DOWN:
                    self.gridManager.moving_in_gridSystem(yLen= 1 * TILESIZE)
            
            if event.type == pg.MOUSEBUTTONDOWN and event.button ==1:
                mouse_pose = pg.mouse.get_pos()
                convertedPosX = mouse_pose[0] // TILESIZE
                convertedPosY = mouse_pose[1] // TILESIZE
                self.gridManager.grid.x = convertedPosX
                self.gridManager.grid.y = convertedPosY
                self.gridManager.select_tile(convertedPosX, convertedPosY)
            if event.type == pg.MOUSEMOTION:
                self.old_mouse_pos = self.new_mouse_pos
                self.new_mouse_pos = pg.mouse.get_pos()
                if self.old_mouse_pos != self.new_mouse_pos:
                    self.gridManager.grid.x = self.new_mouse_pos[0] // TILESIZE
                    self.gridManager.grid.y = self.new_mouse_pos[1] // TILESIZE
        
    
