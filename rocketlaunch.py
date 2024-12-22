import pygame as pg
from sprites import Rocket
import sys as s

def main():
    ## VARIABLES ##

    fps = 40
    clock = pg.time.Clock()
    window_height = 800
    window_width = 800
    # sky_blue = (135, 206, 235)
    space_blue = (4, 12, 36)
    black = (0, 0, 0)
    
    increase_boost = False
    decrease_boost = False
    angle_right = False
    angle_left = False

    ## SETUP ##
    print("initializing")
    running = True
    pg.init()
    # window
    print("creating window")
    pg.display.set_caption('Rocket Launch')
    window = pg.display.set_mode((window_width, window_height))
    # background
    print("creating background")
    background = pg.surface.Surface((window_width*10, window_height*10))
    background_rect = background.get_rect()
    # space = pg.transform.scale(pg.image.load('assets/space.jpg'), (window_width*10, window_height*10))
    ground = pg.transform.scale(pg.image.load('assets/ground.png'), (window_width*10, window_height))
    # rocket
    print("creating rocket")
    rocket = Rocket(window_height*10, window_width*10)

    ## MAIN LOOP ##
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                try:
                    s.exit(0)
                finally:
                    running = False
            elif event.type == pg.KEYDOWN:
                if event.key == ord('q'):
                    try:
                        s.exit(0)
                    finally:    
                        running = False
                if event.key == pg.K_UP:
                    increase_boost = True
                    decrease_boost = False
                if event.key == pg.K_DOWN:
                    decrease_boost = True
                    increase_boost = False
                if event.key == pg.K_LEFT:
                    angle_left = True
                    angle_right = False
                if event.key == pg.K_RIGHT:
                    angle_right = True
                    angle_left = False
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    increase_boost = False
                if event.key == pg.K_DOWN:
                    decrease_boost = False
                if event.key == pg.K_LEFT:
                    angle_left = False
                if event.key == pg.K_RIGHT:
                    angle_right = False
                    
        # boost
        if increase_boost and rocket.boosting < 15:
            if rocket.boosting < 5.0:
                rocket.boosting = 5.0
            else:
                rocket.boosting += 0.1
        if decrease_boost and rocket.boosting > 0:
            if rocket.boosting < 5.0:
                rocket.boosting = 0.0
            else:
                rocket.boosting -= 0.1
            
        # angle
        if angle_right and rocket.y > 0:
            rocket.rocket_angle += 2
        if angle_left and rocket.y > 0:
            rocket.rocket_angle -= 2
        
        # reset background
        window.fill(black)
        # background.blit(space, (0, 0))
        background.fill(space_blue)
        background.blit(ground, (0, window_height*9))
        background_rect.x = (window_width / 2) - rocket.rect.centerx
        background_rect.y = (window_height / 2) - rocket.rect.centery

        # rocket
        rocket.update()
        background.blit(rocket.image, rocket.rect)
        
        # draw background
        window.blit(background, background_rect)
        
        pg.display.update()
        clock.tick(fps)
