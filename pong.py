# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (C) 2020
# Jens Hannemann, Kentucky State University, jens.hannemann@kysu.edu

import sys
from math import sin, cos, radians
import random
import pygame
from pygame.locals import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BOUNDARY_THICKNESS = 5

NET_WIDTH = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_OFFSET = 10
PADDLE_SPEED = 10

# paddle states
PADDLE_STOP = 'stop'
PADDLE_UP = 'up'
PADDLE_DOWN = 'down'

# game states
GAME_ON = 'on'
GAME_STOP = 'stop'
GAME_OVER = 'over'

FRAMES_PER_SECOND = 30

BALL_SPEED = 8
BALL_SIZE = 9

MAX_ANGLE = 30

MAX_SCORE = 11
SCORE_POS_Y = 30
SCORE_POS_LEFT = WINDOW_WIDTH/4
SCORE_POS_RIGHT = WINDOW_WIDTH * 3/4

NET = pygame.Rect(WINDOW_WIDTH/2 - NET_WIDTH/2, 0, NET_WIDTH, WINDOW_HEIGHT)

TOP_BOUNDARY = pygame.Rect(0,
                           0,
                           WINDOW_WIDTH,
                           BOUNDARY_THICKNESS)
BOTTOM_BOUNDARY = pygame.Rect(0,
                              WINDOW_HEIGHT - BOUNDARY_THICKNESS,
                              WINDOW_WIDTH,
                              BOUNDARY_THICKNESS)
LEFT_BOUNDARY = pygame.Rect(0,
                            0,
                            BOUNDARY_THICKNESS,
                            WINDOW_HEIGHT)
RIGHT_BOUNDARY = pygame.Rect(WINDOW_WIDTH - BOUNDARY_THICKNESS,
                             0,
                             BOUNDARY_THICKNESS,
                             WINDOW_HEIGHT)
left_paddle = pygame.Rect(BOUNDARY_THICKNESS + PADDLE_OFFSET,
                          WINDOW_HEIGHT/2 - PADDLE_HEIGHT/2,
                          PADDLE_WIDTH,
                          PADDLE_HEIGHT)
right_paddle = pygame.Rect(WINDOW_WIDTH - BOUNDARY_THICKNESS -
                           PADDLE_OFFSET - PADDLE_WIDTH,
                           WINDOW_HEIGHT/2 - PADDLE_HEIGHT/2,
                           PADDLE_WIDTH,
                           PADDLE_HEIGHT)

left_paddle_state = PADDLE_STOP
right_paddle_state = PADDLE_STOP

ball = pygame.Rect(WINDOW_WIDTH/2 - BALL_SIZE/2,
                   WINDOW_HEIGHT/2 - BALL_SIZE/2,
                   BALL_SIZE,
                   BALL_SIZE)

ball_speed_x = BALL_SPEED
ball_speed_y = 0

game_state = GAME_OVER
left_score = 0
right_score = 0

pygame.init()
FONT = pygame.font.Font('freesansbold.ttf', 24)
GAME_OVER_SURFACE = FONT.render('GAME     OVER ',
                                True, WHITE)
GAME_OVER_RECT = GAME_OVER_SURFACE.get_rect()
GAME_OVER_RECT.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
FPS_CLOCK = pygame.time.Clock()

# set up the window
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

# main game loop
while True:
    # process events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            # update game state
            if game_state == GAME_OVER or game_state == GAME_STOP:
                # pick initial angle
                angle = radians(random.randint(-MAX_ANGLE, +MAX_ANGLE))
                ball_speed_x = BALL_SPEED * cos(angle)
                ball_speed_y = BALL_SPEED * sin(angle)
                # pick initial direction
                ball_speed_x *= random.choice((-1, 1))
                # reset score
                if game_state == GAME_OVER:
                    left_score = 0
                    right_score = 0
                game_state = GAME_ON
            # update paddle state
            if event.key == K_w and left_paddle_state == PADDLE_STOP:
                left_paddle_state = PADDLE_UP
            elif event.key == K_s and left_paddle_state == PADDLE_STOP:
                left_paddle_state = PADDLE_DOWN
            elif event.key == K_UP and right_paddle_state == PADDLE_STOP:
                right_paddle_state = PADDLE_UP
            elif event.key == K_DOWN and right_paddle_state == PADDLE_STOP:
                right_paddle_state = PADDLE_DOWN
        elif event.type == KEYUP:
            # update paddle state
            if event.key == K_w and left_paddle_state == PADDLE_UP:
                left_paddle_state = PADDLE_STOP
            elif event.key == K_s and left_paddle_state == PADDLE_DOWN:
                left_paddle_state = PADDLE_STOP
            elif event.key == K_UP and right_paddle_state == PADDLE_UP:
                right_paddle_state = PADDLE_STOP
            elif event.key == K_DOWN and right_paddle_state == PADDLE_DOWN:
                right_paddle_state = PADDLE_STOP

    # update game state
    if game_state == GAME_ON:
        if left_paddle_state == PADDLE_UP:
            left_paddle.y -= PADDLE_SPEED
        elif left_paddle_state == PADDLE_DOWN:
            left_paddle.y += PADDLE_SPEED
        
        if right_paddle_state == PADDLE_UP:
            right_paddle.y -= PADDLE_SPEED
        elif right_paddle_state == PADDLE_DOWN:
            right_paddle.y += PADDLE_SPEED

        # stop paddles at top and bottom boundaries
        if left_paddle.colliderect(TOP_BOUNDARY):
            left_paddle_state = PADDLE_STOP
            left_paddle.top = TOP_BOUNDARY.bottom
        if left_paddle.colliderect(BOTTOM_BOUNDARY):
            left_paddle_state = PADDLE_STOP
            left_paddle.bottom = BOTTOM_BOUNDARY.top

        if right_paddle.colliderect(TOP_BOUNDARY):
            right_paddle_state = PADDLE_STOP
            right_paddle.top = TOP_BOUNDARY.bottom
        if right_paddle.colliderect(BOTTOM_BOUNDARY):
            right_paddle_state = PADDLE_STOP
            right_paddle.bottom = BOTTOM_BOUNDARY.top

        # update ball position
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # bounce ball off paddles and boundaries
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            if ball.colliderect(left_paddle):
                ball.left = left_paddle.right
            else:
                ball.right = right_paddle.left
            ball_speed_x = -ball_speed_x

        if ball.colliderect(LEFT_BOUNDARY) or ball.colliderect(RIGHT_BOUNDARY):
            game_state = GAME_STOP
            if ball.colliderect(LEFT_BOUNDARY):
                right_score += 1
            if ball.colliderect(RIGHT_BOUNDARY):
                left_score += 1
            if left_score == MAX_SCORE or right_score == MAX_SCORE:
                game_state = GAME_OVER
            ball.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

        if ball.colliderect(TOP_BOUNDARY) or ball.colliderect(BOTTOM_BOUNDARY):
            if ball.colliderect(TOP_BOUNDARY):
                ball.top = TOP_BOUNDARY.bottom
            else:
                ball.bottom = BOTTOM_BOUNDARY.top
            ball_speed_y = -ball_speed_y

    # draw scene
    DISPLAY_SURFACE.fill(BLACK)
    for rect in (NET,
                 TOP_BOUNDARY, BOTTOM_BOUNDARY,
                 LEFT_BOUNDARY, RIGHT_BOUNDARY,
                 left_paddle, right_paddle, ball):
        pygame.draw.rect(DISPLAY_SURFACE, WHITE, rect)

    left_score_surface = FONT.render('{:d}'.format(left_score), True, WHITE)
    right_score_surface = FONT.render('{:d}'.format(right_score), True, WHITE)
    left_score_rect = left_score_surface.get_rect()
    right_score_rect = right_score_surface.get_rect()
    left_score_rect.center = (SCORE_POS_LEFT, SCORE_POS_Y)
    right_score_rect.center = (SCORE_POS_RIGHT, SCORE_POS_Y)
    DISPLAY_SURFACE.blit(left_score_surface, left_score_rect)
    DISPLAY_SURFACE.blit(right_score_surface, right_score_rect)

    if game_state == GAME_OVER:
        DISPLAY_SURFACE.blit(GAME_OVER_SURFACE, GAME_OVER_RECT)
    
    pygame.display.update()
    FPS_CLOCK.tick(FRAMES_PER_SECOND)

