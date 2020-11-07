__author__ = 'Alex'

import pygame
import sys


# Function


screen = pygame.display.set_mode((576, 900))
clock = pygame.time.Clock()

# ------------------------------------------------< Images
# ------------Background--------------
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
# -------------Floor---------------------
floor = pygame.image.load('assets/base.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ------Blit background----
    screen.blit(bg_surface, (0,0))
    # ------Blit floor --------
    floor_x_pos -= 1
    screen.blit(floor, (floor_x_pos, 800))

    pygame.display.update()
    clock.tick(120)