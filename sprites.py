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
        self.floor = self.window_height * 0.9
        self.rect = self.image.get_rect()
        self.rect.bottom = self.floor
        self.rect.centerx = self.window_width / 2
        self.x = float(self.rect.x)
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.rocket_angle = 0 # angle of rocket 0 is up
        self.boosting = 0
        self.gravity = 9.81
        self.air_resistance = 0.99
    
    def update(self):
        self.ax, self.ay = 0, 0
        
        # thrust
        if self.boosting > 0:
            thrust = self.boosting
            angle_rad = math.radians(self.rocket_angle)
            self.ay += math.cos(angle_rad) * thrust
            self.ax += math.sin(angle_rad) * thrust * 0.1
            
        # gravity
        self.ay -= self.gravity
                
        # air resistance
        self.vx *= self.air_resistance
        self.vy *= self.air_resistance
                
        # update velocity
        self.vx += self.ax
        self.vy += self.ay
                
        # update displacement
        self.x += self.vx
        self.y += self.vy

        ## BOUNDARIES ##
        # ensure rocket stays above ground
        if self.y < 0:
            self.y = 0
            self.vy = 0
        # ensure rocket doesn't go too high
        top_boundary = self.window_height - self.rect.height
        if self.y > top_boundary:
            self.y = top_boundary
            self.vy = 0
        # ensure the rocket does not go within the last 1/10 of either side of the screen
        left_boundary = (self.rect.width/2)
        right_boundary = self.window_width - (self.rect.width/2)
        if self.x < left_boundary:
            self.x = left_boundary
            self.vx = 0
        elif self.x > right_boundary:
            self.x = right_boundary
            self.vx = 0
        
        # image
        if self.boosting > 0:
            self.image = pg.transform.rotate(self.img[1], -self.rocket_angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.image = self.img[0]
            
        # track stats
        s.stdout.write(f"{self.ax=:.2f}, {self.ay=:.2f}, {self.vx=:.2f}, {self.vy=:.2f}, {self.x=:.2f}, {self.y=:.2f} {self.rocket_angle=:.2f} {self.boosting=:.2f}     \r")
        s.stdout.flush()
        
        # update rect
        self.rect.centerx = int(self.x)
        self.rect.bottom = self.floor -int(self.y)
