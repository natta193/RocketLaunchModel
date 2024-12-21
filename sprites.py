import pygame as pg

class Rocket(pg.sprite.Sprite):
    def __init__(self, height, width):
        pg.sprite.Sprite.__init__(self)
        self.img = []
        self.image_no_flame = pg.transform.scale(pg.image.load('assets/rocket_no_flame.png'), (69, 121)).convert_alpha()
        self.img.append(self.image_no_flame)
        self.image = self.img[0]
        self.image_flame = pg.transform.scale(pg.image.load('assets/rocket_flame.png'), (69, 121)).convert_alpha()
        self.img.append(self.image_flame)
        self.window_height = height
        self.window_width = width
        self.rect = self.image.get_rect()
        self.rect.bottom = self.window_height * 0.9
        self.rect.centerx = self.window_width / 2
        self.v = [0, 0]
        self.angle = 0 # angle of rocket 0 is up
        self.boosting = 0
    
    def update(self):
        ## BOUNDS ##
        if self.rect.bottom < 200:
            self.rect.x += int(self.v[0])
            self.rect.y += int(self.v[1])
        self.vy -= (1/self.rect.y)**2 # gravity
        
    def accelerate(self):
        if self. boosting > 0:
            pass # calculate dv
        