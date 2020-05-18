import pygame as pg
import os
import time
import random

from player import Player
from enemy import Enemy
from helpers import collide
import constants as const

pg.font.init()

WIN = pg.display.set_mode((const.WIDTH, const.HEIGHT))
pg.display.set_caption('Space Shooter')

# Background
BG = pg.transform.scale(const.BACKGROUND, (const.WIDTH, const.HEIGHT))

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    lost = False
    lost_count = 0
    main_font = pg.font.SysFont('comicsans', 50)
    lost_font = pg.font.SysFont('comicsans', 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    laser_vel = 5

    player = Player(300, 650)

    clock = pg.time.Clock()

    def redraw_windown():
        WIN.blit(BG, (0, 0))

        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (const.WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render(f"You Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (const.WIDTH/2 - lost_label.get_width()/2, 350))

        pg.display.update()

    while run:
        clock.tick(FPS)
        redraw_windown()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5

            for i in range(wave_length):
                enemy = Enemy(
                            random.randrange(50, const.WIDTH-100),
                            random.randrange(-1500, -100),
                            random.choice(['blue', 'green', 'red']))
                enemies.append(enemy)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()

        if keys[pg.K_a] and player.x - player_vel > 0 : # left
            player.x -= player_vel
        if keys[pg.K_d] and player.x + player_vel < const.WIDTH - player.get_width(): # right
            player.x += player_vel
        if keys[pg.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pg.K_s] and player.y + player_vel < const.HEIGHT - player.get_height(): # down
            player.y += player_vel
        if keys[pg.K_SPACE]:
            player.shoot()

        # create a copy of this list with '[:]'
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*FPS) == 1:
                enemy.shoot()
                enemy.move_lasers(laser_vel, player)

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > const.HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

main()

