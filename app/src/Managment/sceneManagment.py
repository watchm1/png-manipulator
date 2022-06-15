import pygame as pg
from Managment import gridManagment
from constants.settings import *
 
class ScreenManager(): 
    def __init__(self, image, choosen_color):
        # Screen Managment
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.img = image
        self.color_code = choosen_color
        self.bg = pg.image.load(image)
        self.bg = pg.transform.scale(self.bg, (WIDTH, HEIGHT))
        self.screen.blit(self.bg, (0,0))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.middleGround = pg.sprite.Group()
        self.background = pg.sprite.Group()
        self.gridManager = gridManagment.GridManager(manager = self, col = HEIGHT // TILESIZE, row = WIDTH // TILESIZE)
    def load_data(self):
        pass

    def new(self):
        self.background = pg.sprite.Group()
        self.middleGround = pg.sprite.Group()
        self.gridManager = gridManagment.GridManager(self)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) /1000
            
            self.update()
            self.draw()
            self.events()

    def update(self):
        self.background.update()
        self.middleGround.update()

    def quit(self):
        pg.quit()
    
    def draw(self):
        self.screen.blit(self.bg, (0,0))
        self.background.draw(self.screen)
        self.gridManager.draw_grid_map()
        self.middleGround.draw(self.screen)
        pg.display.flip()
    
    
        

    def events(self):
        self.mousePose = (0,0)
        self.convertedX = 0
        self.convertedY = 0
        self.clicked = False
        
        self.old_mouse_pos = (0,0)
        self.new_mouse_pos = (0,0)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYUP:
                if event.key == pg.K_LCTRL:
                    self.clicked = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RCTRL:
                    if(self.gridManager.tiles != None or self.gridManager.tiles != []):
                        self.gridManager.imageManipulator.getImage(self.img, self.gridManager.tiles, settings= TILESIZE)
                        self.gridManager.imageManipulator.execute(self.color_code)
                        pg.quit()
                if event.key == pg.K_x:
                    self.gridManager.unselectTile()
                if event.key == pg.K_LCTRL:
                    self.clicked= True
            if event.type == pg.MOUSEBUTTONDOWN and event.button ==1:
                mousePose = pg.mouse.get_pos()
                convertedX = mousePose[0] // TILESIZE
                convertedY = mousePose[1] // TILESIZE
                self.gridManager.selectTile(x = convertedX, y = convertedY) 
            if event.type ==  pg.MOUSEMOTION:
                self.mousePose = pg.mouse.get_pos()
                self.convertedX = self.mousePose[0] // TILESIZE
                self.convertedY = self.mousePose[1] // TILESIZE
                if self.clicked == True : 
                    self.gridManager.selectTile(x = self.convertedX, y = self.convertedY)
                    