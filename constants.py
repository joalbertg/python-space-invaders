import pygame as pg
import os

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

BACKGROUND = pg.image.load(os.path.join('assets', 'background-black.png'))

