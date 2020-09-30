# !/usr/bin/python3
# coding : utf-8

""" Tutorial zero of my pygame learning"""

import pygame
from pygame.locals import *


class Window():
    """Handle a graphical windows"""
    def __init__(self, resolution: tuple):
        """Default constructor"""
        self.window = pygame.display.set_mode(resolution)
        self.resolution = resolution
        self.run = True

    def _handle_event(self):
        """handle event in our class"""
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False

    def update(self):
        """Update"""

    def draw(self):
        """Draw call"""
        pygame.display.update()

    def game_loop(self):
        while self.run:
            self._handle_event()
            self.update()
            self.draw()


def main():
    pygame.init()
    Win = Window((640, 480))
    Win.game_loop()


if __name__ == "__main__":
    main()
