__author__ = 'Alex'

import pygame
import sys


screen = pygame.display.set_mode((576, 900))
clock = pygame.time.Clock()

# ------------------------------------------------< Images
# ------------Background--------------
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
# -------------Floor---------------------
floor = pygame.image.load('assets/base.png').convert()
floor = pygame.transform.scale2x(floor)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ------Blit background----
    screen.blit(bg_surface, (0,0))
    # ------Blit floor --------
    screen.blit(floor, (0, 800))

    pygame.display.update()
    clock.tick(120)