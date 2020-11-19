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
    bottom_pipe = pipe.get_rect(midtop=(700, random_height))
    top_pipe = pipe.get_rect(midbottom=(700, random_height - 300))
    return bottom_pipe, top_pipe


def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipe(pipes):
    for p in pipes:
        if p.bottom >= 900:
            screen.blit(pipe, p)
        else:
            flip_pipe = pygame.transform.flip(pipe, False, True)
            screen.blit(flip_pipe, p)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= 10 or bird_rect.bottom >= 800:
        return False

    return True


def rotated_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird


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
bird = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center=(100, 450))
gravity = 0.35  
bird_movement = 0

# -------------------Pipes---------------------
pipe = pygame.image.load('assets/pipe-green.png').convert()
pipe = pygame.transform.scale2x(pipe)
pipe_list = []
pipe_height = [x for x in range(350, 650)]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

game_active = True

while True:
    for event in pygame.event.get():
        # -------------For QUIT Game------------------------
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # --------------For Controlling Bird----------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 10
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 450)
                bird_movement = 0

        # -------------For spawn pipe every 1.2 second-----
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe()) # append = 1 item, extend = tuple

    # ------Blit background----
    screen.blit(bg_surface, (0, 0))
    # ------Blit floor --------
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    if game_active:
        # ------Blit Bird ---------
        bird_movement += gravity
        roteted_bird = rotated_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(roteted_bird, bird_rect)
        # -------Blit pipe----------
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)

        if len(pipe_list) > 5:
            pipe_list.remove(pipe_list[0])

        game_active = check_collision(pipe_list)

    pygame.display.update()
    clock.tick(120)
