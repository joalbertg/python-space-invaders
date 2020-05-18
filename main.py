import pygame as pg
import os
import time
import random

from player import Player
from enemy import Enemy
import constants as const

pg.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Space Shooter')

# Background
BG = pg.transform.scale(const.BACKGROUND, (WIDTH, HEIGHT))

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pg.font.SysFont('comicsans', 50)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5

    player = Player(300, 650)

    clock = pg.time.Clock()

    def redraw_windown():
        WIN.blit(BG, (0, 0))

        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        pg.display.update()

    while run:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            wave_length += 5

            for i in range(wave_length):
                enemy = Enemy(
                            random.randrange(50, WIDTH-100),
                            random.randrange(-1500, -100),
                            random.choice(['blue', 'green', 'red']))
                enemies.append(enemy)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()

        if keys[pg.K_a] and player.x - player_vel > 0 : # left
            player.x -= player_vel
        if keys[pg.K_d] and player.x + player_vel < WIDTH - player.get_width(): # right
            player.x += player_vel
        if keys[pg.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pg.K_s] and player.y + player_vel < HEIGHT - player.get_height(): # down
            player.y += player_vel

        for enemy in enemies:
            enemy.move(enemy_vel)

        redraw_windown()

main()

