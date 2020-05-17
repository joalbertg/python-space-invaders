import pygame as pg
import os
import time
import random

WIDTH, HEIGHT = 750, 750
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Space Shooter')

# Load images
BLUE_SPACE_SHIP = pg.image.load(os.path.join('assets', 'pixel_ship_blue_small.png'))
GREEN_SPACE_SHIP = pg.image.load(os.path.join('assets', 'pixel_ship_green_small.png'))
RED_SPACE_SHIP = pg.image.load(os.path.join('assets', 'pixel_ship_red_small.png'))

# Player ship
YELLOW_SPACE_SHIP = pg.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))

# Lasers
BLUE_LASER = pg.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
GREEN_LASER = pg.image.load(os.path.join('assets', 'pixel_laser_green.png'))
RED_LASER = pg.image.load(os.path.join('assets', 'pixel_laser_red.png'))
YELLOW_LASER = pg.image.load(os.path.join('assets', 'pixel_laser_yellow.png'))

# Background
BG = pg.image.load(os.path.join('assets', 'background-black.png'))

def main():
    run = True
    FPS = 60
    clock = pg.time.Clock()

    def redraw_windown():
        WIN.blit(BG, (0, 0))
        pg.display.update()

    while run:
        clock.tick(FPS)
        redraw_windown()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

main()

