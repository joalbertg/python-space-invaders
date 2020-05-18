import pygame as pg

from ship import Ship
import constants as const

class Player(Ship):
    def __init__(self, x, y, health=100):
        super(Player, self).__init__(x, y, health)
        self.ship_img = const.YELLOW_SPACE_SHIP
        self.laser_img = const.YELLOW_LASER
        self.mask = pg.mask.from_surface(self.ship_img)
        self.max_health = health

