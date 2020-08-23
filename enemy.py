import pygame as pg

from ship import Ship
from laser import Laser
import constants as const


class Enemy(Ship):
    COLOR_MAP = {
        "blue": (const.BLUE_SPACE_SHIP, const.BLUE_LASER),
        "green": (const.GREEN_SPACE_SHIP, const.GREEN_LASER),
        "red": (const.RED_SPACE_SHIP, const.RED_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super(Enemy, self).__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pg.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
