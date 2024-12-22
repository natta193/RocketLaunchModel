import pygame as pg
from sprites import Rocket
import sys as s

def main():
    ## VARIABLES ##

    fps = 40
    clock = pg.time.Clock()
    window_height = 600
    window_width = 800
    sky_blue = (135, 206, 235)
    ground_color = (124, 252, 0)

    ## SETUP ##
    print("initializing")
    running = True
    pg.init()
    # window
    print("window")
    pg.display.set_caption('Rocket Launch')
    window = pg.display.set_mode((window_width, window_height))
    # background
    print("creating background")
    background = pg.surface.Surface((window_width*10, window_height*10))
    background_rect = background.get_rect()
    ground = pg.transform.scale(pg.image.load('assets/ground.png'), (window_width*10, window_height))
    # rocket
    print("creating rocket")
    rocket = Rocket(window_height, window_width)

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
                    rocket.boosting += 0.03
                if event.key == pg.K_DOWN and rocket.boosting > 0:
                    rocket.boosting -= 0.03
                if event.key == pg.K_LEFT and rocket.y > 0:
                    rocket.rocket_angle -= 1
                if event.key == pg.K_RIGHT and rocket.y > 0:
                    rocket.rocket_angle += 1
        # reset background
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
