__author__ = 'Alex'

import pygame
import sys


# ---------------Function-----------------------
def draw_floor():
    screen.blit(floor, (floor_x_pos, 800))
    screen.blit(floor, (floor_x_pos + 576, 800))


# ------------Screen --------------------------
screen = pygame.display.set_mode((576, 900))
clock = pygame.time.Clock()
# ------------Background--------------
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
# -------------Floor---------------------
floor = pygame.image.load('assets/base.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
# --------------Bird----------------------------
bird = pygame.image.load('assets/bluebird-midflap.png').convert()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center=(100, 500))
gravity = 0.25
bird_movement = 0

while True:
    for event in pygame.event.get():
        # -------------For QUIT Game------------------------
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # --------------For Controlling Bird----------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 10
                if bird_rect.centery <= 0:
                    bird_rect.centery = 0


    # ------Blit background----
    screen.blit(bg_surface, (0, 0))
    # ------Blit floor --------
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0
    # ------Blit Bird ---------
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird, bird_rect)

    pygame.display.update()
    clock.tick(120)
