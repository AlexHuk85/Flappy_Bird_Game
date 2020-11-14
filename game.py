__author__ = 'Alex'

import pygame
import sys
import random


# ---------------Function-----------------------
def draw_floor():
    screen.blit(floor, (floor_x_pos, 800))
    screen.blit(floor, (floor_x_pos + 576, 800))


def create_pipe():
    random_height = random.choice(pipe_height)
    new_pipe = pipe.get_rect(midtop=(700, random_height))
    return new_pipe


def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipe(pipes):
    for p in pipes:
        screen.blit(pipe, p)


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

# -------------------Pipes---------------------
pipe = pygame.image.load('assets/pipe-green.png').convert()
pipe = pygame.transform.scale2x(pipe)
pipe_list = []
pipe_height = [x for x in range(250, 750)]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

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
        # -------------For spawn pipe every 1.2 second-----
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

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
    # -------Blit pipe----------
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)

    pygame.display.update()
    clock.tick(120)
