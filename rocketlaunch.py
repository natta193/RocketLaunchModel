import pygame as pg
from sprites import Rocket
import sys as s

## VARIABES ##

fps = 40
clock = pg.time.Clock()
window_height = 600
window_width = 800
sky_blue = (135, 206, 235)
ground_color = (124, 252, 0)


## FUNCTIONS ## 

## SETUP ##

running = True
pg.init()
# window
pg.display.set_caption('Rocket Launch')
window = pg.display.set_mode((window_width, window_height))
window_rect = window.get_rect()
# background
background = pg.surface.Surface((window_width*100, window_height*100))
background.fill(())
# rocket
rocket = Rocket(window_height, window_width)

## MAIN LOOP ##
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            try:
                s.exit(0)
            finally:
                running = False
        elif event.type = pg.KEYDOWN:
            if event.key == ord('q'):
                try:
                    s.exit(0)
                finally:    
                    running = False
            if event.key == pg.K_UP:
                rocket.boosting += 0.1
            if event.key == pg.K_DOWN:
                rocket.boosting -= 0.1
            if event.key == pg.K_LEFT and rocket.boosting > 0:
                rocket.angle -= 2
            if event.key == pg.K_RIGHT and rocket.boosting > 0:
                rocket.angle += 2
    
    
