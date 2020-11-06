__author__ = 'Alex'

import pygame
import sys


screen = pygame.display.set_mode((576, 900))
clock = pygame.time.Clock()

# ------------------------------------------------< Images
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0,0))

    pygame.display.update()
    clock.tick(120)