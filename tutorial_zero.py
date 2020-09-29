# !/usr/bin/python3
# coding : utf-8

""" Tutorial zero of my pygame learning"""

import pygame
from pygame.locals import *


def main() -> int:
    pygame.init()
    window = pygame.display.set_mode((640, 480))
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
