# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (C) 2020
# Jens Hannemann, Kentucky State University, jens.hannemann@kysu.edu

import sys
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

FRAMES_PER_SECOND = 30

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

pygame.init()
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
    if left_paddle_state == PADDLE_UP:
        left_paddle.y -= PADDLE_SPEED
    elif left_paddle_state == PADDLE_DOWN:
        left_paddle.y += PADDLE_SPEED
    
    if right_paddle_state == PADDLE_UP:
        right_paddle.y -= PADDLE_SPEED
    elif right_paddle_state == PADDLE_DOWN:
        right_paddle.y += PADDLE_SPEED

    # draw scene
    DISPLAY_SURFACE.fill(BLACK)
    for rect in (NET,
                 TOP_BOUNDARY, BOTTOM_BOUNDARY,
                 LEFT_BOUNDARY, RIGHT_BOUNDARY,
                 left_paddle, right_paddle):
        pygame.draw.rect(DISPLAY_SURFACE, WHITE, rect)
    
    pygame.display.update()
    FPS_CLOCK.tick(FRAMES_PER_SECOND)

