__author__ = 'Alex'

import pygame
import sys
import random

pygame.init()
pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)


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
            death_sound.play()
            return False
    if bird_rect.top <= 10 or bird_rect.bottom >= 800:
        return False

    return True


def rotated_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird


def bird_animation():
    new_bird = bird_frame[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {(int(score))}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'Higher score: {(int(high_score))}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(288, 750))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


# ------------Screen --------------------------
screen = pygame.display.set_mode((576, 900))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04b_19.ttf', 40)
# ------------Background--------------
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
# -------------Floor---------------------
floor = pygame.image.load('assets/base.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
# --------------Bird----------------------------
# bird = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
# bird = pygame.transform.scale2x(bird)
# bird_rect = bird.get_rect(center=(100, 450))
# ------------------Creating Bird Animation---------
bird_up_flap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png')).convert_alpha()
bird_mid_flap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png')).convert_alpha()
bird_down_flap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png')).convert_alpha()

bird_frame = [bird_up_flap, bird_mid_flap, bird_down_flap]
bird_index = 0
bird_surface = bird_frame[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 500))

gravity = 0.32
bird_movement = 0

# -----------------Score -------------------------
score = 0
high_score = 0

# ---------------------Sound ------------------------
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
death_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# -------------------Pipes---------------------
pipe = pygame.image.load('assets/pipe-green.png').convert()
pipe = pygame.transform.scale2x(pipe)
pipe_list = []
pipe_height = [x for x in range(350, 650)]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(288, 450))

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
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 450)
                bird_movement = 0
                score = 0
        # ---------For Bird Animation -----------
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird_surface, bird_rect = bird_animation()

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
        roteted_bird = rotated_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(roteted_bird, bird_rect)
        # -------Blit pipe----------
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)

        if len(pipe_list) > 5:
            pipe_list.remove(pipe_list[0])

        game_active = check_collision(pipe_list)

        score += 0.01
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')

    pygame.display.update()
    clock.tick(120)
