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

    def move_lasers(self, vel, objs):
        self.colldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(const.HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pg.draw.rect(window,
                (255, 0, 0),
                (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pg.draw.rect(window,
                (0, 255, 0),
                (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

