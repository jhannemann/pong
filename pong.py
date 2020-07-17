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

pygame.init()

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

    # draw scene
    DISPLAY_SURFACE.fill(BLACK)
    pygame.display.update()
