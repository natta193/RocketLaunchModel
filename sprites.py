import pygame as pg
import math
import sys as s

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
        self.floor = self.window_height * 9
        self.rect = self.image.get_rect()
        self.rect.bottom = self.floor
        self.rect.centerx = self.window_width / 2
        self.x = float(self.rect.x)
        self.y = 0
        self.v = [0, 0]
        self.a = [0, 0]
        self.rocket_angle = 0 # angle of rocket 0 is up
        self.boosting = 0
        self.gravity = 1
    
    def update(self):
        self.a = [0, 0]
        
        # accelerate
        if self.boosting > 0:
            self.a[1] += (math.cos(math.radians(abs(self.rocket_angle))) * self.boosting)
            if self.rocket_angle > 0:
                self.a[0] += (math.sin(math.radians(abs(self.rocket_angle))) * self.boosting)
            elif self.rocket_angle < 0:
                self.a[0] -= (math.sin(math.radians(abs(self.rocket_angle))) * self.boosting)
            
        # gravity
        if self.y > 0: 
            self.gravity = 10 * (1 - ((2*self.y) / self.window_height*100))
            if self.gravity < 0.1:
                self.gravity = 0.1
            self.a[1] -= self.gravity * 0.1
                
        # update velocity
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
                
        # update position
        self.x += self.v[0]
        self.y += self.v[1]

        ## BOUNDS ##
        if self.y < 0:
            self.y = 0
            if self.v[1] < 0:
                self.v[1] *= -0.1
                if 0 < self.v[1] < 0.01:
                    self.v[0], self.v[1] = 0, 0 # vel
                    self.a[0], self.a[1] = 0, 0 # accel
        
        # image
        if self.boosting > 0:
            self.image = self.img[1]
        else:
            self.image = self.img[0]
            
        # track stats
        s.stdout.write(f"{self.a[0]=:.2f}, {self.a[1]=:.2f}, {self.v[0]=:.2f}, {self.v[1]=:.2f}, {self.x=:.2f}, {self.y=:.2f} {self.rocket_angle=:.2f} {self.boosting=:.2f} {self.gravity=:.2f}     \r")
        s.stdout.flush()
        
        # update rect
        self.rect.x = int(self.x)
        self.rect.bottom = -int(self.y) + self.floor
