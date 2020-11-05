__author__ = 'Alex'

import pygame
import sys


screen = pygame.display.set_mode((576, 900))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()