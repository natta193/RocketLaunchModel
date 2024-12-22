import pygame as pg
from sprites import Rocket
import sys as s

def main():
    ## VARIABLES ##

    fps = 40
    clock = pg.time.Clock()
    window_height = 800
    window_width = 800
    sky_blue = (135, 206, 235)
    black = (0, 0, 0)
    
    increase_boost = False
    decrease_boost = False

    ## SETUP ##
    print("initializing")
    running = True
    pg.init()
    # window
    print("window")
    pg.display.set_caption('Rocket Launch')
    window = pg.display.set_mode((window_width, window_height))
    print(f"{window_width=}, {window_height=}")
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
                if event.key == pg.K_LEFT and rocket.y > 0:
                    rocket.rocket_angle -= 1
                if event.key == pg.K_RIGHT and rocket.y > 0:
                    rocket.rocket_angle += 1
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    increase_boost = False
                if event.key == pg.K_DOWN:
                    decrease_boost = False
                    
        # boost
        if increase_boost and rocket.boosting < 15:
            rocket.boosting += 0.1
        if decrease_boost and rocket.boosting > 0:
            rocket.boosting -= 0.1
        
        # reset background
        window.fill(black)
        # background.blit(space, (0, 0))
        background.fill(sky_blue)
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
